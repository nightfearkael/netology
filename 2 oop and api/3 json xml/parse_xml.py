import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    items = root.findall('channel/item')

    word_list = []
    for item in items:
        word_list += [elem for elem in item.find('description').text.split(' ') if len(elem) > word_max_len]

    word_counter = {}
    for word in set(word_list):
        word_counter.update({word: word_list.count(word)})

    return sorted(word_counter, key=word_counter.get, reverse=True)[:top_words_amt]

if __name__ == '__main__':
    print(read_xml('newsafr.xml'))

