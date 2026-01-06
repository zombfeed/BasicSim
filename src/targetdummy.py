import math


class TargetDummy:
    def __init__(self, health, armor):
        self.__armor = armor
        self.__max_health = health
        self.current_health = health

    def set_health(self, health):
        self.__max_health = health

    def set_armor(self, armor):
        self.__armor = armor

    def get_health(self):
        return self.__max_health

    def get_armor(self):
        return self.__armor

    def take_damage(self, damage, ignore_armor=False):
        if ignore_armor:
            self.current_health -= damage
            return damage
        else:
            result_damage = math.floor(damage - damage * (self.get_armor() / 100))
            self.current_health -= result_damage
            return result_damage
