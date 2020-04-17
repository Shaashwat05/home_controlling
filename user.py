import socket
import os
import subprocess
from tkinter import *
import tkinter.ttk as ttk
import time


s=socket.socket()
host="192.168.1.172"
port=9999

s.connect((host,port))



def cam(event):
    s.send(str.encode("camera"))

def temp(event):
    s.send(str.encode("temperature"))
    temperature=s.recv(1024)
    print(temperature.decode("utf-8"))


def welcome(wc_msg,start):
    screen=Tk()
    screen.geometry("300x500")
    screen.configure(bg='#525252')
    welcome = Message(screen, text=wc_msg,bg='#525252', font =('Chilanka', 12, 'bold'), padx=70, pady=70 )
    welcome.place(relx=0.5, rely=0.35, anchor=CENTER)
    while True:
    
    #if(i<=100):
        welcome.pack_forget()
        #time.sleep(5)
        if(int(time.time()-start)>3):
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
    screen.geometry("300x500")
    screen.configure(bg='#525252')
    style = ttk.Style()   
    style.configure('TButton', font =('Chilanka', 12, 'bold'), foreground = 'black', background='white', relief=FLAT ) 

        

    camera=ttk.Button(screen, text="camera",style = 'TButton')
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
    smoke.place(relx=0.5, rely=0.8, anchor=CENTER)

    screen.mainloop()

    


while(True):
    wc_msg=s.recv(1024)
    wc_msg=wc_msg.decode("utf-8")
    print(wc_msg)
    app(wc_msg)
