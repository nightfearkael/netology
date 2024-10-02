import json


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм
    with open(file_path, encoding='utf-8') as new_file:
        data = json.load(new_file)
    data_list = data['rss']['channel']['items']

    word_list = []
    for list in data_list:
        word_list += [elem for elem in list['description'].split(' ') if len(elem) > word_max_len]

    word_counter = {}
    for word in set(word_list):
        word_counter.update({word: word_list.count(word)})

    return sorted(word_counter, key=word_counter.get, reverse=True)[:top_words_amt]


if __name__ == '__main__':
    print(read_json('newsafr.json'))

