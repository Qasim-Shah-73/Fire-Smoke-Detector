from tkinter import *
from tkinter import messagebox
from firebase_admin import db

################# GUI ######################

root2 =Tk()

root2.geometry('740x460+150+20')
root2.title('Fire And Smoke Detector')

#background image and place on root
bgimage = PhotoImage(file='bg-image.png')
bglabel = Label(root2,image= bgimage)
bglabel.place(x=0,y=0)


#title for Form
titlelabel= Label(root2,text='Fire & Smoke Detection System',font=('Times New Roman',22,'bold'),bg='lightblue')
titlelabel.place(x=180,y=25)

#Change Admin Number
changeAdminlabel=Label(root2,text='Change Admin Number',font=('times new roman',18,'bold'),bg='lightblue')
changeAdminlabel.place(x=100,y=100)
changeAdminentry = Entry(root2,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
changeAdminentry.place(x=100,y=140)
change1Button = Button(root2,text='Change',font=('Arial',14),bd=0,fg='green',bg='lightgrey',
                   cursor='hand2',activebackground='grey',width='15')
change1Button.place(x=450,y=135)

#Change Manager Number
changeManagerlabel=Label(root2,text='Change Manager Number',font=('times new roman',18,'bold'),bg='lightblue')
changeManagerlabel.place(x=100,y=190)
changeManagerentry = Entry(root2,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
changeManagerentry.place(x=100,y=230)
change2Button = Button(root2,text='Change',font=('Arial',14),bd=0,fg='green',bg='lightgrey',
                   cursor='hand2',activebackground='grey',width='15')
change2Button.place(x=450,y=225)

#Change Emergency Number
changeEmergencylabel=Label(root2,text='Change Emergency Number',font=('times new roman',18,'bold'),bg='lightblue')
changeEmergencylabel.place(x=100,y=280)
changeEmergencyentry = Entry(root2,font=('times new roman',18,'bold'),fg='black',bg='lightgrey')
changeEmergencyentry.place(x=100,y=320)
change3Button = Button(root2,text='Change',font=('Arial',14),bd=0,fg='green',bg='lightgrey',
                   cursor='hand2',activebackground='grey',width='15')
change3Button.place(x=450,y=315)

#Generate Report
ReportButton = Button(root2,text='Generate Report',font=('Arial',14),bd=0,fg='black',bg='green',
                   cursor='hand2',activebackground='grey',width='15')
ReportButton.place(x=270,y=390)

#close Button
closeButton= Button(root2,text='Exit',font=('Arial',14),bd=0,fg='black',bg='red',
                   cursor='hand2',activebackground='grey')
closeButton.place(x=470,y=390)

root2.mainloop()