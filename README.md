# Busia Sensor Data Quality Control (Level 2 Checks)

This repository contains scripts and methods for performing **quality control (QC)** on environmental sensor data collected from **28 stations in Busia County, Kenya**.  
The QC checks focus on ensuring **internal consistency** of weather measurements across neighbouring stations.

---

## 📌 Project Overview
Environmental sensors were installed in Busia to collect weather data at **15-minute intervals**.  
The measured variables include:

- 🌡️ Air Temperature (`Tair`)
- 💧 Relative Humidity (`RH`)
- 🌧️ Rainfall (`Rain`)
- 🌬️ Wind Speed (`WindSpeed`)
- 🧭 Wind Direction (`WindDir`)
- 🌍 Atmospheric Pressure (`Pressure`)

This project implements **Level 2 Quality Control**, which applies **spatial and temporal consistency checks**.

---

## ⚙️ Level 2 Quality Checks

1. **SO_All – Spatial Outlier Check**  
   For each station and timestamp, verify if the **z-score of an observation (median-adjusted, IQR-scaled)** lies within the threshold compared to neighbours.

2. **FZ_Rain – Faulty Zeros Check**  
   For each station with a **rainfall reading of zero**, compare against the **median rainfall of ≥5 neighbouring stations** at the same timestamp.

3. **HI_Rain – High Rainfall Check**  
   For each station and timestamp, compare rainfall against neighbourhood medians.  
   Flag as `HI_Rain=2` if rainfall exceeds a **variable threshold**.

4. **Temporal Consistency Check**  
   If the time gap between consecutive measurements at a station is **> 15 minutes**,  
   flag the value as **`-1` (not enough info to validate)** for step/spike checks.

---

📌 Notes

Some stations (e.g., Station 16, Station 23, Station 24, Station 28, Station 8) are geographically isolated → no neighbours within 4 km.

For such stations, some QC checks cannot be performed → flagged as -1.

👩‍💻 Author
Lorraine Atsulu
