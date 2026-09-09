# National-scale Tidal Flat DEM Reconstruction Using Optical Satellite Imagery

Code accompanying the **Remote Sensing of Environment (RSE, 2026)** paper for reconstructing annual **30 m tidal-flat Digital Elevation Models (DEMs)** across the UK using **Sentinel-2 and Landsat 8/9 optical imagery**, **ICESat-2 laser altimetry**, and **machine learning**.

[![Paper](https://img.shields.io/badge/Paper-RSE%202026-orange)](https://www.sciencedirect.com/science/article/pii/S0034425726003135)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Google Earth Engine](https://img.shields.io/badge/Platform-Google%20Earth%20Engine-green)](https://earthengine.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## Example DEMs

Annual tidal-flat DEMs reconstructed for four UK estuaries.

<table>
<tr>
<td align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Morecambe_output_.gif" width="240"><br>
<b>Morecambe Bay</b>
</td>

<td align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Solway_output_.gif" width="240"><br>
<b>Solway Firth</b>
</td>

<td align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/wash_output_.gif" width="240"><br>
<b>The Wash</b>
</td>

<td align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/GIF/Thames_output_.gif" width="240"><br>
<b>Thames Estuary</b>
</td>

</tr>
</table>

---

## Overview

Tidal flats change rapidly, and their morphology is difficult to survey in the field at national scale. This project reconstructs annual 30 m tidal-flat DEMs for the UK coastline from 2019-2024 using optical satellite imagery and ICESat-2 laser altimetry.

The reconstruction workflow consists of three components:

- **STAT-ICE** -- an algorithm that automatically extracts tidal-flat elevation measurements from ICESat-2 ATL03/ATL08 observations.
- **Dual Tidal Flat Index (DTFI)** --a spectral index was developed to delineate tidal flats from turbid water using Sentinel‑2 and Landsat imagery.
- **Optical elevation proxies** -- annual composites of Normalized Annual Exposure Frequency (NAEF), NDWI, MNDWI, and Sentinel-2 Band 8A reflectance, derived from Sentinel-2 and Landsat imagery in Google Earth Engine.
- **Random Forest regression** -- combines the optical proxies with the refined ICESat-2 elevations using STAT-ICE to produce the annual 30 m tidal-flat DEMs.

---

## Interactive DEM Viewer

A Google Earth Engine app for browsing the annual tidal-flat DEM products (2019-2024):

https://minyukui.projects.earthengine.app/view/ukdem2019-2024

<img src="https://github.com/user-attachments/assets/12a8c531-b195-4b49-9f4b-bcb82dc563c3" width="1000">

---

## Reconstruction Workflow

<p align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/Fig.3_paper4_new.jpg" width="1000">
</p>

**Figure 1.** Overall workflow of the DEM reconstruction framework. Four optical elevation proxies (NAEF, annual mean NDWI, annual mean MNDWI, and annual mean Sentinel-2 Band 8A reflectance) are integrated with refined ICESat-2 elevations through a Random Forest model to generate annual tidal-flat DEMs.

---

## STAT-ICE Algorithm

<p align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/Fig.6_paper4.jpg" width="1000">
</p>

**Figure 2.** Workflow of the Statistical Automated Tidal Flat Elevation Extraction from ICESat-2 (STAT-ICE) algorithm, which automatically extracts tidal-flat elevation measurements from ICESat-2 observations.

---

## Dual Tidal Flat Index (DTFI)

The DTFI is a spectral index for tidal-flat mapping using Sentinel-2 and Landsat imagery.

Interactive visualization: https://minyukui.projects.earthengine.app/view/dtfi

<p align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/papar5_FigS4_combine.jpg" width="1000">
</p>

**Figure 3.** DTFI results for ten estuaries, compared with NDWI and the resulting binary water/non-water classifications derived from Sentinel-2 and Landsat imagery.

---

## Data

This project uses:

- Sentinel-2 MSI and Landsat 8/9 OLI/OLI2 imagery
- ICESat-2 ATL03/ATL08 observations
- Google Earth Engine
- Random Forest regression

---

## Citation

If you use this repository in your research, please cite:

```bibtex
@article{xxxx,
  title={National-scale Tidal Flat DEM Reconstruction Using Optical Satellite Imagery},
  author={...},
  journal={Remote Sensing of Environment},
  year={2026},
  volume={...},
  pages={...},
  doi={...}
}
```

---

## Acknowledgements

We acknowledge the following open datasets and platforms:

- NASA ICESat-2 Mission
- ESA Sentinel-2 Mission
- Google Earth Engine

---

## License

This project is released under the MIT License.

