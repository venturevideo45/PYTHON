from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def ALERT():
    messagebox.showwarning("!!!ALERT!!!", "VIRUS DETECTED! REMOVING NOW !! ")

def YESNO():
    response = messagebox.askyesno("!!!ALERT!!!", "VIRUS DETECTED! DO YOU WANT TO REMOVE IT NOW !! ")
    if response:
        messagebox.showinfo("REMOVING", "REMOVING VIRUS NOW !!")
    else:
        messagebox.showinfo("CANCELLED", "VIRUS REMOVAL CANCELLED !!")

def QUES():
    response = messagebox.askquestion("RATINGS", " WAS YOUR EXPERIENCE WITH US AMAZING?")
    if response == 'yes':
        messagebox.showinfo("AMAZING", "THANK YOU FOR YOUR FEEDBACK, WE ARE GLAD TO HEAR THAT !!")
    else:
        messagebox.showinfo("POOR", "SORRY TO HEAR THAT, WE WILL TRY TO IMPROVE OUR SERVICE !!")

def ERROR():

    messagebox.showerror("ERROR", "AN ERROR OCCURRED WHILE SCANNING FOR VIRUSES !!")



button1 = Button(root, text="ALERT", command=ALERT)
button1.place(x=40, y=40)
button2 = Button(root, text="YES/NO", command=YESNO)
button2.place(x=40, y=80)
button3 = Button(root, text="QUESTION", command=QUES)
button3.place(x=40, y=120)
button4 = Button(root, text="ERROR", command=ERROR)
button4.place(x=40, y=160)
root.mainloop()

