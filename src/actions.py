import os
import json

from abilities import Ability


def get_class_actions_json(class_name):
    action_file = os.path.join("./resources", f"{class_name.lower()}_actions.json")
    with open(action_file, "r") as file:
        data = json.load(file)
    return data


class ActionPriorityList:
    def __init__(self):
        self.action_class = ""
        self.actions = []
        self.variables = {}
        self.action_lists = {}

    def build_list(self, action_list):
        self.action_class, actions = action_list
        for action in actions:
            self.add(self.create_ability(self.action_class, action))

    def create_ability(self, action_class, action):
        match action_class.lower():
            case "rogue":
                return Ability(
                    **get_class_actions_json(action_class)[action],
                )
            case _:
                raise Exception("Error: action class not specified in action file")

    def add(self, action):
        self.actions.append(action)

    def __iadd__(self, other):
        if isinstance(other, str):
            self.actions.append(other)
        else:
            raise TypeError(
                f"Error: Unsupported operand type(s) for +='{type(other).__name__}'"
            )
        return self

    def __repr__(self):
        return f"{self.actions}"

    def call_action_list(self):
        raise NotImplementedError

    def run_action_list(self):
        raise NotImplementedError
