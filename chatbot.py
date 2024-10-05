import pandas as pd
from soil_classifier import classify_soil
import tkinter as tk
from tkinter import filedialog
import os

def load_crop_data(crop_data_path):
    crop_data = pd.read_csv(crop_data_path)
    return crop_data

def recommend_crop(crop_data, soil_type, district):
    # Filter data for the specific district and soil type
    filtered_data = crop_data[(crop_data['District'].str.lower() == district.lower()) & 
                               (crop_data['Soil_Type'].str.lower() == soil_type.lower())]
    
    if filtered_data.empty:
        return "No crop recommendations available for this district and soil type."

    # Get the crop with the highest yield
    recommended_crop = filtered_data.loc[filtered_data['Yield'].idxmax()]
    return recommended_crop['Crop']

def chatbot():
    crop_data_path = "E:\\HACKATHON\\ChatBot\\ChatBot\\India Agriculture Crop Production1.csv"
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

    recommended_crop = recommend_crop(crop_data, soil_type, district)
    print("Recommended Crop:", recommended_crop)

if __name__ == "__main__":
    chatbot()
