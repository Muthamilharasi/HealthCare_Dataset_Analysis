# 🏥 Healthcare Data Analysis Project

## 📌 Overview

This project focuses on performing end-to-end data analysis on a healthcare dataset. It includes data cleaning, transformation (ETL), exploratory data analysis (EDA), and generation of meaningful insights to support data-driven decision-making.

---

## ⚙️ Tools & Technologies

* Python (Pandas)
* SQL (MySQL)
* Tableau (for dashboard visualization)
* Git & GitHub

---

## 🔄 ETL Process

### Extract

* Imported raw healthcare dataset using Pandas

### Transform

* Handled missing values
* Removed duplicate records
* Standardized categorical data (e.g., Gender)
* Cleaned text fields (Name formatting)
* Converted date columns to proper datetime format
* Sorted dataset for better organization

### Load

* Exported cleaned dataset to CSV
* (Optional) Loaded data into MySQL for structured querying

---

## 📊 Exploratory Data Analysis (EDA)

Performed analysis to identify:

* Disease distribution across patients
* Most common diseases affecting young individuals (≤18 years)
* Average billing amount per medical condition
* Gender distribution of patients

---

## 🔍 Key Insights

* Identified top diseases affecting younger patients
* Observed variations in billing amounts across medical conditions
* Found distribution patterns based on gender

---

## 📁 Project Structure

* `analysis.py` → Python script (ETL + EDA)
* `healthcare_dataset.csv` → Raw dataset
* `cleaned_sorted_data.csv` → Cleaned dataset

---

## ▶️ How to Run

1. Install required libraries:

   ```
   pip install pandas
   ```

2. Run the script:

   ```
   python analysis.py
   ```

---


## 👤 Author

Muthamilharasi
Aspiring Data Analyst | AI & Data Science Student

---
