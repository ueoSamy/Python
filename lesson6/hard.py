# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, name, color):
        self._name = name
        self._color = color


class AnimalToys(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Животное'


class CartoonToys(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Мульт - персонаж'


class CarToys(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Игрушка-машинка'


class Factory:
    def creating(self, name, color, toy_type, order_count=1):
        self._purchas_materials()
        self._sewing_process()
        self._coloring()
        self._name = name
        self._color = color
        self._toy_type = toy_type
        self._order_count = order_count
        if toy_type == 'Животное':
            return self._completed_toy(), AnimalToys(name, color)
        elif toy_type == 'Мульт - персонаж':
            return self._completed_toy(), CartoonToys(name, color)
        elif toy_type == 'Игрушка-машинка':
            return  self._completed_toy(), CarToys(name, color)

    def _purchas_materials(self):
        print('Закупаем сырья для игрушек ...')

    def _sewing_process(self):
        print('Пошивка игрушек ...')

    def _coloring(self):
        print('Окраска игрушек ...')

    def _completed_toy(self):
        print('----------------------------------')
        print(f'Игрушка готова!\n'
              f'Название: {self._name}\n'
              f'Цвет: {self._color}\n'
              f'Тип игрушки: {self._toy_type}\n'
              f'Количество игрушек: {self._order_count} шт.')
        print('**********************************')


factory = Factory()
toy = factory.creating('Фокси', 'Оранжевый', 'Животное', 3)
toy = factory.creating('Леапольд', 'Бело-Оарнжевый', 'Мульт - персонаж')
toy = factory.creating('Серия BMW', 'Красный', 'Игрушка-машинка', 15)
