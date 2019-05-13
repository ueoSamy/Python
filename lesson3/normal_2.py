# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

list_names = ['Вася', 'Антон', 'Алиса', 'Дима', 'Марина']
list_salary = ['12500', '13000', '12000', '15000', '14500']
right_side = len(max(list_names, key=len))

with open('salary.txt', mode='w', encoding='utf-8') as file:
    for i, j in zip(list_names, list_salary):
        file.writelines("{}. {:<{}}".format(list_names.index(i) + 1, i, right_side) + ' - ' + j + '\n')
# считываем строки из файла
with open('salary.txt', mode='r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)

# как выглядят строки внутри файла
with open('salary.txt', mode='r+', encoding='utf-8') as file:
    for line in file:
        print(line)

with open('salary.txt', mode='r+', encoding='utf-8') as file:
    for line in file:
        ind, names, symb, salary = line.split()
        salary = int(salary)
        salary_tax = salary * 0.87
        if salary >= 13000:
            print('{}. {:<{}} {} {}, -13% - {}'.format(ind, names.upper(), right_side, symb, salary, salary_tax))