from tkinter import *
import tkinter.ttk as ttk



screen=Tk()
screen.geometry("300x500")
screen.configure(bg='#525252')
#panel1.place(x=0, y=0, relwidth=1, relheight=1)



style = ttk.Style()   
style.configure('TButton', font =('Chilanka', 12, 'bold'), foreground = 'black', background='white', relief=FLAT ) 


camera=ttk.Button(screen, text="camera",style = 'TButton')
#camera.bind("<Button-1>", cam)
camera.place(relx=0.5, rely=0.2, anchor=CENTER)
screen.grid_forget()


temperature=ttk.Button(screen, text="temperature", style = 'TButton')
#temperature.bind("<Button-1>", temp)
temperature.place(relx=0.5, rely=0.35, anchor=CENTER)

lights=ttk.Button(screen, text="lights", style = 'TButton')
lights.place(relx=0.5, rely=0.5, anchor=CENTER)

fans=ttk.Button(screen, text="fans", style = 'TButton')
fans.place(relx=0.5, rely=0.65, anchor=CENTER)

smoke=ttk.Button(screen, text="smoke", style = 'TButton')
smoke.place(relx=0.5, rely=0.8, anchor=CENTER)


screen.mainloop()