import requests

api_key='df854455033b01454445d208766e502c'

base_url='https://api.openweathermap.org/data/2.5/weather?q='

city=input('Wpisz nazwe miasta: ')

complete_url= base_url + city +"&appid="+ api_key + '&lang=PT&units=metric'

response=requests.get(complete_url)

data=response.json()
print("Temperatura: ", data['main']['temp'])
print("Cisnienie: ", data['main']['pressure'])
print("Predkosc wiatru: ", data['wind']['speed'])