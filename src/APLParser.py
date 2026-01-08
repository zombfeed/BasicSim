import os


def parse_actions_file(file_path):
    ext = os.path.splitext(file_path)[1]
    if ext != ".actions":
        raise Exception(f"Error: Invalid file type {ext}")
    actions = []
    action_class = ""
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("#"):
                continue
            if line.startswith("!#"):
                action_class = line.split("!#")[1].strip()
                continue
            if line.startswith("actions="):
                actions = [line.split("=")[1].strip()]
            if line.startswith("actions+="):
                actions.append(line.split("+=")[1].strip())

    return action_class, actions
