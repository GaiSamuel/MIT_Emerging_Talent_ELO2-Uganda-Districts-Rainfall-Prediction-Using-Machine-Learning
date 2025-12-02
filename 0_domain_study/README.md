# 📚 Domain Research: Uganda Rainfall & Agriculture

**Goal:** This folder organizes our understanding of the problem domain. It
 contains the raw background literature (PDFs), our synthesized notes, and
  external resources necessary to understand *why* this research is needed.

---

## 🧭 Directory Contents

If you are new to this project, start here to understand the context.

| File / Resource | Type | Description |
| :--- | :--- | :--- |
| **[0_domain_research.md](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/0_domain_study/0_domain_research.md)** | **Start Here** | **The Master Summary.** Our group's synthesized understanding of the problem. Includes the System Analysis, Stakeholder Breakdown, and Gap Analysis. |
| **[September to December (SOND) 2025 Seasonal Rainfall Outlook](https://meteo.mwe.go.ug/media/downloads/files/September%20to%20December%20(SOND)%202025%20Seasonal%20Rainfall%20Outlook%20(1)_compressed.pdf)** | `PDF` | **Primary Source.** The official UNMA report forecasting "Above-Normal" rainfall. Contains critical data on sector-specific impacts (Agri, Health, Disaster). |

---

## 🔗 External Resources & References

These are live links to the data sources and organizations relevant to our
 problem statement.

### 🌦️ Meteorological Data Sources

- **[Copernicus Climate Data Store (ERA5)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download)**
  **and**
 **[Climate Hazards Center](https://data.chc.ucsb.edu/products/CHIRPS-2.0/EAC_monthly/tifs/)**
: The source of our historical reanalysis and Rainfall data (1981–Present). We
 use this to train our model.
- **[Humanitarian Dat Exchange (HDX)](https://data.humdata.org/dataset/cod-ab-uga)**:
 Administrative boundaries for Uganda (District Shapefiles) to map our predictions.

### 🚜 Agriculture & Context

- **[FAO Uganda Country Profile](https://www.fao.org/uganda/en/)**:
 Background on why Uganda is dependent on rain-fed agriculture.
- **[ReliefWeb Uganda](https://reliefweb.int/country/uga)**: Reports on recent
 floods, landslides, and climate disasters in the Elgon/Kigezi regions.

---

## 🧩 Key Takeaways from Research

**1. The Problem:**
Current forecasts provided by UNMA are **Regional** (broad zones), but farmers
 need **District-Specific** (granular) data to manage risks like water logging
  and nutrient leaching.

**2. The Opportunity:**
By using historical ERA5 and climate hazards (CHIRPS) data, we can identify
 specific rainfall thresholds for
 each district. This allows us to predict not just "if" it will rain, but if it
  will rain enough to damage specific crops.

**3. The System:**
The domain is an intersection of **Meteorology** (Rainfall patterns),
 **Agriculture** (Crop cycles), and **Disaster Management** (Flood/Landslide warnings).
