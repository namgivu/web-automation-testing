"""This is the non-selenium way"""

from common import *
from s03a_config_local import *

#get html of a page via pure python ref. https://stackoverflow.com/a/23565355/248616
import requests
r = requests.get('http://fb.com/%s' % FB_USER_ID) #open profile page of the facebook user
r.raise_for_status()
html = r.content

#search string with regex ref. https://stackoverflow.com/a/4667014/248616
import re
# m = re.search('meta http-equiv="refresh" content="0; URL=/([^?]+)\?', html)
m = re.search('a class="profileLink" href="([^"]+)"', html)
href = m.group(1) #will be https://www.facebook.com/$FB_USER_NAME on 201705.24
username = href.split('/')[-1]
print(href)
print(username)