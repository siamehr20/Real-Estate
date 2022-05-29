import json
import os


def save_to_file(file_path , data):
    with open(file_path , 'a') as f:
        f.write(json.dumps(data)+'\n')


def load_data(file_path):
    with open(file_path , 'r') as f:
        lines = f.read()
        agents = json.loads(lines)
    return agents
