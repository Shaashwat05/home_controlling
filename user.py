import socket
import os
import subprocess
from tkinter import *
import tkinter.ttk as ttk
import time
from pickle import loads,dumps
import cv2
import struct



s=socket.socket()
host="192.168.1.173"
port=9999

s.connect((host,port))



def cam(event):
    s.send(str.encode("camera"))
    data = b""
    rec_size = struct.calcsize(">L")
    while True:
        data = b""
        rec_size = struct.calcsize(">L")
        while(len(data)<rec_size):
            data+=s.recv(4096)
        print("Started receiving data")
        inp_msg_size = data[:rec_size]
        data = data[rec_size:]
        msg_size = struct.unpack(">L",inp_msg_size)[0]
        while(len(data)<msg_size):
            data+= s.recv(4096)
        fr_data = data[:msg_size]
        data = data[msg_size:]
        
        frame = loads(fr_data,fix_imports = True,encoding = "bytes")
        frame = cv2.imdecode(frame,cv2.IMREAD_COLOR)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):

            break
    cv2.destroyAllWindows()
    s.send(str.encode('quit'))
    print("hi")

def temp(event):
    s.send(str.encode("temperature"))
    temperature=s.recv(1024)
    print(temperature.decode("utf-8"))


def smokeLevel(event):
    s.send(str.encode("smoke"))
    smoke=s.recv(1024)
    print(smoke.decode("utf-8"))


def welcome(wc_msg,start):
    screen=Tk()
    screen.geometry("300x500")
    screen.configure(bg='#525252')
    welcome = Message(screen, text=wc_msg,bg='#525252', font =('Chilanka', 12, 'bold'), padx=70, pady=70 )
    welcome.place(relx=0.5, rely=0.35, anchor=CENTER)
    while True:
        welcome.pack_forget()
        #time.sleep(5)
        if(int(time.time()-start)>2):
            print("hi")
            break
        screen.update_idletasks()
        screen.update()
    screen.destroy()

def app(wc_msg):
    start=time.time()
    welcome(wc_msg,start)
    #panel1.place(x=0, y=0, relwidth=1, relheight=1)
    screen=Tk()
    back = PhotoImage(file="background3.png")
    screen.geometry("300x500")
    panel1 = Label(screen, image=back)
    panel1.pack(side='top', fill='both', expand='yes')
    screen.configure(bg='#525252')
    style = ttk.Style()   
    style.configure('TButton', font =('Chilanka', 12, 'bold'), foreground = 'black', background='white', relief=FLAT ) 

        
    cam_im=PhotoImage(file="camera.png")
    camera=ttk.Button(screen, text="camera",image= cam_im,style = 'TButton',)
    camera.bind("<Button-1>", cam)
    camera.place(relx=0.5, rely=0.2, anchor=CENTER)

    temperature=ttk.Button(screen, text="temperature", style = 'TButton')
    temperature.bind("<Button-1>", temp)
    temperature.place(relx=0.5, rely=0.35, anchor=CENTER)

    lights=ttk.Button(screen, text="lights", style = 'TButton')
    lights.place(relx=0.5, rely=0.5, anchor=CENTER)

    fans=ttk.Button(screen, text="fans", style = 'TButton')
    fans.place(relx=0.5, rely=0.65, anchor=CENTER)

    smoke=ttk.Button(screen, text="smoke", style = 'TButton')
    smoke.bind(("<Button-1>", smokeLevel))
    smoke.place(relx=0.5, rely=0.8, anchor=CENTER)

    panel1.image = back

    screen.mainloop()

    


while(True):
    wc_msg=s.recv(1024)
    wc_msg=wc_msg.decode("utf-8")
    print(wc_msg)
    app(wc_msg)
