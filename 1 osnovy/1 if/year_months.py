
def check_month(month: int):
    if month == 12 or month == 1 or month == 2:
        return 'Зима'
    elif month == 3 or month == 4 or month == 5:
        return 'Весна'
    elif month == 6 or month == 7 or month == 8:
        return 'Лето'
    elif month == 9 or month == 10 or month == 11:
        return 'Осень'
    else:
        return 'Некорректный номер месяца'


def check_month2(month: int):
    if month in [1, 2, 12]:
        return 'Зима'
    elif month in [3, 4, 5]:
        return 'Весна'
    elif month in [6, 7, 8]:
        return 'Лето'
    elif month in [9, 10, 11]:
        return 'Осень'
    else:
        return 'Некорректный номер месяца'


def check_month3(month: int):
    """Напишите ваш код здесь"""
    match month:
        case 12 | 1 | 2:
            return 'Зима'
        case 3 | 4 | 5:
            return 'Весна'
        case 6 | 7 | 8:
            return 'Лето'
        case 9 | 10 | 11:
            return 'Осень'
        case _:
            return 'Некорректный номер месяца'


if __name__ == '__main__':
    # Этот код менять не надо
    season = check_month(1)
    assert season == 'Зима', "Ответ должен быть Зима"
    print(f"1 месяц время года: {season}")
    season = check_month(4)
    assert season == 'Весна', "Ответ должен быть Весна"
    print(f"4 месяц время года: {season}")
    season = check_month(18)
    assert season == "Некорректный номер месяца", "Ответ должен быть 'Некорректный номер месяца'"
    print(f"18 месяц: {season}")