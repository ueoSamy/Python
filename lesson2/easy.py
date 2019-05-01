# region Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'банан', 'киви', 'арбуз']
right_side = len(max(fruits, key=len))

for item in fruits:  # с методом .fromat() - первый способ
    print("{}. {:>{}}".format(fruits.index(item) + 1, item, right_side))

maxelem = len(max(fruits, key=len))  # тут определим самцю длинную слову

for item in fruits:  # с методом .fromat() - второй способ
    print("{}. {}".format(fruits.index(item) + 1, item.rjust(maxelem, ' ')))
# endregion


# region Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_a = [2, 3, 4, 5, 6, 7, 8, 9]
list_b = [1, 2, 3, 4, 5, 6, 7, 8]

for item in list_b:
    if item in list_a:
        list_a.remove(item)
print(list_a)
# endregion

# region Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list_one = [12, 9, 8, 32, 65, 14, 76, 25, 66, 18, 8]
list_two = []
for number in list_one:
    if number % 2:
        number = number / 4
        list_two.append(number)
    else:
        number = number * 2
        list_two.append(number)

print(list_two)
# endregion
