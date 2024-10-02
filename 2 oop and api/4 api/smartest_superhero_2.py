import requests


def get_the_smartest_superhero(superheros):
    the_smartest_superhero = ''
    # ваш код здесь
    intelligence = 0
    for id in superheros:
        response = requests.get(f'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/{id}.json')
        hero = response.json()
        if hero['powerstats']['intelligence'] > intelligence:
            intelligence = hero['powerstats']['intelligence']
            the_smartest_superhero = hero['name']

    return the_smartest_superhero


if __name__ == 'main':
    assert get_the_smartest_superhero([332, 149, 655]) == 'Thanos'
