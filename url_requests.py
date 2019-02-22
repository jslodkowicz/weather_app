import requests

API_URL = 'http://api.openweathermap.org/data/2.5/'
KEY = '88e58e33732c69a0d4687d8d2c09caf7'

CITY_URL = API_URL + 'weather?q={city_name}&APPID={key}&units=metric'
CIRCLE_URL = API_URL + 'find?lat={}&lon={}&cnt=10&APPID={key}'
RECTANGLE_ZONE_URL = API_URL + 'box/city?bbox={},{},{},{},{}&APPID={key}'

# zwraca aktualną pogodę we wskazanym mieście


def city_weather(city):
    data = requests.get(CITY_URL.format(city_name=city, key=KEY))
    return data.json()

# zwraca pogodę w 10 najbliższych miastach


def city_circle(coords):
    data = requests.get(CIRCLE_URL.format(*coords, key=KEY))
    return data.json()

# zwraca pogodę w miastach w określonym promieniu


def rectangle_zone(coords):
    data = requests.get(RECTANGLE_ZONE_URL.format(
        *coords, 10, key=KEY))
    return data.json()


if __name__ == '__main__':
    print(city_circle((14, 53)))
