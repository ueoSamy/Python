# region Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys


def make_dir(path):
    try:
        os.mkdir(path)
        print('Директория создана успешно')
    except FileExistsError:
        print('Директория уже существует')


def rm_dir(path):
    try:
        os.removedirs(path)
        print('Директория успешно удалена')
    except FileNotFoundError:
        print('Директория для удаления не найдена.')


# endregion

# region Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    print([i for i in os.listdir() if os.path.isdir(i)])  # проверка является ли папкой и потом отображать


# endregion


# region Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def create_file_copy():
    file_name = sys.argv[0]

    with open(file_name, 'rb') as f:
        name, extension = file_name.split('.')  # разделяем имя файла наименование.расширения
        with open(name + '_copy.' + extension, 'wb') as destination_f:  # создаем файл,
            # и туда кладем копия содержимого из файла f
            destination_f.write(f.read())


# endregion

# чтобы создание несколько папок сработал если только запустим с easy скрипт
# при импорте чтобы не сработала
if __name__ == "__main__":
    dir_path = 'dir_{}'
    [make_dir(dir_path.format(i)) for i in range(1, 10)]
    [rm_dir(dir_path.format(i)) for i in range(1, 10)]

    list_dir()