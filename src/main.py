import os
import sys
import simpy
from actions import ActionPriorityList as APL
from APLParser import parse_actions_file
from player import Player, StatBlock, Weapon
from targetdummy import TargetDummy


actions_file = os.path.join("./resources", "test_apl.actions")

rogue_file = os.path.join("./resources", "rogue_actions.json")


def main():
    actions_filepath = sys.argv[1]
    if not os.path.isfile(actions_filepath):
        raise Exception(f"Error: could not find {actions_filepath}")
    if os.path.splitext(actions_filepath)[1] != ".actions":
        raise Exception(
            f'Error: {actions_filepath} is not a valid file (program requires a ".actions" file'
        )
    env = simpy.Environment()
    env.process(wrapper(env, actions_filepath, 5 * 60))
    env.run(5 * 60 + 1)


def wrapper(env, actions_filepath, run_length):
    result = yield env.process(basic_sim(env, actions_filepath, run_length))
    print(f"Total damage: {result}")
    print(f"DPS: {float(result / (5 * 60))}")


def build_player(apl_file_path):
    actions = parse_actions_file(apl_file_path)
    apl = APL()
    apl.build_list(actions)
    stat_block = StatBlock(100, 30, 30, 30, 30)
    weapon = Weapon(5, 10, 2.4)
    player = Player(
        stat_block, weapon, 1, resource_amount=100, ability_list=apl.actions
    )
    return player


def basic_sim(env, actions_filepath, run_length):
    target = TargetDummy(1000, 30)
    player = build_player(actions_filepath)
    total_damage = 0
    print("Running simulation...")
    while True:
        if player.current_resource < player.max_resource:
            player.current_resource += 1
            yield env.timeout(0.1)

        if player.current_resource >= 75:
            total_damage += player.do_damage(
                target, player.ability_list[0]
            )  # cast sinister strike
            yield env.timeout(player.ability_list[0].gcd)
        else:
            total_damage += player.do_damage(
                target, player.ability_list[1]
            )  # cast attack
            yield env.timeout(player.ability_list[1].gcd)
        if env.now >= run_length:
            break
    return total_damage


if __name__ == "__main__":
    main()
