import os
import sys

import logging

DEBUG = True

LOG_FILE = "./log.log"
LOG_LEVEL = logging.DEBUG

logger = logging.getLogger()


plain_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Add json formatter for log file.

def config_logger(log):
    logger = logging.getLogger(log)

    if DEBUG:
        stream = logging.StreamHandler()
        stream.setFormatter(plain_formatter)
        logger.addHandler(stream)

    file = logging.FileHandler(LOG_FILE)
    file.setFormatter(plain_formatter)
    logger.addHandler(file)

    logger.setLevel(LOG_LEVEL)

    return logger

DB_PATH = '/Users/ingrid/Dev/dashboard/server/api/db'
DB_PATH = "/Users/icheung/Dev/foo/server/api/db"

envkeys = []
this_module = sys.modules[__name__]
for key in envkeys:
    setattr(this_module, key, os.environ.get(key, None))

