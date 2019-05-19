# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys

print('sys.argv = ', sys.argv)


def print_help():  # меню подсказки, help
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.mkdir(dir_name)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:  # проверка не создано ли тек. директория ранее
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")  # проверка ping pong хаха :D


def cp(filename):
    with open(filename, 'rb') as f:  # Я не стал с легким путьем так скажем с shutil идти.
        with open('copy_' + filename, 'wb') as destination_f:  # так же открываем файл копируем содержимое
            destination_f.write(f.read())  # создаем другой файл и кладем туда нашу копию
# работа с файлом в бинарном режиме в случае попадется нам не текстовый файл


def rm(filename):
    result = input('Вы уверены? y/n:')  # чтобы случайно не удалили нужный нам файл.
    # Проверка правильный ли файл мы удаляем
    if result == 'y':
        try:
            os.remove(filename)
        except FileNotFoundError:
            print('Файл для удаления не найден.')
        except PermissionError:
            print('В доступе было отказано!')
            os.rmdir(filename)
            print('Но мы все равно удалили! :)')


def ls():
    print(os.getcwd())


def cd(path):
    try:
        os.chdir(path)
        print('Успешно перешли в указанную папку')
    except FileNotFoundError:
        print('Невозможно перейти в директорию, ее не существует!')


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        if key == 'cd' or key == 'cp' or key == 'rm':  # если к ключу переданы cd, cp, rm тогда передать имя директории
            do[key](dir_name)
        else:
            do[key]()  # иначе остальным ключам аргументы не требуются
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
