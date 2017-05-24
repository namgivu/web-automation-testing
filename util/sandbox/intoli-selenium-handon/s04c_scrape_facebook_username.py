"""This is the non-selenium way"""

from common import *
from s03a_config_local import *

#get html of a page via pure python ref. https://stackoverflow.com/a/23565355/248616
import requests
r = requests.get('http://fb.com/%s' % FB_USER) #open profile page of the facebook user
r.raise_for_status()
html = r.content

#search string with regex ref. https://stackoverflow.com/a/4667014/248616
import re
m = re.search('meta http-equiv="refresh" content="0; URL=/([^?]+)\?', html)
username = m.group(1)
print(username)