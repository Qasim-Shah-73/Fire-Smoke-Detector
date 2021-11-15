from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from firebase_admin import db

########## functions #############

def login1():
    root.destroy()
    import login

def clear():
    firstentrylabel.delete(0,END)
    lastentrylabel.delete(0, END)
    contactentrylabel.delete(0, END)
    emailentry.delete(0, END)
    answerentry.delete(0, END)
    passwordentry.delete(0, END)
    confirmentry.delete(0, END)
    securityComobox.set(0)

def signup():
    if firstentrylabel.get()=='' or lastentrylabel.get()=='' or contactentrylabel==''\
        or emailentry=='' or securityComobox.get()=='Select' or answerentry ==''\
        or passwordentry=='' or confirmentry=='':
        messagebox.showerror('Error','All fields are required')
    elif passwordentry.get() != confirmentry.get():
        messagebox.showerror('Error', 'Password entered not same')
    else:
        ### insert into DB if cleared
        db.reference('Fire and Smoke')
        ref = db.reference('Fire and Smoke')

        admin_ref = ref.set(
            {
                'Admin': {
                    'fname': firstentrylabel.get(),
                    'lname': lastentrylabel.get(),
                    'email': emailentry.get(),
                    'contact': contactentrylabel.get(),
                    'security': securityComobox.current(),
                    'Answer': answerentry.get(),
                    'Password': passwordentry.get()
                }
            }
        )
        clear()
        messagebox.showinfo('Sucess','Admin Registreed Succesfully')

root = Tk()

root.geometry('1000x730+150+20')
root.title('Fire And Smoke Detector')

#background image and place on root
bgimage = PhotoImage(file='background.png')
bglabel = Label(root,image= bgimage)
bglabel.place(x=0,y=0)

#title for Form
titlelabel= Label(root,text='Registeration Form',font=('Times New Roman',22,'bold'),fg='yellow',bg='black')
titlelabel.place(x=400,y=50)

#Name Entries
firstnamelabel=Label(root,text='First Name',font=('times new roman',18,'bold'),fg ='yellow',bg='black')
firstnamelabel.place(x=100,y=150)
firstentrylabel = Entry(root,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
firstentrylabel.place(x=100,y=190)

lastnamelabel=Label(root,text='Last Name',font=('times new roman',18,'bold'),fg ='yellow',bg='black')
lastnamelabel.place(x=600,y=150)
lastentrylabel = Entry(root,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
lastentrylabel.place(x=600,y=190)

#contact number
contactnumlabel=Label(root,text='Contact Number',font=('times new roman',18,'bold'),fg ='yellow',bg='black')
contactnumlabel.place(x=100,y=250)
contactentrylabel = Entry(root,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
contactentrylabel.place(x=100,y=290)

#email Address
emaillabel=Label(root,text='Email Address',font=('times new roman',18,'bold'),fg ='yellow',bg='black')
emaillabel.place(x=600,y=250)
emailentry = Entry(root,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
emailentry.place(x=600,y=290)

#Security Question
securitylabel=Label(root,text='Security Questions',font=('times new roman',18,'bold'),fg ='yellow',bg='black')
securitylabel.place(x=100,y=350)
securityComobox = ttk.Combobox(root,font=('times new roman',18,'bold') ,state='readonly',
                    values=('Select','Your first Pet Name?','Your Fav color?','Your Best Friend Name?'))
securityComobox.place(x=100,y=390)
securityComobox.current(0)

#Security Answer
answerlabel=Label(root,text='Answer',font=('times new roman',18,'bold'),fg ='yellow',bg='black')
answerlabel.place(x=600,y=350)
answerentry = Entry(root,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
answerentry.place(x=600,y=390)

#Password
passwordlabel=Label(root,text='Password',font=('times new roman',18,'bold'),fg ='yellow',bg='black')
passwordlabel.place(x=100,y=450)
passwordentry = Entry(root,font=('times new roman',18,'bold'),fg='black',bg='lightgrey',show='*')
passwordentry.place(x=100,y=490)

confirmlabel=Label(root,text='Confirm Password',font=('times new roman',18,'bold'),fg ='yellow',bg='black')
confirmlabel.place(x=600,y=450)
confirmentry = Entry(root,font=('times new roman',18,'bold'),fg='black',bg='lightgrey',show='*')
confirmentry.place(x=600,y=490)

#sign Up Button
signupImage = PhotoImage(file='sign up.png')
signupButton = Button(root,image = signupImage, bd = 0,cursor='hand2',command = signup)
signupButton.place(x = 250, y = 600)

#Login Button
LoginImage = PhotoImage(file='logn.png')
LoginButton = Button(root,image = LoginImage, bd = 0,cursor='hand2',command=login1)
LoginButton.place(x = 550, y = 600)

root.mainloop()