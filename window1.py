from tkinter import *
from tkinter import messagebox
from firebase_admin import db


################ Functions ##################
def login():
    db.reference('Fire and Smoke')
    ref = db.reference('Fire and Smoke').child('Admin').get()
    if entry0.get()=='' or entry1.get()=='':
        messagebox.showerror('Error','All fields are reequired')
        entry0.delete(0,END)
        entry1.delete(0,END)
    i = -1
    j = -1
    email0 = entry0.get()
    passw0 = entry1.get()
    ref1 = str(ref)

    i = ref1.find("email': '{0}'".format(email0))
    j = ref1.find("Password': '{0}'".format(passw0))

    if i != -1 and j!=-1:
        window1.destroy()
        import Home


def forgotpassword():
    print("Button Clicked")
    window1.destroy()
    import window2


window1 = Tk()
window1.title('Login')
window1.geometry("1000x530")
window1.configure(bg = "#ffffff")
canvas = Canvas(
    window1,
    bg = "#ffffff",
    height = 530,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    708.5, 265.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    font=22)

entry0.place(
    x = 624.0, y = 244,
    width = 169.0,
    height = 40)

entry1_img = PhotoImage(file = f"img_textBox0.png")
entry1_bg = canvas.create_image(
    708.5, 366.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    show='*',
    font=22)

entry1.place(
    x = 624.0, y = 345,
    width = 169.0,
    height = 40)

background_img = PhotoImage(file = f"background1.png")
background = canvas.create_image(
    485.0, 265.0,
    image=background_img)

img0 = PhotoImage(file = f"img1.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b0.place(
    x = 637, y = 412,
    width = 145,
    height = 42)

img1 = PhotoImage(file = f"img11.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = forgotpassword,
    relief = "flat")

b1.place(
    x = 637, y = 463,
    width = 145,
    height = 20)

window1.resizable(False, False)
window1.mainloop()
