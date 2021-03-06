import json
import os


def save_to_file(file_path, data):
    with open(file_path, 'a') as f:
        f.writelines(json.dumps(data))


def load_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.read()
        agents = json.loads(lines)
    return agents
