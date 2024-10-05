import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data from the CSV files
def load_data():
    try:
        df = pd.read_csv("E:\\HACKATHON\\ChatBot\\ChatBot\\India Agriculture Crop Production1.csv")
    except FileNotFoundError:
        print("Crop production dataset not found.")
        return

    try:
        rainfall_df = pd.read_csv("E:\\HACKATHON\\ChatBot\\ChatBot\\MONTHLY RAINFALL-District Level Data (1990-2015).csv")
    except FileNotFoundError:
        print("Rainfall dataset not found.")
        return

    # Normalize district names in both datasets for matching
    df['District'] = df['District'].str.lower().str.strip()
    rainfall_df['Dist Name'] = rainfall_df['Dist Name'].str.lower().str.strip()

    # Merge the two datasets on district name
    df = df.merge(rainfall_df, left_on='District', right_on='Dist Name', how='left')

    # Encode 'District', 'Soil_Type', and 'Crop' using LabelEncoder
    label_encoder_district = LabelEncoder()
    label_encoder_crop = LabelEncoder()
    label_encoder_soil = LabelEncoder()

    df['District'] = label_encoder_district.fit_transform(df['District'])
    df['Soil_Type'] = label_encoder_soil.fit_transform(df['Soil_Type'])
    df['Crop'] = label_encoder_crop.fit_transform(df['Crop'])

    # Drop rows with missing values in important columns
    df = df.dropna(subset=['Soil_Type', 'District', 'Area', 'Yield', 'Crop'])

    return df, label_encoder_crop, label_encoder_district, label_encoder_soil, rainfall_df
