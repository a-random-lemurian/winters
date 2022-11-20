# Path processing.
import appdirs
import os
import json

GLOBAL_CONFIG = json.load(os.path.join(appdirs.user_config_dir('winters'), '.wintersrc'))
