import requests
from dataclasses import dataclass
API_key="b50218dc7151446f2598e62ffd438786"

@dataclass
class weatherModel():
    main:str
    description:str
    icon:str
    temperature:int

def get_weather_data(city_name,state_code,country_code):
    lat,lon = get_lat_lon_data(city_name,state_code,country_code)
    data=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    weather = weatherModel( main = data.get('weather')[0].get('main'),
                           description=data.get('weather')[0].get('description'),
                           icon=data.get('weather')[0].get('icon'),
                           temperature=int (data.get('main').get('temp'))
                           )
    return weather

def get_lat_lon_data(city_name,state_code,country_code):
    datas = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    return datas[0].get('lat'),datas[0].get('lon')
    
def main(city_name,state_code,country_code):
    weather_data = get_weather_data(city_name,state_code,country_code)
    return weather_data

print(main('Toronto','ON','CA'))

