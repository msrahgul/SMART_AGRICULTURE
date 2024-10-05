import requests

def get_weather_data(location):
    api_key = 'your_openweather_api_key'  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
        }
        return weather_data
    else:
        raise ValueError(f"Error fetching weather data: {data.get('message', 'Unknown error')}")
