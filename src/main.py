import math
import simpy
from abilities import RogueAbility, AbilityType
from player import Player, StatBlock, ResourceType, Weapon
from targetdummy import TargetDummy


class APL:
    def __init__(self):
        self.apl = []

    def add(self, ability):
        self.apl.append(ability)


def main():
    #     ability_list = APL()
    #     ability_list.add(RogueAbility("Sinister Strike", resource_cost=75, ability_type=AbilityType.DAMAGE, ability_power=50))
    #
    #     statblock = StatBlock(100, 30, 30, 30, 30)
    #     weapon = Weapon(5, 10, 2.4)
    #     player = Player(statblock, weapon, ResourceType.ENERGY, resource_amount=100, ability_list=ability_list)
    #     target = TargetDummy(1000, 30)
    #     calculate_total_damage_over_period(player, target, 5 * 60)
    env = simpy.Environment()
    env.process(wrapper(env, 5 * 60))
    env.run(5 * 60 + 1)


def wrapper(env, run_length):
    result = yield env.process(basic_sim(env, run_length))
    print(f"Total damage: {result}")
    print(f"DPS: {float(result / (5 * 60))}")


def calculate_total_damage_over_period(player, target, total_time_in_seconds):
    damage_instance = player.do_damage(
        target,
    )
    total_damage = damage_instance * math.floor(
        (total_time_in_seconds / player.attack_speed)
    )
    print(f"player did {total_damage} over {total_time_in_seconds} seconds")


def basic_sim(env, run_length):
    ability_list = APL()
    ability_list.add(
        RogueAbility(
            "Sinister Strike",
            resource_cost=75,
            ability_type=AbilityType.DAMAGE,
            ability_power=50,
        )
    )

    statblock = StatBlock(100, 30, 30, 30, 30)
    weapon = Weapon(5, 10, 2.4)
    player = Player(
        statblock,
        weapon,
        ResourceType.ENERGY,
        resource_amount=100,
        ability_list=ability_list,
    )
    target = TargetDummy(1000, 30)
    total_damage = 0
    print("Running simulation...")
    while True:
        if player.current_resource < player.max_resource:
            player.current_resource += 1
            yield env.timeout(0.1)

        if player.current_resource >= 75:
            total_damage += player.do_damage(
                target, ability_list.apl[0]
            )  # cast sinister strike
            yield env.timeout(ability_list.apl[0].gcd)
        else:
            total_damage += player.do_damage(target, ability_list.apl[1])  # cast attack
            yield env.timeout(ability_list.apl[1].gcd)
        if env.now >= run_length:
            break
    return total_damage


if __name__ == "__main__":
    main()
