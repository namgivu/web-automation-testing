#import all test module
from test_vault import *

#run test via proboscis
from proboscis import TestProgram
TestProgram().run_and_exit()
