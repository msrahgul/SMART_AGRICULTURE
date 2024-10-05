
# Smart Farming Chatbot

This project is a **Smart Farming Chatbot** that provides crop recommendations based on soil type, district, and other agricultural factors like rainfall, wage data, and fertilizer consumption. It uses image classification to detect soil type and suggests the best crops for the district considering historical data.

## Features

- **Soil Type Detection**: Detects soil type from an image using a pre-trained model.
- **Crop Recommendations**: Recommends crops with the best yields for the given soil type and district.
- **Rainfall Data**: Displays historical monthly and annual rainfall data for the district.
- **Wage Data**: Provides the average daily wage for male and female field labor in the district.
- **Fertilizer Consumption**: Shows the fertilizer consumption (Nitrogen, Phosphate, Potash) for Kharif and Rabi seasons in the district.

## Dataset Requirements

1. **India Agriculture Crop Production with Soil Types CSV**: Contains crop production and soil type data.
2. **Monthly Rainfall Data CSV**: Contains historical monthly rainfall data for different districts.
3. **Wage Data CSV**: Contains daily wage data for male and female field labor across districts.
4. **Fertilizer Consumption Data CSV**: Contains fertilizer consumption data for both Kharif and Rabi seasons.

### Dataset Columns

#### Crop Data (CSV)
- **District**: Name of the district.
- **Crop**: Name of the crop.
- **Soil_Type**: Type of soil in the district.
- **Yield**: Crop yield in tonnes per hectare.
- **Season**: Crop season (Kharif, Rabi, etc.).

#### Rainfall Data (CSV)
- **Dist Name**: Name of the district.
- **Monthly Rainfall**: Rainfall in millimeters for each month (January to December).
- **Annual Rainfall**: Total annual rainfall in millimeters.

#### Wage Data (CSV)
- **Dist Name**: Name of the district.
- **Male Field Labour (Rs per Day)**: Daily wage for male field labor.
- **Female Field Labour (Rs per Day)**: Daily wage for female field labor.

#### Fertilizer Data (CSV)
- **Dist Name**: Name of the district.
- **Nitrogen Kharif Consumption (tons)**: Consumption of nitrogen fertilizer during Kharif season.
- **Nitrogen Rabi Consumption (tons)**: Consumption of nitrogen fertilizer during Rabi season.
- **Phosphate Kharif Consumption (tons)**: Consumption of phosphate fertilizer during Kharif season.
- **Phosphate Rabi Consumption (tons)**: Consumption of phosphate fertilizer during Rabi season.
- **Potash Kharif Consumption (tons)**: Consumption of potash fertilizer during Kharif season.
- **Potash Rabi Consumption (tons)**: Consumption of potash fertilizer during Rabi season.
- **Total Kharif Consumption (tons)**: Total fertilizer consumption during Kharif season.
- **Total Rabi Consumption (tons)**: Total fertilizer consumption during Rabi season.

## File Structure

```bash
.
├── Chatbot.py                         # Main chatbot file
├── recommendation.py                  # Contains logic for crop recommendations, rainfall, wage, and fertilizer data
├── soil_classifier.py                 # Soil type classification using an image
├── India_Agriculture_Crop_Production_with_Soil_Types.csv  # Crop data file (replace with actual path)
├── MONTHLY RAINFALL-District Level Data (1990-2015).csv   # Rainfall data file (replace with actual path)
├── Wages-District Level Data (1966-2017).csv              # Wage data file (replace with actual path)
├── Season Fertilizer consumption-District Level Data (1990-2017).csv  # Fertilizer data file (replace with actual path)
└── README.md                         # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.x
- Required Python packages:
  - `pandas`
  - `tkinter`
  - `tensorflow`
  - `opencv-python`

Install the dependencies using the following command:

```bash
pip install pandas tkinter tensorflow opencv-python
```

### Model Setup

1. Place the **soil classification model** (`soil_classification_model.h5`) at the specified path in `soil_classifier.py`.
2. Ensure that the dataset CSV files are placed at the correct paths mentioned in `recommendation.py` and `Chatbot.py`.

### Running the Chatbot

1. Run the chatbot using the following command:

```bash
python Chatbot.py
```

2. When prompted, upload an image of the soil for classification.
3. Enter the district name for which you want crop recommendations.
4. The chatbot will provide:
   - Recommended crops and their best yields.
   - Monthly and annual rainfall data.
   - Wage data for male and female labor.
   - Fertilizer consumption for Kharif and Rabi seasons.

### Example Output
![alt text](<Screenshot 2024-10-05 100026-1.png>)
![alt text](<Screenshot 2024-10-05 100038.png>)

<video controls src="OUTPUT.mp4" title="Title"></video>

## Notes

- Ensure that the image file selected for soil classification is clear and well-lit for better accuracy.
- The chatbot will gracefully exit if no image is selected or if an invalid district is entered.
- You can modify the dataset paths in the code as per your local setup.

## Future Improvements

- Expand the chatbot to provide additional data such as **water requirements** and **pest control** based on crops.
- Integrate **weather forecast** data to provide real-time recommendations.
- Add support for additional languages for better accessibility to farmers.

## License

This project is open-source and available under the MIT License.
