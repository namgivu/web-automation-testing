#import all test module
from test_vault import *


#create group of groups
from proboscis import register
register(groups=['basic'],    depends_on_groups=['number','string'])
register(groups=['advance'],  depends_on_groups=['user', 'service'])


#run test via proboscis
from proboscis import TestProgram
TestProgram().run_and_exit()
