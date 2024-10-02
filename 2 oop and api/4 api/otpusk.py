import time

import requests


def find_uk_city(coordinates:list) -> str:
    """Ваш код здесь"""
    cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    key = '66a77e3380e2f783064523rmkc62ae0'
    url = 'https://geocode.maps.co/reverse'

    for lat, lon in coordinates:
        params = {'lat': lat, 'lon': lon, 'api_key': key}
        response = requests.get(url, params=params)
        data = response.json()
        city = data['address']['city']
        if city in cities:
            return city


if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'


