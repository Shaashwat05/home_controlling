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
host="192.168.1.176"
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

def light(event):
    s.send(str.encode("light"))
    msg=s.recv(1024)
    print(msg.decode("utf-8"))
    ans=input()
    s.send(str.encode(ans))

def temp(event):
    s.send(str.encode("temperature"))
    temperature=s.recv(1024)
    print(temperature.decode("utf-8"))


def smokeLevel(event):
    s.send(str.encode("smoke"))
    smoke=s.recv(1024)
    print(smoke.decode("utf-8"))

def fan(event):
    s.send(str.encode("fan"))


def welcome(wc_msg,start):
    screen=Tk()
    back = PhotoImage(file="background1.png")
    screen.geometry("300x500")
    screen.configure(bg='#525252')
    panel1 = Label(screen, image=back)
    welcome = Message(screen, text=wc_msg,bg='#353533', font =('Chilanka', 12, 'bold'), padx=70, pady=70 )
    welcome.place(relx=0.5, rely=0.15, anchor=CENTER)
    while True:
        panel1.pack(side='top', fill='both', expand='yes')
        welcome.pack_forget()
        #time.sleep(5)
        if(int(time.time()-start)>7):
            print("hi")
            break
        panel1.image = back
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
    style.configure('TButton', font =('Chilanka', 12, 'bold'), foreground = 'black', background="#383838", relief=FLAT ) 

    cam_im=PhotoImage(file="camera.png")
    camera=ttk.Button(screen, text="camera",image= cam_im,style = 'TButton',)
    camera.bind("<Button-1>", cam)
    camera.place(relx=0.5, rely=0.165, anchor=CENTER)

    temp_im=PhotoImage(file="temperature.png")
    temperature=ttk.Button(screen, text="temperature",image =temp_im, style = 'TButton')
    temperature.bind("<Button-1>", temp)
    temperature.place(relx=0.16, rely=0.30, anchor=CENTER)

    light_im=PhotoImage(file="lights.png")
    lights=ttk.Button(screen, text="lights",image=light_im, style = 'TButton')
    lights.bind("<Button-1>", light)
    lights.place(relx=0.13, rely=0.505, anchor=CENTER)

    fan_im=PhotoImage(file="fan.png")
    fans=ttk.Button(screen, text="fans",image=fan_im ,style = 'TButton')
    fans.bind("<Button-1>", fan)
    fans.place(relx=0.86, rely=0.51, anchor=CENTER)

    smoke_im=PhotoImage(file="smoke.png")
    smoke=ttk.Button(screen, text="smoke",image=smoke_im, style = 'TButton')
    smoke.bind("<Button-1>", smokeLevel)
    smoke.place(relx=0.86, rely=0.31, anchor=CENTER)

    panel1.image = back

    screen.mainloop()

    


while(True):
    wc_msg=s.recv(1024)
    wc_msg=wc_msg.decode("utf-8")
    print(wc_msg)
    app(wc_msg)
