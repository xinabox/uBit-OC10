from OC10 import OC10
from microbit import *

OC10 = OC10()

# start OC10
OC10.init()

# sleep time
DELAY = 5000

# infinite loop
while True:

    # close relay
    OC10.writePin(True)		
    sleep(DELAY)
    
    # open relay
    OC10.writePin(False)
    sleep(DELAY)
