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
        resource_type,
        gcd=1.5,
        cooldown=0,
        resource_cost=0,
        ability_type=AbilityType.NONE,
    ):
        self.name = name
        self.gcd = gcd
        self.cooldown = cooldown
        self.resource_type = resource_type
        self.resource_cost = resource_cost
        self.ability_type = ability_type


class RogueAbility(Ability):
    def __init__(
        self,
        name,
        gcd=1,
        cooldown=0,
        resource_cost=0,
        ability_type=AbilityType.NONE,
        ability_power=0,
        ignore_armor=False,
    ):
        super().__init__(
            name, ResourceType.ENERGY, gcd, cooldown, resource_cost, ability_type
        )
        self.power = ability_power
        self.ignore_armor = ignore_armor
