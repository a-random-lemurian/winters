# Reads Wintersconfig.yaml files in plugin folders

import json


def read_wintersconfig(path):
    with open(path, 'r') as winterscfg:
        return json.load(winterscfg)


def create_wintersconfig(path, data):
    with open(path, 'x') as winterscfg:
        json.dump(data, winterscfg)