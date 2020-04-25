import socket
import sys
#from home_system import *
import numpy as np
import cv2
from pickle import loads, dumps
import struct

wc_msg="WELCOME TO THE GABLINGS"

def create_socket():
    try:
        global host
        global s
        global port
        host=""
        port=9999
        s=socket.socket()
    except socket.error as mag:
        print("socket creation error",str(mag))


def bind_socket():
    try:
        global host
        global s
        global port

        print("binding the socket")
        s.bind((host,port))
        s.listen(5)


    except socket.error as mag:
        print("socket binding error ",str(mag)," retrying")
        bind_socket()


def accept():
    conn,adress=s.accept()
    print("ip : ",adress[0]," port : ",adress[1])
    send_command(conn)
    conn.close()


def send_command(conn):
    conn.send(str.encode(wc_msg))
    while True:
        command=conn.recv(1024)
        command=command.decode("utf-8")
        if(command=='temperature'):
            #temperature=check_temperature()
            temperature="50"
            conn.send(str.encode(temperature))
        if(command=='camera'):
            cap = cv2.VideoCapture(0)
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            i=1
            while True:
                i+=1
                ret,frame = cap.read()
                res,frame = cv2.imencode('.jpg',frame,encode_param)
                data = dumps(frame,0)
                size = len(data)
                conn.send(struct.pack(">L",size)+data)
                op=(conn.recv(1024)).decode("utf-8")
                if(op=="quit"):
                    break
            cap.release()
        if(command=="smoke"):
            #bool, smokeLevel=smoke_level()
            smokeLevel="130"
            conn.send(str.encode(smokeLevel))
        if(command=="lights"):
            '''chk=check_light():
            if(chk =="ON"):
                conn.send(str.encode("Lights are on,should I turn them off"))
                ans=(conn.recv(1024)).decode("utf-8")
                if(ans=="yes"):
                    lights("off")
            else:
                conn.send(str.encode("Lights are off,should I turn them on"))
                ans=(conn.recv(1024)).decode("utf-8")
                if(ans=="yes"):
                    lights("on")'''
        
        if(command=="fan"):
            None









def main():
    create_socket()
    bind_socket()
    accept()

main()
