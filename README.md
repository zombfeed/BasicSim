# BasicSim

Program that runs basic DPS simulation of a World of Warcraft class in the command line.

Prints in command line the simulation results
```
Running simulation...
Total damage: 528600
DPS: 1762.0
```

## How to Run

- In command line, run `./main.sh ./resources/{.actions file}`

## Making an APL
This program parses custom made `.actions` files to run, which contains the action priority list for the simulation

A `.actions` file looks like this:
```
!#rogue
actions=sinister_strike
actions+=attack
```

```
#!{class_name}
actions={action1}
actions+={action2}
actions+={action3}
```

- `#!` tells the program that this APL is for the specified class, and expects actions added to the actions list to be for that class.
- `actions=` begins the list
- `actions+=` adds the following action to the list

## Actions

Actions added to the APL must be valid actions. Valid actions are defined in the `/resources/{class_name}_actions.json` file.
To add a new action, it must be in the following format:
```
"attack": {
    "name": "attack",            # Name of the action
    "resource_type": 0,          # An enum value for resource type (0: None, 1: Energy, 2: Rage, 3: Mana) 
    "gcd": 1,                    # Length of the global cooldown applied to the ability in seconds
    "cooldown": 0,               # Length of the ability's own cooldown in seconds
    "resource_cost": 0,          # Resource cost of the ability
    "ability_type": 1,           # An enum value for ability type (0: None, 1: Damage, 2: Healing, 3: Utility)
    "ability_power": 10,         # Damage multiplier for the ability
    "ignore_armor": false        # If this action ignores target's armor value
```

