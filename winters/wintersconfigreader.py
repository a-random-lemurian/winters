# Reads Wintersconfig.yaml files in plugin folders

import yaml


def winterscfg(path):
    with open(path, 'r') as winterscfg:
        return yaml.safe_load(winterscfg)


def create_wintersconfig(path, data):
    with open(path, 'x') as winterscfg:
        yaml.dump(data, winterscfg)