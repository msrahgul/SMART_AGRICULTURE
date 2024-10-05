import pandas as pd
from daal4py.sklearn.ensemble import RandomForestClassifier  # Intel oneAPI optimized
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# 1. Load Data
def load_data(crop_data_path, rainfall_data_path):
    df = pd.read_csv(crop_data_path)
    rainfall_df = pd.read_csv(rainfall_data_path)

    df['District'] = df['District'].str.lower().str.strip()
    rainfall_df['Dist Name'] = rainfall_df['Dist Name'].str.lower().str.strip()

    df = df.merge(rainfall_df, left_on='District', right_on='Dist Name', how='left')

    label_encoder_district = LabelEncoder()
    label_encoder_crop = LabelEncoder()
    label_encoder_soil = LabelEncoder()

    df['District'] = label_encoder_district.fit_transform(df['District'])
    df['Soil_Type'] = label_encoder_soil.fit_transform(df['Soil_Type'])
    df['Crop'] = label_encoder_crop.fit_transform(df['Crop'])

    df = df.dropna(subset=['Soil_Type', 'District', 'Area', 'Yield', 'Crop'])

    return df, label_encoder_crop, label_encoder_district, label_encoder_soil

# 2. Rainfall Data Processing
def get_rainfall_data(district_data):
    if district_data.isnull().any():
        return "Data not available", {month: "Data not available" for month in ['January', 'February', 'March', 'April', 
                                                                      'May', 'June', 'July', 'August', 
                                                                      'September', 'October', 'November', 'December']}
    
    annual_rainfall = float(district_data['ANNUAL RAINFALL (Millimeters)'])
    monthly_rainfall = {
        month: float(district_data[f'{month.upper()} RAINFALL (Millimeters)']) for month in
        ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
         'September', 'October', 'November', 'December']
    }
    return annual_rainfall, monthly_rainfall

# 3. Model Training
def train_model(df):
    X = df[['District', 'Soil_Type', 'Area', 'Yield']]
    y = df['Crop']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return clf

# 4. Crop Recommendation
def crop_recommendation(user_input, df, clf, label_encoder_crop, label_encoder_district, label_encoder_soil):
    user_input_cleaned = user_input.strip().lower()
    available_districts = [district.lower() for district in label_encoder_district.classes_]

    if user_input_cleaned not in available_districts:
        return f"Error: '{user_input}' is not a valid district. Please try again. Available districts: {', '.join(label_encoder_district.classes_)}"

    district = label_encoder_district.transform([user_input_cleaned])[0]
    soil_type = df[df['District'] == district]['Soil_Type'].iloc[0]
    area = df[df['District'] == district]['Area'].mean()
    yield_value = df[df['District'] == district]['Yield'].mean()

    input_data = pd.DataFrame([[district, soil_type, area, yield_value]], columns=['District', 'Soil_Type', 'Area', 'Yield'])
    prediction = clf.predict(input_data)[0]
    crop_name = label_encoder_crop.inverse_transform([prediction])[0]

    crop_data = df[df['Crop'] == prediction]
    avg_yield = crop_data['Yield'].mean()
    avg_area = crop_data['Area'].mean()
    predominant_soil = label_encoder_soil.inverse_transform([crop_data['Soil_Type'].mode()[0]])[0]
    common_season = crop_data['Season'].mode()[0]

    district_rainfall = df[df['District'] == district].iloc[0]
    annual_rainfall, monthly_rainfall = get_rainfall_data(district_rainfall)

    rainfall_details = {}
    if common_season.lower() == 'rabi':
        rainfall_details = {month: monthly_rainfall[month] for month in ['October', 'November', 'December', 'January', 'February', 'March']}
    elif common_season.lower() == 'kharif':
        rainfall_details = {month: monthly_rainfall[month] for month in ['June', 'July', 'August', 'September']}
    elif common_season.lower() == 'zaid':
        rainfall_details = {month: monthly_rainfall[month] for month in ['March', 'April', 'May']}
    else:
        rainfall_details = monthly_rainfall

    response = (f"We recommend planting {crop_name} in {user_input}.\n"
                f"Average Yield: {avg_yield:.2f} tonnes per hectare\n"
                f"Average Area: {avg_area:.2f} hectares\n"
                f"Predominant Soil Type: {predominant_soil}\n"
                f"Common Season: {common_season}\n"
                f"Annual Rainfall: {annual_rainfall}\n"
                f"Rainfall Details (mm) for {common_season.capitalize()} season:\n")

    for month, rainfall in rainfall_details.items():
        if isinstance(rainfall, str):
            response += f"- {month}: {rainfall}\n"
        else:
            response += f"- {month}: {rainfall:.2f} mm\n"

    return response

# 5. Main Function
def main():
    crop_data_path = "D:/ChatBot/data/India Agriculture Crop Production1.csv"
    rainfall_data_path = "D:/ChatBot/data/MONTHLY RAINFALL-District Level Data (1990-2015).csv"

    df, label_encoder_crop, label_encoder_district, label_encoder_soil = load_data(crop_data_path, rainfall_data_path)
    clf = train_model(df)

    print("Welcome to the Smart Farming Chatbot!")
    print("Please provide the district name for crop recommendations.")
    
    while True:
        user_input = input("Enter District (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Smart Farming Chatbot! Goodbye.")
            break
        result = crop_recommendation(user_input, df, clf, label_encoder_crop, label_encoder_district, label_encoder_soil)
        print(result)

if __name__ == "__main__":
    main()
