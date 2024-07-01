import email
from tkinter import *
from tkinter import messagebox
from types import CoroutineType
import mysql.connector as sqltor
mycon=sqltor.connect(
        host='localhost',
        user='root',
        passwd='Mynameisayusha1!',
        database='miniproject')
csr=mycon.cursor()

def add_details():
    global sname
    global email
    global pno
    global street
    global apt
    global city 
    global state 
    global country 
    global pin

    sname=sname.get()
    email=email.get()
    pno=pno.get()
    street=street.get()
    apt=apt.get()
    city=city.get()
    state=state.get()
    country=country.get()
    pin=pin.get()

    #call get new sid

    q1="insert into seller values('{}','{}','{}')".format(sid,sname,email)
    q2="insert into s_address values('{}','{}','{}','{}','{}','{}')".format(sid,street,city,state,country,pin)

    try:
        csr.execute(q1)                
        csr.execute(q2)

        mycon.commit()
        messagebox.showinfo('Success',"Seller ID Created")
        x='Your Seller ID is'+ sid
        messagebox.showinfo('sid',x)
    except:
        messagebox.showinfo("Error","Cannot add given book data into Database")
    
    window.destroy()

def signuppage():
    global sname
    global email
    global pno
    global street
    global apt
    global city 
    global state 
    global country 
    global pin
    window=Tk()
    window.title('Seller')
 
    greet = Label(window, font = ('arial', 30, 'bold'), text = "Sign Up")
    greet.grid(row = 0,columnspan = 3)
 
    #----------name-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter name: ")
    L.grid(row = 2, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)
 
    sname=Entry(window,width=5,font =('arial', 15, 'bold'))
    sname.grid(row=2,column=3)
 
    #----------email-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter email: ")
    L.grid(row = 4, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 4, column = 2)
 
    email=Entry(window,width=5,font =('arial', 15, 'bold'))
    email.grid(row=4,column=3)
 
    #----------phone no-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Enter phone number: ")
    L.grid(row = 6, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 6, column = 2)
 
    pno=Entry(window,width=5,font =('arial', 15, 'bold'))
    pno.grid(row=6,column=3)

    #----------address details-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = " ADDRESS DETAILS ")
    L.grid(row = 8, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 8, column = 2)
 

    #----------street-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Street: ")
    L.grid(row = 10, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 10, column = 2)
 
    street=Entry(window,width=5,font =('arial', 15, 'bold'))
    street.grid(row=10,column=3)
    #----------apt-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Apt: ")
    L.grid(row = 12, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 12, column = 2)
 
    apt=Entry(window,width=5,font =('arial', 15, 'bold'))
    apt.grid(row=12,column=3)
    #----------city-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "City: ")
    L.grid(row = 14, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 14, column = 2)
 
    city=Entry(window,width=5,font =('arial', 15, 'bold'))
    city.grid(row=14,column=3)
    #----------state-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "State: ")
    L.grid(row = 16, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 16, column = 2)
 
    state=Entry(window,width=5,font =('arial', 15, 'bold'))
    state.grid(row=16,column=3)
    #----------country-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Country: ")
    L.grid(row = 18, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 18, column = 2)
 
    country=Entry(window,width=5,font =('arial', 15, 'bold'))
    country.grid(row=18,column=3)
   #----------country-------------------
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "Pin: ")
    L.grid(row = 20, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 20, column = 2)
 
    pin=Entry(window,width=5,font =('arial', 15, 'bold'))
    pin.grid(row=20,column=3)


    
    submitbtn=Button(window,text="Submit",command=add_details,bg="DodgerBlue2",fg="white",font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
        
    print("add")
    pass



def sloginpage():
    window = Tk()
    window.geometry('400x300')
    window.title('Login')
    f = ("Times bold", 14)
    L1 = Label(window, text="Seller ID")
    L1.pack( side = LEFT)
    E1 = Entry(window, bd =5)
    E1.pack(side = RIGHT)
    window.mainloop()


def sellerpage():
    window = Tk()
    window.geometry('400x300')
    window.title('Seller')

    sloginbtn=Button(window,text="Login",command=sloginpage,bg="DodgerBlue2",fg="white",font =f)
    sloginbtn.grid(row=3,columnspan=3)
 
    signupbtn=Button(window,text="Sign Up",command=signuppage,bg="DodgerBlue2",fg="white",font =f)
    signupbtn.grid(row=5,columnspan=3)


    window.mainloop()









