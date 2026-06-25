
<img width="2557" height="1320" alt="image" src="https://github.com/user-attachments/assets/12a8c531-b195-4b49-9f4b-bcb82dc563c3" />

🌊 Google Earth Engine Visualization
[Interactive DEM visualization](https://minyukui.projects.earthengine.app/view/ukdem2019-2024)

## National-scale Tidal Flat DEM Reconstruction Using Optical Satellite Imagery

Tidal flats, intertidal environments periodically exposed and inundated by tidal fluctuations, play a crucial role in enhancing coastal resilience and maintaining ecosystem
functioning. However, their rapid morphological changes and challenging field conditions make accurate, frequent mapping of tidal-flat topography over large spatial extents extremely difficult.
Here, an optical satellite-based framework was presented for national-scale tidal-flat elevation generation. Specifically, 
- A multiple tidal-flat elevation proxy strategy were proposed to comprehensively characterize tidal-flat morphology. 
- A Statistical Automated Tidal Flat Elevation Extraction from ICESat-2 (STAT-ICE) algorithm was developed to derive reliable reference elevations for proxy calibration. 
- The multiple optical proxies  and the refined ICESat-2 reference elevations were integrated within a random forest framework to generate annual 30 m tidal-flat DEMs across the UK coast from 2019 to 2024 ([🌊 Interactive DEM visualization](https://minyukui.projects.earthengine.app/view/ukdem2019-2024)).

<p align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/Fig.3_paper4_new.jpg" width="1000" style="display:inline-block; margin-right:10px;" >
<p align="left">
Fig. 1. Workflow of tidal-flat elevation derived from time-series optical satellite imagery. Four tidal-flat elevation proxies (X1–X4) were constructed, including X1: Normalized Annual Exposure Frequency (NAEF); X2: annual mean NDWI derived from Sentinel-2 imagery (NDWImean); X3: annual mean MNDWI derived from Sentinel-2 imagery (MNDWImean); and X4: annual mean Band 8A reflectance derived from Sentinel-2 imagery (B8Amean). Y represents the refined ICESat-2 elevation points.


## 🏞️ Estuary GIF Showcase

<table>
<tr>
<td align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Morecambe_output_.gif" width="230"><br>
<b>Morecambe Bay</b>
</td>
<td align="center" >
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Solway_output_.gif" width="230"><br>
<b>Solway Firth</b>
</td>
<td align="center" >
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/wash_output_.gif" width="230"><br>
<b>The Wash</b>
</td>
<td align="center" >
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Thames_output_.gif" width="230"><br>
<b>Great Thames Estuary</b>
</td>
</tr>
</table>

<td style="text-align: center; vertical-align: middle;">
    <img width="500" height="50" alt="image" src="https://github.com/user-attachments/assets/c2e71fc0-a26b-402f-803c-48b36968be27" />
</td>

## 🏞️ STAT-ICE algorithm
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/Fig.6_paper4.jpg" width="1000" style="display:inline-block; margin-right:10px;" >
Fig. 2. Flowchart of Statistical Automated Tidal Flat Elevation Extraction from ICESat-2 (STAT-ICE).


**Dual Tidal Flat Index (DTFI)**  
[View DTFI on GEE](https://minyukui.projects.earthengine.app/view/dtfi)
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/papar5_FigS4_combine.jpg" width="1000" style="display:inline-block; margin-right:10px;" >
Fig. 2. Visualization of DTFI and generated water/non-water binary mapping at ten estuaries based on the Sentinel-2 and Landsat 8 images. (a1–a10) True-color Sentinel-2 MSI images (bands 4–3–2) acquired at low tide; (b1–b10) corresponding DTFI visualization results; (c1–c10) NDWI visualization results; and (d1–d10) binary water/non-water maps derived from DTFI > 0.2 and NDWI < 0.2 in the corresponding Sentinel-2 images. (e1–e10) True-color Landsat 8 images (bands 4–3–2) acquired at low tide; (f1–f10) corresponding DTFI visualization results; (g1–g10) NDWI visualization results; and (h1–h10) binary water/non-water maps derived from DTFI > 0.2 and NDWI < 0.2 in the corresponding Landsat 8 images.



