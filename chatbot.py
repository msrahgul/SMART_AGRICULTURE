import pandas as pd
from soil_classifier import classify_soil
import tkinter as tk
from tkinter import filedialog

def load_crop_data(crop_data_path):
    crop_data = pd.read_csv(crop_data_path)
    return crop_data

def recommend_crops(crop_data, soil_type, district):
    # Filter data for the specific district and soil type
    filtered_data = crop_data[(crop_data['District'].str.lower() == district.lower()) & 
                               (crop_data['Soil_Type'].str.lower() == soil_type.lower())]
    
    if filtered_data.empty:
        return "No crop recommendations available for this district and soil type."

    # Group by Crop and get the maximum yield for each crop
    best_yield_crops = filtered_data.groupby('Crop', as_index=False)['Yield'].max()
    best_yield_crops = best_yield_crops.sort_values(by='Yield', ascending=False)
    
    return best_yield_crops

def chatbot():
    crop_data_path = "E:\\HACKATHON\\ChatBot\\ChatBot\\India_Agriculture_Crop_Production_with_Soil_Types.csv"
    crop_data = load_crop_data(crop_data_path)

    print("Welcome to the Smart Farming Chatbot!")
    print("Available columns in crop data:", crop_data.columns)
    
    # Create a Tkinter window for file dialog
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask for image file
    image_path = filedialog.askopenfilename(title="Select an image for soil type identification",
                                             filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if not image_path:
        print("No image selected. Exiting...")
        return

    soil_type = classify_soil(image_path)  # Assuming this function returns the soil type
    print("Identified Soil Type:", soil_type)

    district = input("Enter District (or type 'exit' to quit): ")
    
    if district.lower() == 'exit':
        print("Thank you for using the Smart Farming Chatbot. Goodbye!")
        return

    recommended_crops = recommend_crops(crop_data, soil_type, district)
    
    # Display the recommended crops
    if isinstance(recommended_crops, str):
        print(recommended_crops)
    else:
        print("Recommended Crops and Their Best Yields:")
        for index, row in recommended_crops.iterrows():
            print(f"Crop: {row['Crop']}, Best Yield: {row['Yield']}")

if __name__ == "__main__":
    chatbot()
