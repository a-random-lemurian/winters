# Reads Wintersconfig.yaml files in plugin folders

import yaml


def winterscfg(path):
    with open(path, 'r') as winterscfg:
        return yaml.safe_load(winterscfg)