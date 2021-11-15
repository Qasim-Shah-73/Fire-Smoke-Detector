from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from firebase_admin import db


######### Functions #################3

def login():
    window.destroy()
    import window1

def clear():
    entry0.delete(0,END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    securityComobox.set('Select')


def signup():
    if entry0.get()=='' or entry1.get()=='' or entry2.get()==''\
        or entry3.get()=='' or securityComobox.get()=='Select' or entry5.get() ==''\
        or entry6.get()=='' or entry7.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif entry6.get() != entry7.get():
        messagebox.showerror('Error', 'Password entered not same')
    else:
        ### insert into DB if cleared
        db.reference('Fire and Smoke')
        ref = db.reference('Fire and Smoke')

        admin_ref = ref.set(
            {
                'Admin': {
                    'fname': entry0.get(),
                    'lname': entry1.get(),
                    'email': entry2.get(),
                    'contact': entry3.get(),
                    'security': securityComobox.current(),
                    'Answer': entry5.get(),
                    'Password': entry6.get()
                }
            }
        )
        clear()
        messagebox.showinfo('Sucess','Admin Registreed Succesfully')


window = Tk()
window.title('Sign Up')
window.geometry("1000x730")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 730,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    535.5, 231.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    font=22)

entry0.place(
    x = 451.0, y = 210,
    width = 169.0,
    height = 40)

entry1_img = PhotoImage(file = f"img_textBox0.png")
entry1_bg = canvas.create_image(
    864.5, 231.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    font=22)

entry1.place(
    x = 780.0, y = 210,
    width = 169.0,
    height = 40)

entry2_img = PhotoImage(file = f"img_textBox0.png")
entry2_bg = canvas.create_image(
    535.5, 349.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    font=22)

entry2.place(
    x = 451.0, y = 328,
    width = 169.0,
    height = 40)

entry3_img = PhotoImage(file = f"img_textBox0.png")
entry3_bg = canvas.create_image(
    864.5, 349.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    font=22)

entry3.place(
    x = 780.0, y = 328,
    width = 169.0,
    height = 40)



securityComobox = ttk.Combobox(window,font=('Arial',13),state='readonly',
                    values=('Select','First Pet Name?','Favourite color?','Best Friend Name?'))
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#e9e9e9", background= "#e9e9e9",borderwidth='0px')

securityComobox.place(x = 441.0, y = 454,width = 211.0,height=42)
securityComobox.current(0)

entry5_img = PhotoImage(file = f"img_textBox0.png")
entry5_bg = canvas.create_image(
    864.5, 465.0,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0,
    font=22)

entry5.place(
    x = 780.0, y = 444,
    width = 169.0,
    height = 40)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    491.0, 365.0,
    image=background_img)

entry6_img = PhotoImage(file = f"img_textBox0.png")
entry6_bg = canvas.create_image(
    535.5, 585.0,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0
    ,show='*',
    font=22)

entry6.place(
    x = 451.0, y = 564,
    width = 169.0,
    height = 40)

entry7_img = PhotoImage(file = f"img_textBox0.png")
entry7_bg = canvas.create_image(
    864.5, 583.0,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0
    ,show='*',
    font=22)

entry7.place(
    x = 780.0, y = 562,
    width = 169.0,
    height = 40)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = signup,
    cursor='hand2',
    relief = "flat")

b0.place(
    x = 530, y = 654,
    width = 145,
    height = 42)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b1.place(
    x = 721, y = 654,
    width = 145,
    height = 42)

window.resizable(False, False)
window.mainloop()
