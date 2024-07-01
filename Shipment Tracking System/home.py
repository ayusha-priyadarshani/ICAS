from tkinter import *


import mysql.connector as sqltor
mycon=sqltor.connect(
    host='localhost',
    user='root',
    passwd='Mynameisayusha1!',
    database='miniproject')
 
window=Tk()
window.geometry('400x400')
window.title=("Shipment Tracking System")

from seller import *
from customer import *

greet = Label(window, font = ('arial', 30, 'bold'), text = "Welcome to Shipment Tracking System!")
greet.grid(row = 0,columnspan = 3)
f=('arial', 20)
sellerbtn=Button(window,text="Seller",command=sellerpage,bg="Blue",fg="white",font =f)
sellerbtn.grid(row=3,columnspan=3)
 
customerbtn=Button(window,text="Customer",command=customerlogin,bg="Blue",fg="white",font =f)
customerbtn.grid(row=5,columnspan=3)


window.mainloop()










