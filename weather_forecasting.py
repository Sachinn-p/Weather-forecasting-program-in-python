import requests

def get_weather(api_key, city):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()

    if data['cod'] != '404':
        # Extract relevant information from the API response
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        
        print(f'City: {city}')
        print(f'Weather: {weather_desc}')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
    else:
        print(f'City {city} not found.')

if __name__ == '__main__':
    api_key = ""  # Use the API key here 
    city = input('Enter city name: ')
    get_weather(api_key, city)
