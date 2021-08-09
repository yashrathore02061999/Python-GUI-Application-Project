
#for whatsapp: pip install pywhatkit
#for fb messegner: pip install puautogui
#for sms pip install requests, pip install jason,create accpunt on way2sms

import pywhatkit
import pyautogui
import time
from tkinter import *

'''
In python we have GUI applications i.e. graphical user interface applications i.e. applications containing frames,buttons,text boxes,labels
etc. and other components by which the user can interact with the application and store and process data in the application. 
The tkinter full form is toolkit interface.
The tkinter represents toolkit interface for GUI. 
tHE tkinter interface enables python programmers to use the classes of TK i.e. toolkit module of TCL i.e. Tool Command Language.
Tool Command Language is a programming language like C,C++ etc. but which contains predefined classes for GUI. In our python pgm
we make use of the tkinter module or the tkinter package to use the predefined classes of TCL i.e. tool command language
to develop GUI applications in Python.

Also TCL Language internally uses TK i.e. Toolkit language to generate graphics on screen.
'''


def buttonClick4(self):
    global t
    message = t.get('1.0','end-1c')
    while True:
     pyautogui.typewrite(message)
     pyautogui.press('enter')
     time.sleep(15)




def buttonClick3(self):
    global t1

    global t
    number1 = t1.get('1.0', 'end-1c')
    message = t.get('1.0', 'end-1c')
    pywhatkit.sendwhatmsg(number1, message, 12, 55)


def buttonClick1(self):

    global f1
    global t
    global t1
    global flag
    global f2
    if flag==2:
      f2.pack_forget()

    flag=1
    f1 = Frame(root1, height=600, width=600)
    f1.pack()
    t = Text(f1, width=40, height=10,font=('Times New Roman', -16, ''))
    t1 = Text(f1, width=36, height=1, font=('Times New Roman', -16, ''))
    t1.insert(END, 'INSERT THE WHATS APP NUMBER')
    t.insert(END, 'INSERT THE TEXT ')
    b3 = Button(f1, text='SEND TO WHATSAPP', width=30, height=2, fg='black')
    t.grid(row=7, column=5, padx=20, pady=10)
    t1.grid(row=8, column=5, padx=20, pady=10)
    b3.grid(row=9, column=5, padx=10, pady=10)
    b3.bind("<Button-1>", buttonClick3)



def buttonClick2(self):
    global flag
    global f2
    global t
    if flag==1:
      f1.pack_forget()

    flag=2

    f2 = Frame(root1, height=600, width=600)
    f2.pack()
    t = Text(f2, width=40, height=10, font=('Times New Roman', -16, ''))
    t.insert(END, 'INSERT THE TEXT ')
    b3 = Button(f2, text='SEND TO FACEBOOK', width=30, height=2, fg='black')
    t.grid(row=7, column=5, padx=20, pady=10)
    b3.grid(row=9, column=5, padx=10, pady=10)
    b3.bind("<Button-1>",buttonClick4)



class MyApp1:
    def __init__(self,root):
        global root1
        global flag
        flag=0
        root1=root
        self.f=Frame(root1,width=900,height=900,bg="cyan")
        self.f.grid(row=0,column=0,padx=20,pady=20)
        self.f.pack()
        self.l1=Label(self.f,text='WELCOME TO SOCIAL MEDIA APPLICATION',width=40,height=1,font=('Times New Roman',-20,'bold'),fg='blue',bg='yellow')
        self.l2 = Label(self.f, text='CLICK ON YOUR CHOICE', width=20, height=1,font=('Times New Roman', -20, 'bold'),fg='green')
        self.b1=Button(self.f,text='WHATSAPP',width=10,height=2,fg='black')
        self.b2 = Button(self.f, text='FACEBOOK', width=10, height=2, fg='black')
        self.b1.bind("<Button-1>",buttonClick1)
        self.b2.bind("<Button-1>",buttonClick2)

        self.l1.grid(row=0,column=1,padx=0,pady=0)
        self.l2.grid(row=2,column=1,padx=10,pady=10)
        self.b1.grid(row=4,column=0,padx=10,pady=10)
        self.b2.grid(row=4,column=3,padx=10,pady=10)
        root.mainloop()





'''
to install:
pip install pyautogui
pip install pywhatkit

'''