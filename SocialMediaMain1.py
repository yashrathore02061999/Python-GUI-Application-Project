from YashRathoreSocialMediaApplication import MyApp1
from tkinter import *

'''
In our YashRathoreSocial....  .py is our pyton module or python file in which we have defined a class named MyApp1. Also in the YashRthoreSocial... .py
we have defined many independent functions like buttonClick1(),buttonClick2(),buttonClick3(),buttonClick4() etc.
TO access the class MyApp1 from module named YashRathoreSocial.... .py we have imported the class MyApp1 from the module using the statement
from YashRathoreSocialMediaApplication import MyApp1.


Using statement from tkinter import * we have imported all classes and functions from the tkinter module of python.
'''

root=Tk()


'''
Tk is a predefined class in tkinter module of Python. In above statement we have created an object of Tk() class. Then we have assigned
the object of class Tk() to the variable named root on the LHS of the assignment statement. So remember that root is not a keyword but a variable name.
We could have used any variable name instead of root.  So now in the above statement the variable named root represents the root window of the 
python gui application.

'''
root.title("YASH RATHORE SOCIAL MEDIA APPLICATION")
'''
in above statement we have set the title of the root window to YASH RATHORE SOCIAL MEDIA APPLICATION in the title bar.
'''
root.geometry('1200x1200')
'''
title(),geometry(),configure() etc. are the predefined member functions or member methods of the Tk class. So we have called these member methods
by using the dot operator on the variable named root which stores the Tk class object.
In above statement we have set the width and height of the root window where in 1200x1200 ,the 1st 1200 represents the width and 2nd 1200 represents height.

'''
root.configure(bg='cyan')
'''
in above statement we have set the background color of the root window by passing the bg attribute as input argument to the configure()
non static member member method called on the root variable. cyan is light blue.
'''
m1=MyApp1(root)

'''
In above statement we have called the constructor of the class MyApp1 and passed the root variable as input argument to the constructor of class MyApp1
and the new object of class MyApp1 created is assigned to variable m1. 
'''

'''
To display graphical output we need screen space i.e. space on output screen.  The space allocated initially to every gui python pgm 
on output screen is called as root window. This root window is a top level window.
The root window is highest GUI component in the tkinter python application.

Here in the application when we run the application the entire window which is obtained after enlarging the window is the root window.


'''




