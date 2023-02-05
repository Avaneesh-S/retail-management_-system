# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import*
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QLineEdit
from homepage1 import Ui_categories
from PyQt5.QtWidgets import QMessageBox
from tkinter import*
import time

class Ui_MainWindowlogin(object):
    def newwindow(self):

        import mysql.connector as ms
        mycon=ms.connect(host='localhost',user='root',passwd='adineesh123',database='project')
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        cur=mycon.cursor()
        cur.execute("select username from signup")
        rec=cur.fetchall()
        
        cur.execute("select password from signup where username like '{}' ".format(username))
        rec1=cur.fetchall()
        a=()
        b=()
        for i in rec:
            if username in i:
                a=i
        
        for j in rec1:
            if password in j:
                b=j
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        
        if username in  a and password in b:
            
            
            self.window=QtWidgets.QMainWindow()
            self.ui= Ui_categories()
            self.ui.setupUi(self.window)
            self.window.show()
            
           
            
            
            MainWindow.close()
           
            
            
           
            
        else:
            msg=QMessageBox()
            msg.setWindowTitle("INVALID")
            msg.setText("Invalid Username Or Password")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            
            msg.buttonClicked.connect(self.msgbuttonclick)
            
            x=msg.exec_()
            
        
            
    def msgbuttonclick(self):
        print("")

    def signuppage(self):
        
        import mysql.connector as ms

        root=Tk()
        root.title('Create Account')


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
            custname_label.grid(row=0,column=0,sticky=W)
            age_label=Label(root,text="Age")
            age_label.grid(row=1,column=0,sticky=W)
            dob_label=Label(root,text="Date Of Birth")
            dob_label.grid(row=2,column=0,sticky=W)
            emailid_label=Label(root,text="Email Id")
            emailid_label.grid(row=3,column=0,sticky=W)
            username=Label(root,text='Username').grid(row=4,column=0,sticky=W)
            password=Label(root,text='Password').grid(row=5,column=0,sticky=W)
            

            submit_btn=Button(root,text="Add record to database", command=submit)
            submit_btn.grid(row=6, column=0, columnspan=2,pady=10,padx=10,ipadx=75)

            query_btn=Button(root,text="Show records",command=display)
            query_btn.grid(row=7, column=0 ,columnspan=2,pady=10,padx=10,ipadx=75)




           

            root.mainloop()
        query()

    def showtext(self):
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        


    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 444)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 70, 71, 61))
        self.label_4.setStyleSheet("border-radius:40px")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("12th computer project/default.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 370, 121, 16))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 390, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.signuppage)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 250, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 150, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 210, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
    
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 21))
        self.menubar.setObjectName("menubar")
       
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.newwindow)
        self.pushButton_3.clicked.connect(self.showtext)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.label_2.setText(_translate("MainWindow", "USERNAME:"))
        self.label_3.setText(_translate("MainWindow", "PASSWORD:"))
        self.label.setText(_translate("MainWindow", "Dont\'t have an account?"))
        self.pushButton_2.setText(_translate("MainWindow", "SIGN UP"))
        self.pushButton_3.setText(_translate("MainWindow", "Show Text"))
        
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowlogin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
