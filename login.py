from tkinter import *
from tkinter import messagebox
from firebase_admin import db

################ Functions ##################


'''def register():
    import register
    root1.destroy()
'''

def login():
    db.reference('Fire and Smoke')
    ref = db.reference('Fire and Smoke')
    if emaillabelentry.get()=='' or passlabelentry.get()=='':
        messagebox.showerror('Error','All fields are reequired')
        emaillabelentry.delete(0,END)
        passlabelentry.delete(0,END)

    email0 = ref.child('Admin').child('email').get()
    passw0 = ref.child('Admin').child('Password').get()
    if emaillabelentry.get() == email0 and passlabelentry.get() == passw0:
        root1.destroy()
        import Home


################# GUI ######################

root1 =Tk()

root1.geometry('740x460+150+20')
root1.title('Fire And Smoke Detector')

#background image and place on root
bgimage = PhotoImage(file='bg-image.png')
bglabel = Label(root1,image= bgimage)
bglabel.place(x=0,y=0)


#title for Form
titlelabel= Label(root1,text='Login',font=('Times New Roman',22,'bold'),bg='lightblue')
titlelabel.place(x=350,y=25)

#userImage
userimage = PhotoImage(file='user1.png')
userimagelabel = Label(root1,image = userimage)
userimagelabel.place(x=100,y=100)

#email & Password
emaillabel=Label(root1,text='Email Address',font=('times new roman',18,'bold'),bg='lightblue')
emaillabel.place(x=400,y=100)
emaillabelentry = Entry(root1,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
emaillabelentry.place(x=400,y=150)

passlabel=Label(root1,text='Password',font=('times new roman',18,'bold'),bg='lightblue')
passlabel.place(x=400,y=210)
passlabelentry = Entry(root1,font=('times new roman',18,'bold'),fg='black',bg='lightgrey',show='*')
passlabelentry.place(x=400,y=260)
'''
#register Button
regButton = Button(root1,text='Register New Account',font=('Arial',14),bd=0,fg='green',
                   cursor='hand2',activebackground='lightgrey',command=register)
regButton.place(x=100,y=320)
'''
#Forgot Password
forgotButton = Button(root1,text='Forget Password?',font=('Arial',14),bd=0,fg='red',
                   cursor='hand2',activebackground='lightgrey',activeforeground='red')
forgotButton.place(x=400,y=320)

#Login Button
loginImg = PhotoImage(file='login.png')
LoginButton = Button(root1,text='Login',image=loginImg,font=('Arial',14),bd=0,
                   cursor='hand2',activebackground='lightgrey',command=login)
LoginButton.place(x=270,y=380)


root1.mainloop()