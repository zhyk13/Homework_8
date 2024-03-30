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


def transfer_data(source: str, dest: str, num_row: int):
    """
    Функция для переноса указанной строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """
# Открываем для чтения исходный файл
    with open(source, "r", encoding="utf-8") as file:
        # Содержимое исходного файла построчно записываем в список list_1
        list_1 = file.read().split("\n")
# Проверка на наличие искомой строки
    if len(list_1) < num_row:
        print('Такой строки не существует')
        return
# Открываем/создаем файл для перезаписи
    with open(dest, "a", encoding="utf-8") as file:
        # Проверка на наличие содержимого в файле для перезаписи
        new_line = '\n' if read_all(dest) != "" else ''
# Записываем искомую строку в файл для перезаписи
        file.write(f'{new_line}{list_1[num_row-1]}')


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
        print("Введите номер строки для перезаписи ", new_file, ": ", end='')
        num = int(input())
        transfer_data(file, new_file, num)
        pass
