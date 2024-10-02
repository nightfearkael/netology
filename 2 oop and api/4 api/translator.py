import requests

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20240729T112125Z.06f9f87715e55dda.e13f60f09466c9f3593e02af03a7b7d20c86842f'


def translate_word(word):
    # ваш код здесь
    params = {'key': token, 'lang': 'ru-en', 'text': word}
    response = requests.get(url, params=params)
    word_json = response.json()
    trans_word = word_json['def'][0]['tr'][0]['text']
    return trans_word


if __name__ == '__main__':
    word = 'машина'
    assert translate_word(word) == 'car'
