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
actions={ability1}
actions+={ability2}
actions+={ability3}
```

- `#!` tells the program that this APL is for the specified class, and expects abilities added to the actions list to be for that class.
- `actions=` begins the list
- `actions+=` adds the following ability to the list


