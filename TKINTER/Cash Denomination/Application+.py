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

    label1 = Label(top, text="Enter the amount:", bg="lightblue", font=("Arial", 12))
    label1.pack(pady=10)

    entry = Entry(top, font=("Arial", 12))
    entry.pack(pady=5)

    def calculate():
        try:
            amount = int(entry.get())
            denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
            result = {}
            for denom in denominations:
                count = amount // denom
                if count > 0:
                    result[denom] = count
                    amount -= denom * count
            result_str = "\n".join([f"{denom}: {count}" for denom, count in result.items()])
            messagebox.showinfo("Denominations", f"Number of notes:\n{result_str}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer amount.")

    calculate_button = Button(top, text="Calculate", command=calculate, bg="white", fg="black", font=("Arial", 12), borderwidth=4, relief="solid")
    calculate_button.pack(pady=20)
window.mainloop()


