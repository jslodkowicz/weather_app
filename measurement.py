from url_requests import *
import operator

# oblicza położenie geograficzne miasta


def city_coord(city):
    coord = city_weather(city)['coord']
    return coord

# oblicza pogodę w miastach w promieniu x minut geograficznych


def rectangle_weather(city, x=1):
    coord = city_coord(city)
    rectangle = (
        coord['lon'] - x, coord['lat'] - x,
        coord['lon'] + x, coord['lat'] + x,
    )
    data = rectangle_zone(rectangle)
    return data

# zwraca miasto z najniższą temperaturą w promieniu funkcji rectangle temp


def rectangle_min_temp(city):
    data = rectangle_weather(city)
    dict = {v['name']: v['main']['temp'] for v in data['list']}
    mi = ''.join([min(dict.items(), key=operator.itemgetter(1))[0]])
    return mi, dict[mi]

# zwraca miasto z najniższą temperaturą w promieniu funkcji rectangle temp


def rectangle_max_temp(city):
    data = rectangle_weather(city)
    dict = {v['name']: v['main']['temp'] for v in data['list']}
    ma = ''.join([max(dict.items(), key=operator.itemgetter(1))[0]])
    return ma, dict[ma]


if __name__ == '__main__':
    main()
