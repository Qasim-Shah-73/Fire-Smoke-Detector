from tkinter import *


def PwdChange():
    print("Button Clicked")
    window2.destroy()
    import window3


window2 = Tk()

window2.geometry("1000x600")
window2.configure(bg = "#ffffff")
canvas = Canvas(
    window2,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    708.5, 390.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0)

entry0.place(
    x = 624.0, y = 369,
    width = 169.0,
    height = 40)

entry1_img = PhotoImage(file = f"img_textBox0.png")
entry1_bg = canvas.create_image(
    708.5, 279.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e9e9e9",
    highlightthickness = 0)

entry1.place(
    x = 624.0, y = 258,
    width = 169.0,
    height = 40)

background_img = PhotoImage(file = f"background2.png")
background = canvas.create_image(
    485.0, 300.0,
    image=background_img)

img0 = PhotoImage(file = f"reset.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = PwdChange,
    relief = "flat")

b0.place(
    x = 641, y = 455,
    width = 145,
    height = 42)

window2.resizable(False, False)
window2.mainloop()
