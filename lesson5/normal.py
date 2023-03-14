# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from easy import make_dir, rm_dir, list_dir
import os


def change_dir(folder):
    try:
        os.chdir(folder)
        print('Успешно перешел в папку')
    except FileNotFoundError:  # если директория не найдена
        print('Переход в заданную папку невозможен, ее не существует!')


# создали словарь, и передаем в качестве value(значение) наши функции, в дальнейшем чтобы вызвать по ключу
do = {
    1: change_dir,
    2: list_dir,
    3: rm_dir,
    4: make_dir
}

while True:
    choice = input('Выберите один из пунктов меню:\n'
                   '***************************************\n'
                   '1. Перейти в папку\n'
                   '2. Просмотреть содержимое текущей папки\n'
                   '3. Удалить папку\n'
                   '4. Создавть папку\n'
                   '5. Выход\n\n')

    try:
        if len(choice.split()) == 2:  # Если передан более 1 пользовательских аргумента
            choice, folder_name = choice.split()
            choice = int(choice)  # преоброзовали выбор в int, потому что у нас key является int
            if do.get(choice):  # передаем в качестве ключа choice
                do.get(choice)(folder_name)
        else:  # Если передан 1 пользовательский аргумент
            choice = int(choice)
            if choice == 5:
                break
            elif do.get(choice):
                print(do.get(choice)())
    except ValueError:  # в случае если пользователь ввел не те данные, не понятные символы
        print('Ошибка! Неверные данные!\n')
    except TypeError:  # если пользователь забыл указать назв. папки
        print('Ошибка! Вы не указали имя папки!\n')