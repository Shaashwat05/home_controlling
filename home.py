import socket
import sys
#from home_system import *

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
            temperature="50"
            conn.send(str.encode(temperature))





def main():
    create_socket()
    bind_socket()
    accept()

main()