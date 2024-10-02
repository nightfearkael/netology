courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

# Добавьте в список всех преподавателей со всех курсов
all_list = []
for m in mentors:
    all_list += m
# Допишите здесь ваш код, который заполнит all_list. Можете как складывать списки, так и использовать метод extend
# Сделайте список all_names_list, состоящий только из имён, и заполните его
all_names_list = []
for mentor in all_list:
    name = mentor.split(' ')[0]
    all_names_list.append(name)

# Сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
unique_names = set(all_names_list)

# Теперь необходимо отсортировать имена в алфавитном порядке. Подсказка: используйте sorted() для списка
# Допишите код ниже
all_names_sorted = sorted(list(unique_names))
# Допишите конструкцию вывода результата. Используйте string.join()
# Результат будет в all_names_sorted
print(f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}')


# Уникальные имена будут в unique_names
unique_names = all_names_sorted

# Подсчитайте встречаемость каждого имени через list.count()
popular = []
for name in unique_names:
    popular.append([name, all_names_list.count(name)]) # Добавьте подсчёт имён

# Это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
# Используйте его, как есть, или напишите собственный :)
popular.sort(key=lambda x:x[1], reverse=True)

# Получите топ-3 часто встречающихся имён из списка popular
# Подсказка: возьмите срез списка
top_3 = popular[0:3]
for mentor in top_3:
    top_3[top_3.index(mentor)] = f"{mentor[0]}: {mentor[1]} раз(а)"
print(', '.join(top_3))


