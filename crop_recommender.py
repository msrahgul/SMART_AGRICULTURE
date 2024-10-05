def recommend_crop(crop_data, soil_type, district):
    # Filter data based on the identified soil type and district
    filtered_data = crop_data[(crop_data['Soil_Type'] == soil_type) & (crop_data['District'].str.lower() == district.lower())]

    # Check if there are any crops for the given criteria
    if filtered_data.empty:
        return "No crop recommendations available for this soil type in the specified district."

    # Find the crop with the highest yield
    recommended_crop = filtered_data.loc[filtered_data['Yield'].idxmax()]

    return recommended_crop['Crop']  # Return the name of the recommended crop
