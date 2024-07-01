from tkinter import *
from tkinter import messagebox
import mysql.connector as sqltor
mycon=sqltor.connect(
        host='localhost',
        user='root',
        passwd='Mynameisayusha1!',
        database='miniproject')
csr=mycon.cursor()
#-----------------------------customer functions-----------------------
def view_packaged():
    def showpd():
        global pid
        pid=id.get()
        q="select distict(S_ID),name,email from seller natural join orders_from where P_ID='{}'".format(pid)
        try:
            csr.execute(q)
            i=0
            e=Label(window,width=10,text='Seller id',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=0)
            e=Label(window,width=10,text=' Seller Name',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=1)
            e=Label(window,width=10,text='Email',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=2)
            i=5
            for package in csr:
                e = Entry(window, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, package[j])
                i+=1
        except:
            messagebox.showinfo("Error","Cannot Fetch data.")
        
        print("view")
        pass
    window = Tk()
    window.geometry('400x300')
    window.title('Customer')
    f = ("Times bold", 14)
    greet = Label(window, font = ('arial', 30, 'bold'), text = "View Package Details")
    greet.grid(row = 0,columnspan = 3)

    L=Label(window,text='Enter the package id:')
    L.grid(row = 2, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)
 
    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)
 
    submitbtn=Button(window,text="Submit",fg='blue',command=showpd,font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)

def view_sellerd():
    def showindowd():
        global pid
        pid=id.get()
        q="select * from package where P_ID='{}'".format(pid)
        try:
            csr.execute(q)
            i=0
            e=Label(window,width=10,text='Package id',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=0)
            e=Label(window,width=10,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=1)
            e=Label(window,width=10,text='Weight',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=2)
            e=Label(window,width=10,text='Size',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=3)
            e=Label(window,width=10,text='Category',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=4)
            e=Label(window,width=10,text='Fragile?',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=5)
            e=Label(window,width=10,text='Description',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=6)
            i=5
            for package in csr:
                for j in (len(package)):
                    e = Entry(window, width=10, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, package[j])
                i+=1
        except:
            messagebox.showinfo("Error","Cannot Fetch data.")
        
    window = Tk()
    window.geometry('400x300')
    window.title('Customer')
    greet = Label(window, font = ('arial', 30, 'bold'), text = "View Seller Details")
    greet.grid(row = 0,columnspan = 3)
   
    L=Label(window,text='Enter package id: ')
    L.grid(row = 2, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)
 
    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)
 
    submitbtn=Button(window,text="Submit",fg='blue',command=showindowd,font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)

def track_shipment():
    def showtracking():
        global pid
        pid=id.get()
        q="call track_shipment('{}')".format(pid)
        try:
            csr.execute(q)
            i=0
            e=Label(window,width=10,text='Package ID',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=0)
            e=Label(window,width=10,text=' Seller ID',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=1)
            e=Label(window,width=10,text='Order Date',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=2)
            e=Label(window,width=10,text='Ship Date',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=3)
            e=Label(window,width=10,text='Status',borderwidth=2, relief='ridge',anchor='w',bg='blue')
            e.grid(row=4,column=4)
            i=5
            for package in csr:
                e = Entry(window, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, package[j])
                i+=1
        except:
            messagebox.showinfo("Error","Cannot Fetch data.")
        
        print("view")
        pass
    window = Tk()
    window.geometry('400x300')
    window.title('Customer')
    greet = Label(window, font = ('arial', 30, 'bold'), text = "Track Shipment")
    greet.grid(row = 0,columnspan = 3)

    L=Label(window,text='Enter the package id')
    L.grid(row = 2, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)
 
    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)
 

    submitbtn=Button(window,text="Submit",fg='blue',command=showtracking,font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)

  

#-----------------------------------customer menu after login-------------------------------------
def customermenu():
    global cid
    cid=id.get()

    window = Tk()
    window.geometry('400x300')
    window.title('Customer')
    f = ("Times bold", 14)

    viewpackagedbtn=Button(window,text="View Package Details",command=view_packaged,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
    viewpackagedbtn.grid(row=3,columnspan=3)
 
    viewindowellerdbtn=Button(window,text="View Seller Details",command=view_sellerd,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
    viewindowellerdbtn.grid(row=5,columnspan=3)
 
    trackbtn=Button(window,text="Track Shipment",command=track_shipment,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
    trackbtn.grid(row=7,columnspan=3)
    window.mainloop()


#----------------------------------------customer login---------------------------------------------
def customerlogin():
    window = Tk()
    window.geometry('400x300')
    window.title('Customer')
    f = ("Times bold", 14)
    global id
    L=Label(window,text='Enter your customer id')
    L.grid(row = 2, column = 1)
 
    L = Label(window, font = ('arial', 15, 'bold'), text = "   ")
    L.grid(row = 2, column = 2)
 
    id=Entry(window,width=5,font =('arial', 15, 'bold'))
    id.grid(row=2,column=3)
 

    submitbtn=Button(window,text="Submit",fg='blue',command=customermenu,font = ('arial', 15, 'bold'))
    submitbtn.grid(row=8,columnspan=3)
    
    window.mainloop()