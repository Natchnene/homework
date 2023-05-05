# Написать функцию, которая принимает список словарей, где каждый словарь представляет собой
# запись об ученике (с ключами 'имя', 'возраст', 'оценки'), и возвращает список словарей,
# отсортированный по возрасту учеников в порядке убывания.


def custom_sort(array: list) -> list:
    array.sort(key=lambda x: x['Age'])
    return array

print(custom_sort([{'Name': 'Petia', 'Age': 14, 'Grades': 8}, {'Name': 'Kolia', 'Age': 12, 'Grades': 7}]))