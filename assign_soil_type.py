import pandas as pd

# Load the CSV file
file_path = "E:\\HACKATHON\\ChatBot\\ChatBot\\India Agriculture Crop Production.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Define soil types based on crops
soil_type_map = {
    'Rice': 'Clay',
    'Wheat': 'Clay',
    'Cotton': 'Clay',
    'Groundnut': 'Sandy',
    'Millets': 'Sandy',
    'Potato': 'Sandy',
    'Vegetables': 'Loamy',
    'Corn': 'Loamy',
    'Sugarcane': 'Loamy'
}

# Function to assign soil type based on crop
def assign_soil_type(crop):
    return soil_type_map.get(crop, 'Loamy')  # Default to 'Loamy' if crop not in the map

# Add the Soil_Type column based on the Crop column
df['Soil_Type'] = df['Crop'].apply(assign_soil_type)

# Save the updated DataFrame to a new CSV file with the Soil_Type column
updated_file_path = "D:\\ChatBot\\India Agriculture Crop Production1.csv"

try:
    df.to_csv(updated_file_path, index=False)
    print("Updated CSV with Soil_Type saved as:", updated_file_path)
except Exception as e:
    print(f"An error occurred while saving the CSV: {e}")
``