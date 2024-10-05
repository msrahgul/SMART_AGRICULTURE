# rainfall_data.py

rainfall_data = {
    "madurai": {
        "January": 16.20,
        "February": 6.10,
        "March": 7.00,
        "April": 39.60,
        "May": 16.20,
        "June": 65.90,
        "July": 34.20,
        "August": 198.90,
        "September": 219.00,
        "October": 241.70,
        "November": 136.10,
        "December": 99.30
    },
    # You can add more districts and their rainfall data here
}

def display_rainfall_data(district):
    if district in rainfall_data:
        print(f"Rainfall Details (mm) for Whole year season:")
        for month, rainfall in rainfall_data[district].items():
            print(f"- {month}: {rainfall} mm")
    else:
        print("Rainfall data not found for the selected district.")
