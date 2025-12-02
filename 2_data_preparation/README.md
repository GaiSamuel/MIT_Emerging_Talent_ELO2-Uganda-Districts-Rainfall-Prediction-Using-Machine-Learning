# ⚙️ Data Preparation Scripts

**Goal:** This folder contains the Python notebooks used to transform raw
 climate data (GRIB/Shapefiles) into clean, usable CSVs.

## 1. Spatial Setup

*This script prepares the geographical boundaries used to aggregate climate data.*

<!-- markdownlint-disable MD013 -->
| Script Name | Input (Read) | Process | Output (Save) |
| :--- | :--- | :--- | :--- |
| `processing_uganda_districts_shapefile.ipynb` | `uga_admbnda_adm2_ubos_20200824.shp` (Raw Shapefile) | Loads the official administrative boundaries, simplifies geometry for faster processing, and validates district names. | A simplified GeoDataFrame used internally by subsequent scripts for spatial joins. |
<!-- markdownlint-enable MD013 -->

---

## 2. Variable Extraction (Raw $\rightarrow$ Level 1)

*These scripts iterate through raw climate files, apply a spatial join with the
 district shapefile, and calculate the monthly mean for each district.*

<!-- markdownlint-disable MD013 -->
| Script Name | Input Data | Process | Output File (Saved to `/1_datasets`) |
| :--- | :--- | :--- | :--- |
| `processing_chirps_rainfall_data.ipynb` | CHIRPS Raster (`.tif`) | Performs **Zonal Statistics** to calculate average rainfall per district polygon. | `uganda_districts_monthly_rainfall.csv` |
| `processing_temperature.ipynb` | ERA5 Temperature (`.grib`) | Spatially joins grid points to districts; aggregates monthly means. | `uganda_monthly_temperature_1981_2025.csv` |
| `process_dewpoint_temperature.ipynb` | ERA5 Dewpoint (`.grib`) | Spatially joins grid points to districts; aggregates monthly means. | `uganda_monthly_dewpoint_temperature_1981_2025.csv` |
| `processing_precipitation.ipynb` | ERA5 Precipitation (`.grib`) | Extracts total precipitation (used for imputation ratios). | `uganda_monthly_precipitation_1981_2025.csv` |
| `processing_pressure.ipynb` | ERA5 Pressure (`.grib`) | Extracts surface pressure data. | `uganda_monthly_pressure_1981_2025.csv` |
| `processing_total_cloud_cover.ipynb` | ERA5 Cloud Cover (`.grib`) | Extracts cloud cover fraction. | `uganda_monthly_total_cloud_cover_1981_2025.csv` |
| `processing_wind_u_component.ipynb` | ERA5 Wind U (`.grib`) | Extracts Zonal (East-West) wind vectors. | `uganda_monthly_wind_u_component_1981_2025.csv` |
| `processing_wind_v_component.ipynb` | ERA5 Wind V (`.grib`) | Extracts Meridional (North-South) wind vectors. | `uganda_monthly_wind_v_component_1981_2025.csv` |
<!-- markdownlint-enable MD013 -->

---

## 3. Merging & Cleaning (Level 1 $\rightarrow$ Level 2)

*This is the final assembly step that creates the Master Dataset.*

<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD013 -->
| Script Name | Inputs | Process | Output (Saved to `/1_datasets`) |
| :--- | :--- | :--- | :--- |
| `merge_datasets.ipynb` | All CSVs generated in Step 2. | 1. **Merges** all 8 variables on `District`, `Region`, `Date`.<br>2. **Converts Units** (Kelvin $\rightarrow$ Celsius).<br>3. **Imputes Missing Data** (Fills gaps in CHIRPS/Temp/Surface Pressure using ERA5 ratios and climatology).<br>4. **Drops** invalid districts. | **`uganda_monthly_rainfall_and_climate_variables_1981_2025.csv`**<br>*(This is the clean file used for analysis)* |
<!-- markdownlint-enable MD013 -->
<!-- markdownlint-enable MD033 -->
