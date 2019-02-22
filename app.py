from url_requests import *
from measurement import *

# pokazuje temperaturę, ciśnienie i zachmurzenie w mieście


def city_temp(city):
    data = city_weather(city)
    main = data['main']
    return '\nAktualna temperatura w {} to {}°C, ciśnienie: {} hPa, zachmurzenie: {}%'.format(city, main['temp'], main['pressure'], main['humidity'], key=KEY)
    return ['temp']


def rectangle_temp(city):
    data = rectangle_weather(city)
    dict = data['list']
    dict = {v['name']: v['main']['temp'] for v in data['list']}
    ma = ''.join([max(dict.items(), key=operator.itemgetter(1))[0]])
    mi = ''.join([min(dict.items(), key=operator.itemgetter(1))[0]])
    if city in dict:
        print(f'W {city} jest {dict[city]}°C\n')
    else:
        print(city_temp(city) + '\n')
    return f'Najcieplejsze miejsce w okolicy to {ma}: {dict[ma]}°C, a najzimniej jest w {mi}: {dict[mi]}°C'


def ask_for_temp():
    city = input('What city do you want to check?\n')
    return city_temp(city)


def ask_for_ractangle():
    city = input('Gdzie jesteś?\n\n>>> ')
    return rectangle_temp(city)


if __name__ == '__main__':
    main()
