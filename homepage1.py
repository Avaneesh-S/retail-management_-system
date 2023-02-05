# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from vegetablepage import Ui_MainWindow
from fruitpage2 import  Ui_MainWindow1
from cartpagewithtable import  Ui_MainWindow2
from beverages import Ui_MainWindow3
from PyQt5.QtWidgets import QMessageBox



class Ui_categories(object):
    def cartwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=  Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
    def vegwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
        
        
    def fruitwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.show()
       
    def beveragewindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def msgbuttonclick(self):
        print('')

    def search(self):
        f=open('vegetablenames.txt','r')
        vegename=f.read().split()
        
        
        g=open('fruitnames.txt','r')
        fruitname=g.read().split()
        searchvalue=self.searchbar.text()
        
        if searchvalue in vegename:
           
            self.windowv=QtWidgets.QMainWindow()
            self.ui= Ui_MainWindow()
            self.ui.setupUi(self.windowv)
            self.windowv.show()
            '''
            categories.close()'''
        elif searchvalue in fruitname:
            
            self.windowf=QtWidgets.QMainWindow()
            self.ui= Ui_MainWindow1()
            self.ui.setupUi(self.windowf)
            self.windowf.show()
            '''
            categories.close()'''
        
            
        else:
            msg=QMessageBox()
            msg.setWindowTitle("INVALID")
            msg.setText("No Items Match Your Search")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            
            msg.buttonClicked.connect(self.msgbuttonclick)
            
            x=msg.exec_()


    
            
            
    def setupUi(self, categories):
        
        categories.setObjectName("categories")
        categories.resize(1381, 1165)
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
        categories.setPalette(palette)
        categories.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(categories)
        self.centralwidget.setObjectName("centralwidget")
        self.buyoffers = QtWidgets.QLabel(self.centralwidget)
        self.buyoffers.setGeometry(QtCore.QRect(10, 80, 1331, 281))
        self.buyoffers.setText("")
        self.buyoffers.setPixmap(QtGui.QPixmap("12th computer project/mainpic.PNG"))
        
        self.buyoffers.setScaledContents(True)
        self.buyoffers.setObjectName("buyoffers")
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setGeometry(QtCore.QRect(390, 10, 51, 31))
        self.searchbutton.setObjectName("searchbutton")
        self.searchbutton.clicked.connect(self.search)
        self.cart = QtWidgets.QPushButton(self.centralwidget)
        self.cart.setGeometry(QtCore.QRect(1160, 10, 181, 51))
        self.cart.clicked.connect(self.cartwindow)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cart.setFont(font)
        self.cart.setObjectName("cart")
        self.searchbar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(110, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchbar.setFont(font)
        self.searchbar.setObjectName("searchbar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 420, 671, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("12th computer project/pic2.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 380, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1340, 200, 21, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 420, 681, 231))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("12th computer project/pic3.PNG"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(890, 380, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setObjectName("label_4")
        categories.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(categories)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1381, 21))
        self.menubar.setObjectName("menubar")
        self.menuCATEGORIES = QtWidgets.QMenu(self.menubar)
        self.menuCATEGORIES.setObjectName("menuCATEGORIES")
        self.menuOFFERS = QtWidgets.QMenu(self.menubar)
        self.menuOFFERS.setObjectName("menuOFFERS")
        categories.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(categories)
        self.statusbar.setObjectName("statusbar")
        categories.setStatusBar(self.statusbar)
        self.actionvegetable = QtWidgets.QAction(categories)
        self.actionvegetable.setObjectName("actionvegetable")
        self.actionfruits = QtWidgets.QAction(categories)
        self.actionfruits.setObjectName("actionfruits")
        self.actionbeverages = QtWidgets.QAction(categories)
        self.actionbeverages.setObjectName("actionbeverages")
        self.actionbakery_and_diary = QtWidgets.QAction(categories)
        self.actionbakery_and_diary.setObjectName("actionbakery_and_diary")
        self.actiononion = QtWidgets.QAction(categories)
        self.actiononion.setObjectName("actiononion")
        self.actioncapsicum = QtWidgets.QAction(categories)
        self.actioncapsicum.setObjectName("actioncapsicum")
        self.actionpotato = QtWidgets.QAction(categories)
        self.actionpotato.setObjectName("actionpotato")
        self.actiontomato = QtWidgets.QAction(categories)
        self.actiontomato.setObjectName("actiontomato")
        self.actionfoodgrains = QtWidgets.QAction(categories)
        self.actionfoodgrains.setObjectName("actionfoodgrains")
        self.menuCATEGORIES.addAction(self.actionvegetable)
        self.menuCATEGORIES.addAction(self.actionfruits)
        self.menuCATEGORIES.addAction(self.actionbeverages)
        self.menuCATEGORIES.addAction(self.actionbakery_and_diary)
        self.menuCATEGORIES.addAction(self.actionfoodgrains)
        self.menubar.addAction(self.menuCATEGORIES.menuAction())
        self.menubar.addAction(self.menuOFFERS.menuAction())

        self.retranslateUi(categories)
        QtCore.QMetaObject.connectSlotsByName(categories)
        self.pushButton.clicked.connect(self.changepicture)
        
        
    def retranslateUi(self, categories):
        _translate = QtCore.QCoreApplication.translate
        categories.setWindowTitle(_translate("categories", "MainWindow"))
        self.searchbutton.setText(_translate("categories", "search"))
        self.cart.setText(_translate("categories", "My Items"))
        self.label_2.setText(_translate("categories", "  FRUITS AND VEGETABLES CORNER"))
        self.pushButton.setText(_translate("categories", ">"))
        self.label_4.setText(_translate("categories", "BEVERAGES"))
        self.menuCATEGORIES.setTitle(_translate("categories", "SHOP BY CATEGORIES"))
        self.menuOFFERS.setTitle(_translate("categories", "OFFERS"))
        self.actionvegetable.setText(_translate("categories", "vegetable"))
        self.actionvegetable.triggered.connect(self.vegwindow)
        self.actionfruits.setText(_translate("categories", "fruits"))
        self.actionfruits.triggered.connect(self.fruitwindow)
        self.actionbeverages.setText(_translate("categories", "beverages"))
        self.actionbakery_and_diary.setText(_translate("categories", "bakery and diary"))
        self.actionbeverages.triggered.connect(self.beveragewindow)
        self.actiononion.setText(_translate("categories", "onion"))
        self.actioncapsicum.setText(_translate("categories", "capsicum"))
        self.actionpotato.setText(_translate("categories", "potato"))
        self.actiontomato.setText(_translate("categories", "tomato"))
        self.actionfoodgrains.setText(_translate("categories", "foodgrains"))
        

    def changepicture(self):
        self.buyoffers.setPixmap(QtGui.QPixmap("12th computer project/offers5.jpg"))
        
      
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    categories = QtWidgets.QMainWindow()
    ui = Ui_categories()
    ui.setupUi(categories)
    categories.show()
    sys.exit(app.exec_())
