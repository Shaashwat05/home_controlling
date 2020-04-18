import RPI.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor
import time
import botbook_mcp3002 as mcp #


def check_temperature():
    sensor = W1ThermSensor()
    temperature = sensor.get_temperature()
    return temperature

def smoke_level():
    smokeLevel= mcp.readAnalog()
    print ("Current smoke level is %i " % smokeLevel) #
    if smokeLevel > 120:
        return "smoke detected",smokeLevel
    else:
        return "your house is smoke free", smokeLevel


    


