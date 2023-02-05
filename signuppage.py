from tkinter import*
import mysql.connector as ms

root=Tk()
root.title('customer database')


def submit():
    mycon=ms.connect(host='localhost',user='root',password='adineesh123',database='project')
    cur=mycon.cursor()
    
    a=customername.get()
    b=emailid.get()
    c=username1.get()
    d=password1.get()
    e=age.get()
    f=dob.get()
    cur.execute("insert into signup values('{}','{}','{}','{}','{}','{}')".format(a,e,f,b,c,d))
    mycon.commit()

    print("record added")
     
    customername.delete(0,END)
    age.delete(0,END)
    dob.delete(0,END)
    emailid.delete(0,END)
    username1.delete(0,END)
    password1.delete(0,END)
def display():
    mycon=ms.connect(host='localhost',user='root',password='adineesh123',database='project')
    cur=mycon.cursor()
    cur.execute("select*from signup")
    records=cur.fetchall()
    print(records)
    

def query():
    

    

    global customername,emailid,username1,password1,age,dob 
    customername=Entry(root, width=30)
    customername.grid(row=0, column=1, padx=20)
    
    age=Entry(root,width=30)
    age.grid(row=1, column=1)
    
    dob=Entry(root, width=30)
    dob.grid(row=2,column=1)
    
    emailid=Entry(root,width=30)
    emailid.grid(row=3,column=1)

    username1=Entry(root,width=30)
    username1.grid(row=4,column=1)
    password1=Entry(root,width=30)
    password1.grid(row=5,column=1)
    


    custname_label=Label(root, text="Name")
    custname_label.grid(row=0,column=0)
    age_label=Label(root,text="Age")
    age_label.grid(row=1,column=0)
    dob_label=Label(root,text="DateOfBirth")
    dob_label.grid(row=2,column=0)
    emailid_label=Label(root,text="EmailId")
    emailid_label.grid(row=3,column=0)
    username=Label(root,text='Username').grid(row=4,column=0)
    password=Label(root,text='Password').grid(row=5,column=0)
    

    submit_btn=Button(root,text="add record to database", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2,pady=10,padx=10,ipadx=137)

    query_btn=Button(root,text="Show records",command=display)
    query_btn.grid(row=7, column=0 ,columnspan=2,pady=10,padx=10,ipadx=137)




   

    root.mainloop()
query()
