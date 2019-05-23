# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

# region Класс GamePerson


class GamePerson:
    def __init__(self, name, health=100, damage=8, armor=0, has_armor=False):
        self.name = name
        self._health = health
        self._damage = damage
        self._armor = armor
        self.has_armor = has_armor

    def get_health(self):
        return self._health  # получили здоровье

    def get_damage(self):
        return self._damage  # получили урон

    def is_armor_on_player(self, value):  # проверка есть ли бронья у персонажа
        if self.has_armor:
            self._armor = value
            print('Броня надета')
            print('Защита {}'.format(value))

    def protect(self, enemy_damage):  # защита брони если оно имеется
        if self.is_armor_on_player():
            return enemy_damage / self._armor

    def _set_health(self, value):  # присваиваем остаток здоровье
        self._health = value

    def getting_damage(self, enemy_damage):  # получение урона
        self._set_health(self._health - enemy_damage)

    def strike(self, damage):  # нанесение урона
        self._set_health(self._health - damage)

    def calc_damage(self, enemy):  # подсчет урона
        if enemy.is_armor_on_player(self._armor):
            return self._damage / enemy.protect()
        else:
            return enemy.get_health() - self._damage

    def attack(self, enemy):  # атака соперника
        damage = self.calc_damage(enemy)
        enemy.strike(damage)


# endregion

# region Player
class Player(GamePerson):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


# endregion


# region Enemy


class Enemy(GamePerson):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


# endregion

class StartGame:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_game(self):
        last_attacker = self.player
        while self.player.get_health() > 0 and self.enemy.get_health() > 0:
            if last_attacker == self.player:
                self.enemy.attack(self.player)
                last_attacker = self.enemy
            else:
                self.player.attack(self.enemy)
                last_attacker = self.player
        if self.player.get_health() > 0:
            print('Победил игрок {}'.format(self.player))
        else:
            print('Победил враг {}'.format(self.enemy))


player = Player('Альянс', 100, 8, 100)
enemy = Enemy('Орда', 100, 7, 100)
game = StartGame(player, enemy)
game.start_game()
