from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def msg():
    messagebox.showwarning("!!!ALERT!!!", "VIRUS DETECTED! REMOVING NOW !! ")
    

button1 = Button(root, text="SCAN FOR VIRUSES IN SYSTEM", command=msg)
button1.place(x=40, y=40)

root.mainloop()