import os
import json

with open('config.json') as conf:
    config = json.load(conf)

file_path = os.path.join(config['uri'], 'teste.txt')