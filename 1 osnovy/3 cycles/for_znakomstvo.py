def solve(boys: list, girls: list):
    result = []  # в эту строку сохраните полученные пары или сообщение "Кто-то может остаться без пары!"
    if len(boys) == len(girls): # проверьте, что длины списков одинаковы
        for boy, girl in zip(sorted(boys), sorted(girls)):  # отсортируйте пары, объедините при помощи zip и распакуйте в цикле
           result.append(f"{boy} и {girl}")
        result = ", ".join(result)
    else:
        result = "Кто-то может остаться без пары!"
    return result


if __name__ == '__main__':
    # Этот код менять не нужно
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")
