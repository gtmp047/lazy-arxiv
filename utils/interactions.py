from os.path import dirname, join, exists, abspath, normpath

import yaml
from dotted.collection import DottedDict
from numpy.core.tests.test_scalarinherit import C

PROJECT_NAME = 'lazy-arxiv'
PROJECT_ROOT_DIR_PATH = abspath(join(dirname(__file__), '..', '..'))

CONFIG_FILE_NAME = 'configs/admin.conf'
LOG_FILE_NAME = f'{PROJECT_NAME}.log'

CONFIG_FILE_PATH = join(PROJECT_ROOT_DIR_PATH, PROJECT_NAME, CONFIG_FILE_NAME)

LOG_DIR_PATH = join(PROJECT_ROOT_DIR_PATH, PROJECT_NAME, 'logs')
LOG_FILE_PATH = join(LOG_DIR_PATH, LOG_FILE_NAME)

DATA_DIR_PATH = join(PROJECT_ROOT_DIR_PATH, PROJECT_NAME, 'data')

assert exists(CONFIG_FILE_PATH), 'CONFIG_FILE_PATH not detected!'
# assert exists(LOG_DIR_PATH), 'LOG_FILE_PATH not detected!'

with open(CONFIG_FILE_PATH) as conf_file:
    CONFIG = DottedDict(yaml.safe_load(conf_file))
    CONFIG.data.sqllite = join(DATA_DIR_PATH, CONFIG.data.sqllite)
