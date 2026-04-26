import pandas as pd

# EXTRACT
health_rec = pd.read_csv("healthcare_dataset.csv")

# ---------------- ETL ---------------- #

# Data Inspection
health_rec.info()

# Handle Missing Values
health_rec['Billing Amount'] = health_rec['Billing Amount'].fillna(0)

# Remove duplicates
health_rec = health_rec.drop_duplicates()

# Clean text
health_rec['Name'] = health_rec['Name'].str.strip().str.title()

# Standardize gender
health_rec['Gender'] = health_rec['Gender'].replace({'Female': 'F', 'Male': 'M'})

# Convert dates
health_rec['Date of Admission'] = pd.to_datetime(health_rec['Date of Admission'], errors='coerce')
health_rec['Discharge Date'] = pd.to_datetime(health_rec['Discharge Date'], errors='coerce')

# 🔥 NEW: Sort dataset by Name (ascending) and update it
health_rec = health_rec.sort_values(by='Name').reset_index(drop=True)

# ---------------- EDA ---------------- #

# Disease distribution (young people)
young_disease = (
    health_rec.loc[health_rec['Age'] <= 18, 'Medical Condition']
    .value_counts(normalize=True) * 100
).round(1)

print("Disease % for Age <= 18:")
print(young_disease)

# Average billing by disease
avg_cost = health_rec.groupby('Medical Condition')['Billing Amount'].mean().round(2)
print("\nAverage Billing by Disease:")
print(avg_cost)

# Gender distribution
print("\nGender Distribution:")
print(health_rec['Gender'].value_counts())

# Final structure check (no need to print twice)
print("\nFinal Dataset Info:")
health_rec.info()

# ---------------- LOAD ---------------- #

# Save cleaned + sorted dataset
health_rec.to_csv("cleaned_Health_care_data.csv", index=False)