# region Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


# class TownCar:
#     def __init__(self, company, year_of_issue, name, color, speed, is_police=False):
#         self._company = company
#         self._year_of_issue = year_of_issue
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print(f'Машина {self.name} поехала!')
#
#     def stop(self):
#         print(f'Машина {self.name} остановилась')
#
#     def turn(self, direction):
#         print(f'Машина {self.name} повернулась к {direction}')
#
#
# class SportCar:
#     def __init__(self, company, year_of_issue, name, color, speed, is_police=False):
#         self._company = company
#         self._year_of_issue = year_of_issue
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print(f'Машина {self.name} поехала!')
#
#     def stop(self):
#         print(f'Машина {self.name} остановилась')
#
#     def turn(self, name, direction):
#         print(f'Машина {self.name} повернулась к {direction}')
#
#
# class WorkCar:
#     def __init__(self, company, year_of_issue, name, color, speed, is_police=False):
#         self._company = company
#         self._year_of_issue = year_of_issue
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print(f'Машина {self.name} поехала!')
#
#     def stop(self):
#         print(f'Машина {self.name} остановилась')
#
#     def turn(self, direction):
#         print(f'Машина {self.name} повернулась к {direction}')
#
#
# class PoliceCar:
#     def __init__(self, company, year_of_issue, name, color, speed, is_police=True):
#         self._company = company
#         self._year_of_issue = year_of_issue
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self, name):
#         print(f'Машина {name} поехала!')
#
#     def stop(self, name):
#         print(f'Машина {name} остановилась')
#
#     def turn(self, name, direction):
#         print(f'Машина {name} повернулась к {direction}')
# endregion

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, company, year_of_issue, name, color, speed, is_police=False, typ_car='Городской автомобиль'):
        self._company = company
        self._year_of_issue = year_of_issue
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police
        self._type_car = typ_car

    def go(self):
        print(f'Машина {self._name} поехала!')

    def stop(self):
        print(f'Машина {self._name} остановилась')

    def turn(self, direction):
        print(f'Машина {self._name} повернулась к {direction}')


class TownCar(Car):
    pass


class SportCar(Car):
    def __init__(self, company, year_of_issue, name, color, speed, type_car='Гоничный автомобиль'):
        super().__init__(company, year_of_issue, name, color, speed)
        self._type_car = type_car

    def nitro_enable(self, turn_on_off=False):
        self._turn_on_off = turn_on_off
        print('Нитро включено')

    def sport_speed(self):
        if self.nitro_enable():
            self._speed = self._speed * 10
            print('Скорость увеличена на 10 раз!')


class WorkCar(Car):
    def __init__(self, company, year_of_issue, name, color, speed, type_car='Рабочий автомобиль'):
        super().__init__(company, year_of_issue, name, color, speed)
        self._type_car = type_car


class PoliceCar(Car):
    def __init__(self, company, year_of_issue, name, color, speed, type_car='Полицейский автомобиль'):
        super().__init__(company, year_of_issue, name, color, speed)
        self.is_police = True
        self._type_car = type_car

    def run_mode(self):
        self._speed *= 10
        self.flasher(True)
        print('Скорость увеличена на 10 раз!\nРежим погони')

    def flasher(self, function_on=False):
        self._function_on = function_on
        print('Полицейская мигалка включена')


tcar = TownCar('BMW', 2010, 'X5', 'Черный', 200)
tcar.go()
tcar.turn('городу Мексика')
tcar.stop()
print('*************************')
scar = SportCar('Ferrari', 2010, 'Ferrari Mondial', 'Белый', 320)
scar.go()
scar.nitro_enable(True)
print('*************************')
wcar = WorkCar('Кмаз', 2007, 'Камаз 5320', 'Черно-синий', 120)
wcar.go()
wcar.turn('Заводу')
wcar.stop()
print('*************************')
pcar = PoliceCar('Mercedes', 2006, 'Mercedes-Benz SL-Clas', 'Синий', 300)
pcar.go()
pcar.turn('месту преступление')
pcar.run_mode()
