import RPI.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor


def check_temperature():
    sensor = W1ThermSensor()
    temperature = sensor.get_temperature()
    return temperature
