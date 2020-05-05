import logging
from datetime import datetime
import os
import sys

#TODO simplify log params

logging.getLogger().setLevel(logging.DEBUG)

#region config logger
'''
customize logger
ref. https://stackoverflow.com/a/28330410/248616
'''

# log to file
APP_HOME  = os.path.abspath(f'{os.path.dirname(__file__)}/../../..')
timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
filename  = f'{APP_HOME}/_log_/vault/log{timestamp}.txt'

file_handler = logging.FileHandler(filename, mode='w')
formatter    = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)

# log to console
screen_handler = logging.StreamHandler(stream=sys.stdout)
screen_handler.setFormatter(formatter)

# set it
logging.getLogger().addHandler(file_handler)
logging.getLogger().addHandler(screen_handler)

#endregion config logger

#region log alias/shorthand name
def log(text):
    logging.info(text)
def debug(text):
    logging.debug(text)
l  = log
ld = debug

def log_level(level=logging.INFO):
    logging.getLogger().setLevel(level)
#endregion log alias/shorthand name
