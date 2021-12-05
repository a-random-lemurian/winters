# Path processing.
import appdirs
import os
import yaml

GLOBAL_CONFIG = yaml.load(os.path.join(appdirs.user_config_dir('winters'), '.wintersrc'))
