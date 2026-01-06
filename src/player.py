import math


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


class Player:
    def __init__(self, stat_block, min_damage=0, max_damage=0, attack_speed=0.0):
        self.stats = stat_block
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.attack_speed = attack_speed

    def do_damage(self, target, ignore_armor=False):
        multipliers = 1 + self.stats.versatility / 100
        min_damage = (
            self.min_damage + ((self.stats.primary / 3.5) * self.attack_speed)
        ) * multipliers
        max_damage = (
            self.max_damage + ((self.stats.primary / 3.5) * self.attack_speed)
        ) * multipliers
        damage = math.floor((min_damage + max_damage) / 2)
        return target.take_damage(damage, ignore_armor)
