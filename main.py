#-------------MADE BY HoaxSnowden---------------#


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import hashlib
import datetime
from PyQt5.QtWidgets import QMessageBox

conn = sqlite3.connect("users.db")
c = conn.cursor()

def createTable():
    c.execute(
        "CREATE TABLE IF NOT EXISTS usersLog(firstName TEXT, lastName TEXT, userName TEXT, userPass TEXT, dateRegistered TEXT)"
    )


def dataEntry(firstName, lastName, userName, userPass, dateRegistered):
    c.execute(
        "INSERT INTO usersLog (firstName, lastName, userName, userPass, dateRegistered) VALUES (?, ?, ?, ?, ?)",
        (firstName, lastName, userName, userPass, dateRegistered),
    )
    conn.commit()

def selectUserFromDB(userName, userPass):
    c.execute(
        "SELECT * FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    for row in c.fetchall():
        return row[2]


def selectPassFromDB(userName, userPass):
    c.execute(
        "SELECT * FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    for row in c.fetchall():
        return row[3]

def selectFirstFromDB(userName, userPass):
    c.execute(
        "SELECT * FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    for row in c.fetchall():
        return row[0]


def selectLastFromDB(userName, userPass):
    c.execute(
        "SELECT * FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    for row in c.fetchall():
        return row[1]

def selectDateFromDB(userName, userPass):
    c.execute(
        "SELECT * FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    for row in c.fetchall():
        return row[4]

def delAccount(userName, userPass):
    c.execute(
        "DELETE FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    conn.commit()


def renameAccount(userName, userPass, newUserName):
    c.execute(
        "UPDATE usersLog SET userName = (?) WHERE userName = (?) AND userPass = (?)",
        (newUserName, userName, userPass),
    )
    conn.commit()


def changePass(userName, userPass, newPass):
    c.execute(
        "UPDATE usersLog SET userPass = (?) WHERE userName = (?) AND userPass = (?)",
        (newPass, userName, userPass),
    )
    conn.commit()

createTable()

class loginWin(object):
    def __init__(self, win):
        self.win = win
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QToolButton{\n"
"    background-color: rgb(114, 188,255);\n"
"    border-radius: 50px;\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgba(0,0,25,150);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: none;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: white;\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"     border-bottom: 1px solid rgb(114, 188,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(10,10,10,100);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 188,255);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_2{\n"
"    background-color: none;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"    color: rgb(114, 188,255);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(350, 80, 101, 101))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(80, 80))
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, -90, 1121, 761))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/bg.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 130, 301, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 130, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 200, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 330, 261, 23))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2.raise_()
        self.frame.raise_()
        self.toolButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.loginme)
        self.pushButton_2.clicked.connect(self.registerhere)

    def loginme(self):
        uname = self.lineEdit.text()
        upass = self.lineEdit_2.text()
        upass = hashlib.sha512(upass.encode()).hexdigest()
        if uname == selectUserFromDB(uname, upass) and upass == selectPassFromDB(uname, upass):
            self.infowin = QtWidgets.QMainWindow()
            self.ui = infoWin(self.infowin, uname, upass)
            self.ui.setupUi(self.infowin)
            self.infowin.show()
            self.win.hide()
        else:
            self.showError()
    def showError(self):
        msg = QMessageBox()
        msg.setWindowTitle("Login Error")
        msg.setText("Account doesn't exists in the database")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()
    def registerhere(self):
        self.regwin = QtWidgets.QMainWindow()
        self.ui = registerWin(self.regwin)
        self.ui.setupUi(self.regwin)
        self.regwin.show()
        self.win.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Prompt"))
        self.label.setText(_translate("MainWindow", "Login Form"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter your Password"))
        self.pushButton.setText(_translate("MainWindow", "Login!"))
        self.pushButton_2.setText(_translate("MainWindow", "Doesn\'t have an account yet? Register Here"))



class registerWin(object):
    def __init__(self, win):
        self.win = win
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
"    font-family: \"Berlin Sans FB Demi\";\n"
"    color: white;\n"
"}\n"
"\n"
"QToolButton{\n"
"    background-color: rgb(114, 188,255);\n"
"    border-radius: 50px;\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgba(0,0,25,150);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: none;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: white;\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-bottom: 1px solid rgb(114, 188,255);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(10,10,10,100);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 188,255);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_2{\n"
"    background-color: none;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"    color: rgb(114, 188,255);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-170, 0, 1121, 661))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/bg.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 100, 301, 431))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 340, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 390, 261, 23))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 140, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 190, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 240, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 290, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(350, 50, 101, 101))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(80, 80))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton_2.clicked.connect(self.loginhere)
        self.pushButton.clicked.connect(self.registerme)

    def registerme(self):
        fname = self.lineEdit.text()
        lname = self.lineEdit_2.text()
        uname = self.lineEdit_3.text()
        upass = self.lineEdit_4.text()
        upass = hashlib.sha512(upass.encode()).hexdigest()
        if fname == "" or lname == "" or uname == "" or upass == "":
            self.showError3()
        elif uname == selectUserFromDB(uname, upass) or fname == selectFirstFromDB(uname, upass) or lname == selectLastFromDB(uname, upass) or upass == selectPassFromDB(uname, upass):
            self.showError2()
        elif uname == selectUserFromDB(uname, upass) and upass == selectPassFromDB(uname, upass):
            self.showError2()
        elif self.lineEdit_4.text() == self.lineEdit_5.text():
            dateReged = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            dataEntry(fname, lname, uname, upass, dateReged)
            self.showSuccess()
        else:
            self.showError()

    def showError2(self):
        msg = QMessageBox()
        msg.setWindowTitle("Registry Error")
        msg.setText("Account is in the database already")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()

    def showError3(self):
        msg = QMessageBox()
        msg.setWindowTitle("Registry Error")
        msg.setText("All forms must be answered! Thanks")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()

    def showSuccess(self):
        msg = QMessageBox()
        msg.setWindowTitle("Registry Success")
        msg.setText("You can now login!")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()

    def showError(self):
        msg = QMessageBox()
        msg.setWindowTitle("Registry Error")
        msg.setText("The password you entered are not the same")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()

    def loginhere(self):
        self.loginwin = QtWidgets.QMainWindow()
        self.ui = loginWin(self.loginwin)
        self.ui.setupUi(self.loginwin)
        self.loginwin.show()
        self.win.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registry Prompt"))
        self.label.setText(_translate("MainWindow", "Registry Form"))
        self.pushButton.setText(_translate("MainWindow", "Register!"))
        self.pushButton_2.setText(_translate("MainWindow", "You already have an account? Login here"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your first name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter your last name"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter your username"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Enter your password again"))

class infoWin(object):
    def __init__(self, win, username, userpass):
        self.win = win
        self.username = username
        self.userpass = userpass
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"QToolButton{\n"
"    background-color: rgb(114, 188,255);\n"
"    border-radius: 50px;\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgba(0,0,25,150);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: none;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: white;\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    color: white;\n"
"    border-bottom: 1px solid rgb(114, 188,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(10,10,10,100);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 188,255);\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(50, 450, 301, 121))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 70, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(0, 40, 301, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(50, 30, 301, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 120, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 70, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(0, 50, 301, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(560, 30, 101, 101))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(80, 80))
        self.toolButton.setObjectName("toolButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(50, 210, 301, 231))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 180, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 80, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(30, 130, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(0, 50, 301, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(460, 80, 301, 441))
        self.frame.setMinimumSize(QtCore.QSize(301, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 130, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 50, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 200, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 270, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 340, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-40, -30, 1761, 1011))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/bg.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.toolButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.logout)
        self.pushButton_2.clicked.connect(self.changeUser)
        self.pushButton_3.clicked.connect(self.changePass)
        self.pushButton_4.clicked.connect(self.delAcc)

        self.lineEdit.setText(selectFirstFromDB(self.username, self.userpass))
        self.lineEdit_2.setText(selectLastFromDB(self.username, self.userpass))
        self.lineEdit_3.setText(self.username)
        self.lineEdit_4.setText(selectDateFromDB(self.username, self.userpass))

    def changeUser(self):
        newuser = self.lineEdit_5.text()
        renameAccount(self.username, self.userpass, newuser)
        self.showReSuc()
        self.infowin = QtWidgets.QMainWindow()
        self.ui = infoWin(self.infowin, newuser, self.userpass)
        self.ui.setupUi(self.infowin)
        self.infowin.show()
        self.win.hide()

    def changePass(self):
        newpass = self.lineEdit_6.text()
        newpassVerify = self.lineEdit_7.text()
        if newpass == newpassVerify:
            newpass = hashlib.sha512(newpass.encode()).hexdigest()
            changePass(self.username, self.userpass, newpass)
            self.showCPSuc()
            self.infowin = QtWidgets.QMainWindow()
            self.ui = infoWin(self.infowin, self.username, newpass)
            self.ui.setupUi(self.infowin)
            self.infowin.show()
            self.win.hide()
        else: 
            self.showErPas()

    def delAcc(self):
        self.popupDel()
        delAccount(self.username, self.userpass)
        self.logout()

    def logout(self):
        self.loginwin = QtWidgets.QMainWindow()
        self.ui = loginWin(self.loginwin)
        self.ui.setupUi(self.loginwin)
        self.loginwin.show()
        self.win.hide()

    def popupDel(self):
        msg = QMessageBox()
        msg.setWindowTitle("Account is Deleted!")
        msg.setText("Your account is deleted successfully")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()

    def showReSuc(self):
        msg = QMessageBox()
        msg.setWindowTitle("Renamed Successfully")
        msg.setText("Your account is renamed successfully")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()

    def showCPSuc(self):
        msg = QMessageBox()
        msg.setWindowTitle("Password Changed!")
        msg.setText("Your password is changed successfully")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()

    def showErPas(self):
        msg = QMessageBox()
        msg.setWindowTitle("Password Change Error")
        msg.setText("The two password you entered is not the same")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QtGui.QIcon('images/user.png'))
        x = msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Prompt"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete Now!"))
        self.label_9.setText(_translate("MainWindow", "Delete this account?"))
        self.label_12.setText(_translate("MainWindow", "This will account will be deleted forever"))
        self.pushButton_2.setText(_translate("MainWindow", "Change Username"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "New Username"))
        self.label_7.setText(_translate("MainWindow", "Change your username ?"))
        self.label_10.setText(_translate("MainWindow", "This username will be changed forever"))
        self.pushButton_3.setText(_translate("MainWindow", "Change Password"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Enter New Password"))
        self.label_8.setText(_translate("MainWindow", "Change your password ?"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Enter New Password Again"))
        self.label_11.setText(_translate("MainWindow", "This password will be changed, make sure to remember it"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.label.setText(_translate("MainWindow", "Your Information"))
        self.label_3.setText(_translate("MainWindow", "First Name:"))
        self.label_4.setText(_translate("MainWindow", "Last Name:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.label_5.setText(_translate("MainWindow", "Username:"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "Date Registered:"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Date Registered"))
        self.pushButton.setText(_translate("MainWindow", "Logout"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = registerWin(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
