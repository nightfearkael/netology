from typing import List


def fio(initials: List[str]) -> str:
    sting = initials[0][0]+initials[1][0]+initials[2][0]
    return sting


if __name__ == '__main__':
    assert fio(['Иванов', 'Иван', 'Иванович']) == 'ИИИ'
    assert fio(['Жан', 'Клот', 'Вандамович']) == 'ЖКВ'
    assert fio(['Павлов', 'Иван', 'Уралович']) == 'ПИУ'
    assert fio(['Семейный', 'Доминик', 'Торретович']) == 'СДТ'
    print("\nОтличная работа, отправляйте на проверку!")
