from mq import *
import RPI.GPIO as GPIO
import time
import glob
import os
import botbook_mcp3002 as mcp #

GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)


def check_temperature():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'  
    
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def smoke_level():
    mq = MQ();
    perc = mq.MQPercentage()
    smk=[perc["GAS_LPG"], perc["CO"], perc["SMOKE"]]
    return smk


def check_light():
    if(GPIO.digitalRead(3)==GPIO.HIGH and GPIO.digitalRead(2)==GPIO.LOW):
        return "ON"
    else:
        return "OFF"


def lights(action):
    if(action=="on"):
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(2, GPIO.LOW)
    elif(action=="off"):
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.LOW)
