# Smart Farming Chatbot

## Overview
The Smart Farming Chatbot is an interactive application designed to help farmers identify soil types and recommend suitable crops based on soil characteristics and district information. The chatbot utilizes a trained machine learning model for soil classification and a dataset containing crop production details to provide relevant recommendations.

## Features
- **Soil Type Identification**: Users can upload an image of soil, and the chatbot will classify it into one of the predefined soil types.
- **Crop Recommendations**: Based on the identified soil type and the specified district, the chatbot provides recommendations for crops that yield the best production.
- **User-Friendly Interface**: Utilizes Tkinter for a simple file dialog to select soil images.

## Requirements
- Python 3.x
- Required Libraries:
  - `tensorflow`
  - `keras`
  - `opencv-python`
  - `pandas`
  - `tkinter`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/msrahgul/SMART_AGRICULTURE.git
   cd SmartFarmingChatbot
   ```

2. Install the required packages:
   ```bash
   pip install tensorflow keras opencv-python pandas
   ```

3. Ensure you have the trained model and crop data CSV file in the correct directories:
   - Model path: `E:\\HACKATHON\\ChatBot\\ChatBot\\soil_classification_model.h5`
   - Crop data path: `E:\\HACKATHON\\ChatBot\\ChatBot\\India Agriculture Crop Production1.csv`

## Usage
1. Run the chatbot application:
   ```bash
   python chatbot.py
   ```

2. Follow the prompts in the console:
   - Select an image of soil for classification.
   - Enter the district name when prompted.

## Functionality
- The chatbot will display the identified soil type.
- Based on the soil type and district, it will provide a list of recommended crops along with their best yields.

## Project Structure
```
SmartFarmingChatbot/
│
├── chatbot.py                  # Main chatbot script
├── soil_classifier.py          # Script for soil classification
├── India_Agriculture_Crop_Production_with_Soil_Types # Crop data
└── soil_classification_model.h5 # Trained soil classification model
```

## Contributing
Contributions are welcome! Feel free to submit a pull request or report issues.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [TensorFlow](https://www.tensorflow.org/) for machine learning capabilities.
- [OpenCV](https://opencv.org/) for image processing.
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis.
```

