import requests, json, time
from datetime import datetime

TOKEN = '5880392407:AAEoROv6_KqRzT7XKGSFb40cNDzRVAxV8L4'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def get_temperature():
    weather_api_key = '46a79520f7d3d770c0900eb851944070'
    city = 'Delhi/NCR'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    temperature = data['main']['temp']
    return temperature

def send_temperature():
    temperature = get_temperature()
    chat_id = '1042166601'
    message = f'The current temperature in Delhi is {temperature} degrees Celsius'
    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, json=data)
    print(response.json())

while True:
    send_temperature()
    time.sleep(3600)