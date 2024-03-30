import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str):
    """
    Функция для переноса указанной строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    """
    # Ввод имени искомого абонента
    print("Введите имя абонента: ", new_file, ": ", end='')
    search_name = input()
    # Отбор абонентов по имени
    tmp_list_name = search_user(source, search_name)
    # Разделение списка по строкам
    tmp_list_name = tmp_list_name.split("\n")
    # Ввод телефона искомого абонента
    print("Введите телефон абонента: ", new_file, ": ", end='')
    search_phone = input()
    # Отбор абонентов по телефону
    tmp_list_phone = search_user(source, search_phone)
    # Разделение списка по строкам
    tmp_list_phone = tmp_list_phone.split("\n")
    # Обработка случая отсутствия совпадений
    if tmp_list_name[0] == 'По указанному значению совпадений не найдено' and tmp_list_phone[0] == 'По указанному значению совпадений не найдено':
        print('Совпадений не найдено')
        return
    rezult = []
    # Поиск одновременного совпадения и имени и телефона
    for i in tmp_list_name:
        if i in tmp_list_phone:
            rezult.append(i)
    # Если есть одновременное совпадение и имени и телефона, то записываем
    # первую строку с таким совпадением в новый файл. (Т.к. необходимо
    # переписать только одну строку)
    if len(rezult) != 0:
        with open(dest, "a", encoding="utf-8") as file:
            new_line = '\n' if read_all(dest) != "" else ''
            file.write(f'{new_line}{rezult[0]}')
    else:
        # Если одновременного совпадения и имени и телефона нет, то в новый
        # файл переписываем первую запись с совпадающим именем, если
        # совпадающих имен меньше чем совпадающих телефонов, и первую
        # запись с совпадением в номере телефона, если совпадений номеров
        # телефона меньше чем совпадений имен
        if len(tmp_list_name) <= len(tmp_list_phone):           
            with open(dest, "a", encoding="utf-8") as file:
                new_line = '\n' if read_all(dest) != "" else ''
                file.write(f'{new_line}{tmp_list_name[0]}')
        else:
            with open(dest, "a", encoding="utf-8") as file:
                new_line = '\n' if read_all(dest) != "" else ''
                file.write(f'{new_line}{tmp_list_phone[0]}')


INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""

file = "number1.txt"

if file not in os.listdir():
    print("указанное имя файла отсутсвует")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file, data))
    elif mode == 4:
        new_file = input("Введите имя файла для перезаписываемых данных: ")
        transfer_data(file, new_file)
        pass
