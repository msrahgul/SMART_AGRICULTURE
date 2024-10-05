import pandas as pd

# Load datasets
crop_data = pd.read_csv('E:\\HACKATHON\\ChatBot\\ChatBot\\India Agriculture Crop Production1.csv')
rainfall_data = pd.read_csv('E:\\HACKATHON\\ChatBot\\ChatBot\\MONTHLY RAINFALL-District Level Data (1990-2015).csv')

def recommend_crop(district, soil_type):
    # Strip any leading/trailing spaces and convert to lowercase for comparison
    district = district.strip().lower()
    
    # Check unique district names for debugging
    print("Available districts in crop dataset:", crop_data['District'].unique())

    # Filter the crop data for the given district and soil type
    filtered_crop_data = crop_data[
        (crop_data['District'].str.strip().str.lower() == district) &
        (crop_data['Soil_Type'].str.lower() == soil_type.lower())  # Ensure this matches your dataset's column name
    ]

    # Check if there are any crops for the specified district and soil type
    if filtered_crop_data.empty:
        print(f"No crop data available for {district} with soil type {soil_type}.")
        return

    # Sort the crops by average yield
    sorted_crop_data = filtered_crop_data.sort_values(by='Average_Yield', ascending=False)

    # Get the top crop recommendation
    top_crop = sorted_crop_data.iloc[0]
    print(f"We recommend planting {top_crop['Crop_Name']} in {district}.")
    print(f"Average Yield: {top_crop['Average_Yield']} tonnes per hectare")
    print(f"Average Area: {top_crop['Area']} hectares")
    print(f"Predominant Soil Type: {top_crop['Soil_Type']}")
    print(f"Common Season: {top_crop['Season']}")

    # Retrieve rainfall details for the district
    rainfall_details = rainfall_data[rainfall_data['District'].str.strip().str.lower() == district]
    
    if not rainfall_details.empty:
        annual_rainfall = rainfall_details['Annual_Rainfall'].values[0]
        print(f"Annual Rainfall: {annual_rainfall}")

        # Display monthly rainfall data
        print("Rainfall Details (mm) for the Whole Year Season:")
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December']
        for month in months:
            month_rainfall = rainfall_details[month].values[0]
            print(f"- {month}: {month_rainfall} mm")
    else:
        print(f"No rainfall data available for {district}.")
