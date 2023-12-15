import requests

def get_weather(api_key, city):
    base_url = 'https://api.weatherbit.io/v2.0/current'

    params = {
        'key': api_key,
        'city': city,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data['data'][0]['city_name']
        country = data['data'][0]['country_code']
        description = data['data'][0]['weather']['description']
        temperature = data['data'][0]['temp']

        weather_info = f"Weather in {city_name},{country}:{description}.{temperature}°C."
        return weather_info
    else:
        return "Failed to retrieve weather data."
