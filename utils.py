

import ee
import collections
import os
import geemap
import subprocess
import math


def get_s1_collection(aoi, start_date, end_date):
    
    S1_grd = ee.ImageCollection("COPERNICUS/S1_GRD")\
        .filter(ee.Filter.eq('instrumentMode', 'IW'))\
        .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))\
        .filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))\
        .filterBounds(aoi)\
        .filterDate(start_date, end_date)\
        .select(['VV', 'VH'])
        
    return S1_grd


def get_s2_sr_cld_col(aoi, start_date, end_date, CLOUDY_PIXEL_PERCENTAGE):
    # Import and filter S2 SR.
    s2_sr_col = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')\
        .filterBounds(aoi)\
        .filterDate(start_date, end_date)\
        .filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', CLOUDY_PIXEL_PERCENTAGE)))

    # Import and filter s2cloudless.
    s2_cloudless_col = (ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')\
        .filterBounds(aoi)\
        .filterDate(start_date, end_date))\
        

    # Join the filtered s2cloudless collection to the SR collection by the 'system:index' property.
    return ee.ImageCollection(ee.Join.saveFirst('s2cloudless').apply(**{
        'primary': s2_sr_col,
        'secondary': s2_cloudless_col,
        'condition': ee.Filter.equals(**{
            'leftField': 'system:index',
            'rightField': 'system:index'
        })
    }))
    
def add_cloud_bands(img):
    
     # Get s2cloudless image, subset the probability band.
    cld_prb = ee.Image(img.get('s2cloudless')).select('probability')
  
    #Condition s2cloudless by the probability threshold value.
    is_cloud = cld_prb.lte(60).rename('cloud')
  
    #Add the cloud probability layer and cloud mask as image bands.
    img =  img.addBands(ee.Image([cld_prb, is_cloud]))
      
    return img.updateMask(is_cloud).unmask(0)

# def VI_cal_S2(img):
#     NDWI = img.normalizedDifference(['B3','B8']).rename('NDWI')
#     NDVI = img.normalizedDifference(['B8', 'B4']).rename('NDVI')
#     MNDWI = img.normalizedDifference(['B3','B11']).rename('MNDWI')
#     NDVI = img.normalizedDifference(['B8', 'B4']).rename('NDVI')                    
#     TFI = img.expression('(100*B8)/(B4*(B8-B4+100))',
#                           {
#                           'B8': img.select('B8'),
#                           'B4': img.select('B4')
#                           }).rename('TFI')
#     return img.addBands(NDWI).addBands(TFI).addBands(NDVI).addBands(MNDWI)
def S1_index(img):
    
    TB = img.expression("(10**(VV/10)) + (10**(VH/10))",
                        {
                          'VV': img.select('VV'),
                          'VH': img.select('VH'),
                        }).rename('TB')
    TB = TB.log().multiply(10/math.log(10))
    return img.addBands(TB)

def VI_cal_S2(img):
    NDWI = img.normalizedDifference(['B3','B8']).rename('NDWI')
    NDVI = img.normalizedDifference(['B8', 'B4']).rename('NDVI')
    MNDWI = img.normalizedDifference(['B3','B11']).rename('MNDWI')
    NDVI = img.normalizedDifference(['B8', 'B4']).rename('NDVI')                    
    TFI = img.expression('(NIR*(NIR+red))/(20*red*(NIR-red))',
                        {
                          'NIR':img.select('B8'),
                          'red':img.select('B4'),
                        }).rename('TFI')
    return img.addBands(NDWI).addBands(TFI).addBands(NDVI).addBands(MNDWI)

# def VI_cal_L8(img):
    
#     NDVI = img.normalizedDifference(['SR_B5','SR_B4']).rename('NDVI')
#     NDWI = img.expression('(green - nir)/(green + nir)',
#                           {
#                             'green': img.select('SR_B3'),
#                             'nir'  : img.select('SR_B5')
#                           }).rename('NDWI')

#     TFI = img.expression('(100*B8)/(B4*(B8-B4+50))',
#                           {
#                           'B8': img.select('SR_B5'),
#                           'B4': img.select('SR_B4')
#                           }).rename('TFI')
                          
#     return img.addBands(TFI).addBands(NDWI).addBands(NDVI)

def VI_cal_L8(img):
    
    NDVI = img.normalizedDifference(['SR_B5','SR_B4']).rename('NDVI')
    NDWI = img.expression('(green - nir)/(green + nir)',
                          {
                            'green': img.select('SR_B3'),
                            'nir'  : img.select('SR_B5')
                          }).rename('NDWI')
    MNDWI = img.expression('(green - SWIR1)/(green + SWIR1)',
                          {
                            'green': img.select('SR_B3'),
                            'SWIR1'  : img.select('SR_B6')
                          }).rename('MNDWI')

    TFI = img.expression('(NIR*(red+NIR))/(20*red*(NIR-red))',
                        {
                          'NIR':img.select('SR_B5'),
                          'red':img.select('SR_B4'),
                        }).rename('TFI')
                          
    return img.addBands(TFI).addBands(NDWI).addBands(MNDWI).addBands(NDVI)

def CR(img):
    CR = img.expression('VH - VV',
                        {
                        'VV':img.select('VV'),
                        'VH':img.select('VH')
                        }).rename('CR')
    
    return img.addBands(CR.rename('CR'))

def TF_binary_cal(img):
    
    TFI = img.select('TFI').gt(0.2)#.and(img.select('TFI').lt(1))
    NDWI = img.select('NDWI').lt(0.2)
    TF_binary = TFI.And(NDWI)
    return TF_binary.rename('TF')

def Cal_doy(img):
    doy = ee.Date(img.get('system:time_start')).getRelative('day', 'year').add(1)
    return img.set('DOY', doy)

def cloud_mask_L8(img):
    qa = img.select('QA_PIXEL')
    cloudShadowBitMask = 1 << 3
    cloudsBitMask = 1 << 5
    cirrusBitMask = 1 << 4
    dilatedCloudBitMask = 1 << 1
  
    cloud = qa.bitwiseAnd(cloudShadowBitMask).eq(0)\
                 .And(qa.bitwiseAnd(cloudsBitMask).eq(0))\
                 .And(qa.bitwiseAnd(cirrusBitMask).eq(0))\
                 .And(qa.bitwiseAnd(dilatedCloudBitMask).eq(0))
    
    return img.addBands(cloud.rename('cloud')).updateMask(cloud).unmask(0)

def Landsat_SR_corvert(image):
    opticalBands = image.select('SR_B.').multiply(0.275).add(-2000)
    thermalBands = image.select('ST_B.*').multiply(0.00341802).add(149.0)
    return image.addBands(opticalBands, None, True)\
                .addBands(thermalBands, None, True)
                
def band_rename_L89(img):
    return img.select(['SR_B2','SR_B3','SR_B4','SR_B5','NDWI', 'TFI','NDVI', 'cloud'], ['B2','B3','B4','B8','NDWI', 'TFI','NDVI', 'cloud'])

def Norm(img):
    tfi_mask = img.select('TFI').gt(0).And(img.select('TFI').lt(2))
    NDVI_mask = img.select('NDVI').gt(0)
    NDWI_mask = img.select('NDWI').lt(0)
    return img.mask(tfi_mask.And(NDVI_mask).And(NDWI_mask)).unmask(0)

def normalized_TFI(img):
    tfi_mask = img.select('TFI').gt(0.2).And(img.select('TFI').lt(5))
    ndvi_mask = img.select('NDVI').gt(0)
    ndwi_mask = img.select('NDWI').lt(0)
    zz = img.select('NDWI').mask(ndvi_mask.And(tfi_mask).And(ndwi_mask)).unmask(1)
    return img.addBands(zz.rename('NDWI_norm'))

def TF_get(img):
    TFI = img.select('TFI').gt(0.2).And(img.select('TFI').lt(2))
    NDWI = img.select('NDWI').lt(0.2)
    TF_binary = TFI.And(NDWI)
    return img.addBands(TF_binary.rename('TF'))

def Landsat_processing(roi, Collection, data_start, data_end):
    Landsat_C = (Collection
                 .filterDate(data_start, data_end)
                 .filterBounds(roi)
                 .map(Landsat_SR_corvert)
                 .map(cloud_mask_L8)
                 .map(Cal_doy))

    doy_list = Landsat_C.aggregate_array('DOY').distinct()

    def make_unique_doy(doy):
        doy_num = ee.Number(doy)
        unique_doy = (Landsat_C
                      .filter(ee.Filter.eq('DOY', doy_num))
                      .mosaic()
                      .set('DOY', doy_num))
        return unique_doy

    def CLIP(img):
        return img.clip(roi)
    
    # 在 Python API 中，map 的参数是一个 Python 函数
    unique_doy_collection = doy_list.map(make_unique_doy)

    return  ee.ImageCollection(unique_doy_collection).map(CLIP)#.map(cal_cloud_per).filter(ee.Filter.gt('cloud_per', 40))
