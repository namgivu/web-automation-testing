import os

PWD      = os.path.abspath(os.path.dirname(__file__))
APP_HOME = os.path.abspath(f'{PWD}/..')


#region browser name
class Browser:
    Chrome  = 'Chrome'

    #TODO
    Firefox = 'Firefox'
    Edge    = 'Edge'
    Safari  = 'Safari'

BROWSERS = [
    Browser.Chrome,

    #TODO more browser support here
    # Browser.XXX
]
#endregion browser name


#region snapshot folder

# snapshot flag - TRUE/False means DO/DONT take snapshot during the run
SNAPSHOT_DEBUG = False

# the snapshot home
SNAPSHOT_HOME  = f'{APP_HOME}/_snapshot_'
SNAPSHOT_VAULT = f'{APP_HOME}/_snapshot_/vault'

# timestamp as 'YYYYmm-dd HHMMss ms' ref. https://stackoverflow.com/a/18406412/248616
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:-3]

# prepare folder to store snapshot files for each run
SNAPSHOT_FOLDER = '%s/%s' % (SNAPSHOT_VAULT, timestamp)

#endregion snapshot folder


#webdriver config i.e. to use local/remote webdriver
WEBDRIVER_REMOTE_HUB = ''  # empty means using local hub


#region load local config

#ensure exists
assert os.path.exists(f'{PWD}/config_local.py'), f'Config {PWD}/config_local.py not found - please clone one from {PWD}/config_local.TEMPLATE.py'

#load that config_local.py
from src.config_local import *

#endregion load local config
