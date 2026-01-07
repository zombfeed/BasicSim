import math
from resourcetype import ResourceType


class StatBlock:
    """
    everything but primary should be percentages
    """

    def __init__(self, primary, versatility, mastery, critical_strike, haste):
        self.primary = primary
        self.versatility = versatility
        self.mastery = mastery
        self.critical_strike = critical_strike
        self.haste = haste


class Weapon:
    def __init__(self, min_damage=0, max_damage=0, attack_speed=0.0):
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.attack_speed = attack_speed


class Player:
    def __init__(
        self,
        stat_block,
        weapon,
        resource_type=ResourceType.NONE,
        resource_amount=0,
        ability_list={},
    ):
        self.stats = stat_block
        self.weapon = weapon
        self.resource_type = resource_type
        self.current_resource = resource_amount
        self.max_resource = resource_amount
        self.ability_list = ability_list

    def cast(self, ability):
        raise NotImplementedError

    def do_damage(self, target, ability):
        multipliers = 1 + self.stats.versatility / 100
        min_damage = (
            (ability.power * self.weapon.min_damage + (self.stats.primary / 3.5))
            * self.weapon.attack_speed
        ) * multipliers
        max_damage = (
            (ability.power * self.weapon.max_damage + (self.stats.primary / 3.5))
            * self.weapon.attack_speed
        ) * multipliers

        damage = math.floor((min_damage + max_damage))
        return target.take_damage(damage, ability.ignore_armor)

    # def do_damage(self, target, ignore_armor=False):
    #     multipliers = 1 + self.stats.versatility / 100
    #     min_damage = (
    #         self.weapon.min_damage + ((self.stats.primary / 3.5) * self.weapon.attack_speed)
    #     ) * multipliers
    #     max_damage = (
    #         self.weapon.max_damage + ((self.stats.primary / 3.5) * self.weapon.attack_speed)
    #     ) * multipliers
    #     damage = math.floor((min_damage + max_damage) / 2)
    #     return target.take_damage(damage, ignore_armor)
