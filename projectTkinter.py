import mysql.connector as ms
from tabulate import tabulate
from tkinter import*
import random

mycon=ms.connect(host='localhost',user='root',passwd='adineesh123',database='project')
cur=mycon.cursor()
def tkinterwindow():
    root=Tk()
    root.title("LOGIN")
    root.geometry('350x100')

    label=Label(root,text="Username:").grid(row=0,column=0)
    label0=Label(root,text="Password:").grid(row=1,column=0)
    e=Entry(root,width=40).grid(row=0,column=1)
    e1=Entry(root,width=40).grid(row=1,column=1)


      
        
    def opennewwindow1():
        global newWindow1
        newWindow1=Toplevel(root)
        newWindow1.title("WELCOME")
        newWindow1.geometry('600x500')
        global categories
        categories=StringVar()
        categories.set(' shop by category')
        cur.execute("select shopbycategory from categories")
        rec=cur.fetchall()
        drop=OptionMenu(newWindow1,categories,*rec).grid(row=2,column=3)
        buttonitem=Button(newWindow1,text="click here when done",command=opennewwindow2).grid(row=3,column=3)
        cartbutton=Button(newWindow1,text='CART',command=displaycart).grid(row=6,column=3)
        
    def opennewwindow2():
        
        if categories.get()=="('vegetables',)":
            global newWindow2
            newWindow2=Toplevel(root)
            newWindow2.title("WELCOME")
            sno=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
            cur.execute("select productname from vegetables")
            rec=cur.fetchall()
            global vegetable,vegetable1
            vegetable=StringVar()
            vegetable.set("choose an item")
            vegetable1=StringVar()
            vegetable1.set("choose quantity")
        
            dropitem=OptionMenu(newWindow2,vegetable,*rec).pack()
            dropsno=OptionMenu(newWindow2,vegetable1,*sno).pack()
            buttonitem=Button(newWindow2,text="click here to add to cart",command=addtocart).pack()
        '''elif categories.get=="('fruits',)":
            global newWindow1
            newWindow1=Toplevel(root)
            newWindow1.title("WELCOME")
            sno=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
            cur.execute("select productname from fruits")
            rec=cur.fetchall()
            global vegetable,vegetable1
            vegetable=StringVar()
            vegetable.set("choose an item")
            vegetable1=StringVar()
            vegetable1.set("choose quantity")
        
            dropitem=OptionMenu(newWindow1,vegetable,*rec).pack()
            dropsno=OptionMenu(newWindow1,vegetable1,*sno).pack()
            buttonitem=Button(newWindow1,text="click here to add to cart",command=addtocart).pack()
    '''        
    def addtocart():
        global cart,cartitem
        cart=[]
        cart.append(vegetable.get())
        cartitemnum=[]
        cartitemnum.append(vegetable1.get())
        labeldisplay=Label(newWindow2,text="item has been added to cart").pack()
    def displaycart():
        cartWindow=Toplevel(root)
        cartWindow.title("CART")
        cart1=[]
        
        for i in cart:
            c=''
            for j in i:
                if j.isalpha():
                    c=c+j
            cart1.append(c)
                    
        for i in range(len(cart1)):
            labelcart=Label(cartWindow,text=cart1[i]).grid(row=i,column=0)

        
        
        
    button1=Button(root,text="LOGIN",command=opennewwindow1,width=5,padx=10,pady=10).grid(row=3,column=1)
    '''button2=Button(root,text="SIGN UP",command=signup,width=3,height=1,padx=10,pady=10).pack()'''




    root.mainloop()
