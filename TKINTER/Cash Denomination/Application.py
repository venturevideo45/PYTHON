from logging import root
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Cash Denomination")
window.geometry("650x400")
window.configure(bg="darkblue")

upload = Image.open("D:\\CODING FILE\\PYTHON\\TKINTER\\Cash Denomination\\logo.jpg")
upload = upload.resize((100, 100))
label = ImageTk.PhotoImage(upload)
logo_label = Label(window, image=label, bg="white",  borderwidth=4, relief="solid")
logo_label.pack(pady=10)

def msg ():
   MsgBox = messagebox.showinfo("Cash Denomination", "This is a simple application to calculate the number of notes required for a given amount of money.")

   if MsgBox == "ok" :
         messagebox.showinfo("Cash Denomination", "User accepted message initiating application..........")
         topwin()
        


button1 = Button(window, text="///START PROGRAM///", command=msg, bg="white", fg="black", font=("Arial", 12, "bold"), borderwidth=4, relief="solid")
button1.pack(pady=20)

def topwin():
    top = Toplevel()
    top.title("Cash Denomination Calculator")
    top.geometry("400x300")
    top.configure(bg="lightblue")

    label1 =  Label( top, text="Enter the amount:", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid")
    Entry1 = Entry( top, font=("Arial", 12), borderwidth=4, relief="solid" )
    lb1 = Label( top, text="Number of notes:", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )

    l1 = Label(top, text="1000: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )
    l2 = Label(top, text="500: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )
    l3 = Label(top, text="100: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )
    l4 = Label(top, text="50: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )
    l5 = Label(top, text="20: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )
    l6 = Label(top, text="10: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )
    l7 = Label(top, text="5: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )
    l8 = Label(top, text="2: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )
    l9 = Label(top, text="1: ", bg="lightblue", font=("Arial", 12), borderwidth=4, relief="solid" )

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    t7 = Entry(top)
    t8 = Entry(top)
    t9 = Entry(top)

    def calculate():

        try:
            global amount
            amount = int(Entry1.get())
            note1000 = amount // 1000
            amount %= 1000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50
            note20 = amount // 20
            amount %= 20
            note10 = amount // 10
            amount %= 10
            note5 = amount // 5
            amount %= 5
            note2 = amount // 2
            amount %= 2
            note1 = amount // 1
            amount %= 1

            t1.delete(0, END)
            t1.insert(0, str(note1000))
            t2.delete(0, END)
            t2.insert(0, str(note500))
            t3.delete(0, END)
            t3.insert(0, str(note100))
            t4.delete(0, END)
            t4.insert(0, str(note50))
            t5.delete(0, END)
            t5.insert(0, str(note20))
            t6.delete(0, END)
            t6.insert(0, str(note10))
            t7.delete(0, END)
            t7.insert(0, str(note5))
            t8.delete(0, END)
            t8.insert(0, str(note2))
            t9.delete(0, END)
            t9.insert(0, str(note1))

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer amount.")


    btn = Button(top, text='Calculate', command=calculate, bg='brown', fg='white')

    label1.place(x=230, y=50)
    Entry1.place(x=200, y=80)
    btn.place(x=240, y=120)
    lb1.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)
    l5.place(x=180, y=320)
    l6.place(x=180, y=350)
    l7.place(x=180, y=380)
    l8.place(x=180, y=410)
    l9.place(x=180 ,y= 440)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)
    t5.place(x=270, y=320)
    t6.place(x=270, y=350)
    t7.place(x=270, y=380)
    t8.place(x=270, y=410)
    t9.place(x=270 ,y= 440)



    top.mainloop()

window.mainloop()

            




    
     
