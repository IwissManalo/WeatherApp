import requests

# Replace with your own API key
API_KEY = '5ae567950cb249f28d915424240502'

def current_weather(request, city_name='Makati'):
    
    payload = {
        'key': API_KEY,
        'q': city_name,
    }
    response = requests.get('http://api.weatherapi.com/v1/current.json', params=payload)
    
    print(response.status_code)
    print(response.url)
    
    
    return response.json()

def forecast_weather(request, city_name='Makati'):
    payload = {
        'key': API_KEY,
        'q': city_name,
        'days': 3,
    }
    response = requests.get('http://api.weatherapi.com/v1/forecast.json', params=payload)
    print(response.status_code)
    print(response.url)
    return response.json()

    