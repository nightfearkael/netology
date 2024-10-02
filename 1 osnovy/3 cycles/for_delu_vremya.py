def solve(todo_list: list, workday: float = 8):
    worktime = 0.0
    for todo in todo_list: # посчитайте в цикле сумму рабочего времени и сохраните в переменную worktime
        worktime += todo[1]
    return workday - worktime


if __name__ == '__main__':
    # Этот код менять не нужно
    todo_list = [
        ["Разобрать почту", 1],
        ["Обзвонить клиентов", 2],
        ["Запланировать дела на завтра", 0.6],
        ["Сделать презентацию", 3],
        ["Созвон с командой", 0.5]
    ]
    result = solve(todo_list)
    result = round(result, 1)
    assert result == 0.9, f"Время рассчитано неверно: {result}"
    print(f"Время на отдых: {result}")