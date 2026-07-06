# 🌊 National-scale Tidal Flat DEM Reconstruction Using Optical Satellite Imagery

Official implementation of the **Remote Sensing of Environment (RSE, 2026)** paper for reconstructing annual **30 m tidal-flat Digital Elevation Models (DEMs)** across the UK using **Sentinel-2 and Landsat 8/9 optical imagery**, **ICESat-2 laser altimetry**, and **machine learning**.

[![Paper](https://img.shields.io/badge/Paper-RSE%202026-orange)](https://www.sciencedirect.com/science/article/pii/S0034425726003135)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Google Earth Engine](https://img.shields.io/badge/Platform-Google%20Earth%20Engine-green)](https://earthengine.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

# 🌊 Estuary Showcase

Representative annual tidal-flat DEMs generated for four major UK estuaries.

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

# 📖 Overview

Tidal flats are highly dynamic intertidal environments that play a crucial role in coastal resilience, sediment transport, blue carbon storage, and ecosystem functioning. However, their rapid morphological evolution and the difficulty of conducting field surveys make large-scale topographic mapping particularly challenging.

This repository presents an optical satellite-based framework for reconstructing annual **30 m tidal-flat DEMs** at the national scale. By integrating multi-source optical information with refined ICESat-2 elevations, the framework enables efficient, accurate, and scalable tidal-flat topography reconstruction.

---

# ✨ Highlights

- 🌊 **Developed the STAT-ICE algorithm** for automatic extraction of reliable tidal-flat elevation measurements from ICESat-2 observations.

- 🛰️ **Constructed four complementary optical elevation proxies** that comprehensively characterize tidal-flat morphology.

- 🌍 **Integrated optical proxies and refined ICESat-2 elevations** within a Random Forest framework to generate annual 30 m tidal-flat DEMs across the UK coastline from **2019–2024**.

---

# 🌍 Interactive DEM Visualization

Explore the annual tidal-flat DEM products directly in Google Earth Engine:

### 👉 https://minyukui.projects.earthengine.app/view/ukdem2019-2024

<img src="https://github.com/user-attachments/assets/12a8c531-b195-4b49-9f4b-bcb82dc563c3" width="1000">

---

# 🏞️ Workflow of DEM Reconstruction

<p align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/Fig.3_paper4_new.jpg" width="1000">
</p>

**Figure 1.** Overall workflow of the proposed DEM reconstruction framework. Four optical elevation proxies—including the Normalized Annual Exposure Frequency (NAEF), annual mean NDWI, annual mean MNDWI, and annual mean Sentinel-2 Band 8A reflectance—are integrated with refined ICESat-2 elevations through a Random Forest model to generate annual tidal-flat DEMs.

---

# 🛰️ STAT-ICE Algorithm

<p align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/Fig.6_paper4.jpg" width="1000">
</p>

**Figure 2.** Workflow of the Statistical Automated Tidal Flat Elevation Extraction from ICESat-2 (STAT-ICE) algorithm for automatically extracting reliable tidal-flat elevation measurements from ICESat-2 observations.

---

# 🌊 Dual Tidal Flat Index (DTFI)

The **Dual Tidal Flat Index (DTFI)** is a spectral index designed for robust tidal-flat mapping using Sentinel-2 and Landsat imagery.

### 🌍 Interactive Visualization

👉 https://minyukui.projects.earthengine.app/view/dtfi
<p align="center">
<img src="https://github.com/GISermyk/TideFlatRecon_UK/raw/main/Image/papar5_FigS4_combine.jpg" width="1000">
</p>

**Figure 3.** Visualization of the proposed DTFI across ten representative estuaries. The figure compares DTFI with the conventional NDWI and demonstrates the resulting binary water/non-water classifications derived from Sentinel-2 and Landsat imagery.

---


# 📊 Data

This project is developed using:

- Sentinel-2 MSI and Landsat 8/9 OLI/OLI2 imagery
- ICESat-2 ATL03/ATL08 observations
- Google Earth Engine
- Random Forest regression

---

# 📄 Citation

If you find this repository useful, please consider citing our paper:

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

# 🙏 Acknowledgements

We gratefully acknowledge the following open datasets and platforms:

- NASA ICESat-2 Mission
- ESA Sentinel-2 Mission
- Google Earth Engine

---

# 📜 License

This project is released under the MIT License.

