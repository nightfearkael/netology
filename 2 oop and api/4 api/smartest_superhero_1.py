import requests

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    # ваш код здесь
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    list_heroes = ['Hulk', 'Captain America', 'Thanos']

    response = requests.get(url + '/all.json')
    intelligence = 0
    for hero in response.json():
        if hero.get('name') in list_heroes and hero['powerstats']['intelligence'] > intelligence:
            the_smartest_superhero = hero.get('name')
            intelligence = hero['powerstats']['intelligence']

    return the_smartest_superhero


if __name__ == '__main__':
    print(get_the_smartest_superhero())
