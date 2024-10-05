import random

def get_sensor_data():
    # Simulate fetching data from IoT sensors
    sensor_data = {
        'soil_moisture': random.uniform(0.1, 1.0),  # Example: 0.1 (dry) to 1.0 (wet)
        'soil_temperature': random.uniform(15, 35)  # Example: 15°C to 35°C (can be ignored if not needed)
    }
    return sensor_data
