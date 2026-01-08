from enum import Enum
from resourcetype import ResourceType


class AbilityType(Enum):
    NONE = 0
    DAMAGE = 1
    HEALING = 2
    UTILITY = 3


class Ability:
    def __init__(
        self,
        name,
        resource_type=0,
        gcd=1.5,
        cooldown=0,
        resource_cost=0,
        ability_type=0,
        ability_power=0,
        ignore_armor=False,
    ):
        self.name = name
        self.gcd = gcd
        self.cooldown = cooldown
        self.resource_type = ResourceType(resource_type)
        self.resource_cost = resource_cost
        self.ability_type = AbilityType(ability_type)
        self.ability_power = ability_power
        self.ignore_armor = ignore_armor
