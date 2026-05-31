from tkinter import *
from PIL import Image, ImageTk

Root = Tk()
Root.title("Image Display")
Root.geometry("400x400")

upload = Image.open("IMAGES\\bmw.jpg")
image = ImageTk.PhotoImage(upload)

Label1 = Label(Root, image=image, height=600, width=300)
Label1.place(x=50, y=0)
Label2 = Label(Root, text="BMW", font=("Arial", 20))
Label2.place(x=40, y=360)

Root.mainloop()