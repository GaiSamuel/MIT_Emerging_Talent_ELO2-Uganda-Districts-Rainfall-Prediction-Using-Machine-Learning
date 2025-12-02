# **Uganda Districts' Rainfall Prediction using Machine Learning**

## **The Problem Identification (Milestone 1)**

### The Problem

Uganda’s economy and food security are fundamentally tied to rain-fed agriculture,
 making the country highly sensitive to climate variability. The recent Uganda
  National Meteorological Authority (UNMA)
  outlook predicts "above-normal" (enhanced) rainfall for the SOND 2025 season
   across most of the country. While increased rainfall is generally beneficial,
    this excess introduces critical risks that farmers are currently unprepared
     for, including water logging, nutrient leaching, and significant post-harvest
      losses due to poor drying conditions.

In specific high-risk zones like the Elgon and Kigezi sub-regions, this enhanced
 rainfall threatens crop destruction through landslides and flash floods. The core
  issue is that without precise, district-level predictions, farmers lack the
   granular data needed to effectively time planting or prepare drainage infrastructure
    to mitigate these specific local excesses.

### **Research Question**

> **Can we use historical ERA5 climate data and Climate Hazards data (CHIRPS) to**
**generate granular, district-level rainfall forecasts that allow farmers to**
**anticipate and mitigate the risks of "above-normal" rainfall events?**

### Domain Knowledge

*Based on the [UNMA SOND 2025 Seasonal Rainfall Outlook](https://meteo.mwe.go.ug/media/downloads/files/September%20to%20December%20(SOND)%202025%20Seasonal%20Rainfall%20Outlook%20(1)_compressed.pdf):*

- **Key Risk 1: Agronomic Instability:** The forecasted "above-normal" rains
 pose a high risk of soil nutrient leaching and water logging, which can rot root
  crops like beans and cassava if drainage is not managed.
- **Key Risk 2: Post-Harvest Loss:** Continuous heavy rains during harvest periods
 create poor drying conditions, leading to mold and storage losses for cereal crops.
- **System View (Geographic Vulnerability):** The impact is not uniform; mountainous
 regions (Elgon, Kigezi, Rwenzori) face physical destruction of farmland via landslides,
  while urbanizing areas face flash floods.
- *[Link to full Domain Research in `/0_domain_research`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/0_domain_study/0_domain_research.md)*

---

## 💾 2. Data Strategy (Milestone 2)

> ![Uganda Districts by Redion](graphs/uganda_districts_by_region.png)

### Modeling the World

To capture the complexity of Uganda's climate, we adopted a **multi-source data
 strategy**, combining high-resolution satellite rainfall data with broad
  atmospheric reanalysis models. We aggregate this data spatially using official
   administrative boundaries to create a **District-Level Time Series** for every
    district in Uganda.

**Possible Flaws in this Approach:**

- **Satellite vs. Ground Truth:** We rely on **ERA5 Reanalysis data**
 (satellite + simulation). While globally consistent, it may miss "micro-climate"
  events (like a sudden storm on one specific hill) that a physical rain gauge
   would catch.
- **Climate Change Shifts:** Our model learns from history. If climate change
 causes a fundamentally *new* weather pattern (e.g., the permanent disappearance
  of the dry season), our historical model may struggle to adapt immediately.
- **Missing Districts:** ~15 districts (e.g., Kampala, Amuria) had significant
 structural missing data in the raw source and had to be excluded or heavily
  imputed, potentially reducing accuracy for those specific zones.

**Data Sources:**

1. **CHIRPS (Rainfall):** *Climate Hazards Group InfraRed Precipitation with
 Station data*. We use this as our "Ground Truth" for rainfall because it blends
  satellite imagery with actual station data, providing high accuracy for African
   regions.
2. **ERA5 (Climate Drivers):** *ECMWF Reanalysis v5*. We use this for atmospheric
 drivers (Temperature, Pressure, Wind, Cloud Cover) that influence rainfall patterns.
3. **UBOS Shapefiles:** Official Uganda Bureau of Statistics district boundaries
 (2020) used to spatially aggregate the gridded climate data.

### The Datasets

We have produced two primary clean datasets for this project, available in the
 [`clean_data/`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/1_datasets/clean_data)
  folder:

#### 1. Historical Climate Data (Training Set)

- **File:** [`uganda_monthly_rainfall_and_climate_variables_1981_2025.csv`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/1_datasets/clean_data/uganda_monthly_rainfall_and_climate_variables_1981_2025.csv)

- **Description:** The master dataset used to train our machine learning models.
 It contains 44 years of cleaned, merged, and spatially aggregated climate indicators.
- **Reproducible using:** [`cleaning_script`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/2_data_preparation/cleaning_script/merge_datasets.ipynb)
- **Dimensions:** ~64,560 Rows, 10 Columns.
- **Key Variables:** `rainfall_mm` (Target), `temperature`, `dewpoint_temperature`,
 `surface_pressure_pa`, `wind_u_component`, `wind_v_component`, `total_cloud_cover`.

#### 2. Future Forecast Data (Prediction Set)

- **File:** [`uganda_rainfall_forecasts_2025_2026.csv`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/1_datasets/clean_data/uganda_rainfall_forecasts_2025_2026.csv)

- **Description:** The output of our Random Forest model. It contains the
 14-month recursive forecast for every district.
- **Reproducible using:** [data_analysis.ipynb](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/4_data_analysis/data_analysis.ipynb)
- **Dimensions:** ~1680 Rows, 4 Columns.
- **Timeline:** November 2025 – December 2026.
- **Key Variables:** `district`, `region`, `date`, `predicted_rainfall_mm`.

### Data Processing Pipeline

Our [raw](https://drive.google.com/drive/folders/16Q1MUI4KG64qhDLebSWlTlJxiJwDZxZS)
 data processing is reproducible using the scripts in
  [`extracting_raw_data_scripts/`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/2_data_preparation/extracting_raw_data_scripts)
   folder to produce the [raw datasets](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/1_datasets/raw_data)
    in `csv` and `shapefile`.

**1. Spatial Aggregation (Zonal Statistics):**

- **CHIRPS:** We iterated through raster files and used `rasterstats` to
 calculate the mean rainfall pixels falling within each district polygon.
- **ERA5:** We read GRIB files using `xarray`, converted grid points to geometry
 objects, and performed a **Spatial Join** (`gpd.sjoin`) with the district shapefile
  to compute precise regional averages.

**2. Merging & Harmonization:**

- All 7 distinct climate variables were merged on `District`, `Region`, and `Date`.
- **Unit Conversion:** Kelvin temperatures were converted to Celsius; Pressure
 converted to Pascals.
- **Data Rescue:** We identified districts missing CHIRPS data and successfully
 imputed their values using a calculated conversion ratio from the ERA5 Precipitation
  dataset.

**3. Feature Engineering:**

- **Temporal:** Extracted `Year`, `Month`, and one-hot encoded `Seasons`
 (MAM, SON, JJA, DJF).
- **Lag Features:** Created `Lag_1` and `Lag_3` to capture the "memory" of the
 climate system.
- **Trends:** Calculated 3-month rolling averages to smooth out noise and capture
 seasonal momentum.
