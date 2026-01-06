import math
from player import Player, StatBlock
from targetdummy import TargetDummy


def main():
    statblock = StatBlock(100, 30, 30, 30, 30)
    player = Player(statblock, 3, 10, 2.4)
    target = TargetDummy(1000, 30)
    calculate_total_damage_over_period(player, target, 5 * 60)


def calculate_total_damage_over_period(player, target, total_time_in_seconds):
    damage_instance = player.do_damage(
        target,
    )
    total_damage = damage_instance * math.floor(
        (total_time_in_seconds / player.attack_speed)
    )
    print(f"player did {total_damage} over {total_time_in_seconds} seconds")


if __name__ == "__main__":
    main()
