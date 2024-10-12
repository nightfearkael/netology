def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    return b ** 2 - 4 * a * c


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        print('корней нет')
    elif discriminant(a, b, c) == 0:
        x = -b / (2 * a)
        print(x)
    else:
        x_1 = (-b + discriminant(a, b, c) ** 0.5) / 2 * a
        x_2 = (-b - discriminant(a, b, c) ** 0.5) / 2 * a
        print(x_1, x_2)


if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)
