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
