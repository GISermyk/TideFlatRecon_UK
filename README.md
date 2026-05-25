
# National-scale Tidal Flat DEM Reconstruction Using Optical Satellite Imagery
Tidal flats, intertidal environments periodically exposed and inundated by tidal fluctuations, play a crucial role in enhancing coastal resilience and maintaining ecosystem
functioning. However, their rapid morphological changes and challenging field conditions make accurate, frequent mapping of tidal-flat topography over large spatial extents extremely difficult.
Here, an optical satellite-based framework was presented for national-scale tidal-flat elevation generation. Specifically, 
- A multiple tidal-flat elevation proxy strategy were proposed to comprehensively characterize tidal-flat morphology. 
- A Statistical Automated Tidal Flat Elevation Extraction from ICESat-2 (STAT-ICE) algorithm was developed to derive reliable reference elevations for proxy calibration. 
- The multiple optical proxies derived from time-series Sentinel-2 and Landsat-8/9 imagery and the refined ICESat-2 reference elevations were integrated within a random forest framework to generate annual 30 m tidal-flat DEMs across the UK coast from 2019 to 2024.

<p align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/Fig.3_paper4_new.jpg" width="1000" style="display:inline-block; margin-right:10px;" >
<p align="left">
Fig. 3. Workflow of tidal-flat elevation derived from time-series optical satellite imagery. Four tidal-flat elevation proxies (X1–X4) were constructed, including X1: Normalized Annual Exposure Frequency (NAEF); X2: annual mean NDWI derived from Sentinel-2 imagery (NDWImean); X3: annual mean MNDWI derived from Sentinel-2 imagery (MNDWImean); and X4: annual mean Band 8A reflectance derived from Sentinel-2 imagery (B8Amean). Y represents the refined ICESat-2 elevation points.

<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/Fig.6_paper4.jpg" width="1000" style="display:inline-block; margin-right:10px;" >

## 🌊 Google Earth Engine Visualization

**Dual Tidal Flat Index (DTFI)**  
[View DTFI on GEE](https://minyukui.projects.earthengine.app/view/dtfi)

**Annual UK Tidal Flat DEM (2019–2024)**  
[Interactive DEM visualization](https://minyukui.projects.earthengine.app/view/ukdem2019-2024)

---

## 🏞️ Estuary GIF Showcase


<div>
  <img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Morecambe_output.gif" width="300" style="display:inline-block; margin-right:10px;" />
  <img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Solway_output.gif" width="300" style="display:inline-block; margin-right:10px;" />
</div>

<div style="margin-top:10px;">
  <img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/wash_output.gif" width="300" style="display:inline-block; margin-right:10px;" />
  <img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Thames_output.gif" width="300" style="display:inline-block; margin-right:10px;" />
</div>
