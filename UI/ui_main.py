# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzhbIGI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient, QMovie)
from PySide2.QtWidgets import *
import pyglet
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 0);")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Label1 Create
        self.label_FR = QtWidgets.QLabel(self.centralwidget)
        self.label_FR.setGeometry(QtCore.QRect(-60, 280, 20, 20))
        self.label_FR.setMinimumSize(QtCore.QSize(1500, 550))
        self.label_FR.setMaximumSize(QtCore.QSize(1500, 550))
        self.label_FR.setObjectName("lb1")
        MainWindow.setCentralWidget(self.centralwidget)

        # Push Button1
        self.pushButton_FR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_FR.setGeometry(QtCore.QRect(152, 820, 380, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_FR.setFont(font)
        self.pushButton_FR.setCheckable(False)
        self.pushButton_FR.setEnabled(True)
        self.pushButton_FR.setObjectName("pushButton_FR")
        self.pushButton_FR.clicked.connect(self.on_click)

        # Push Button2
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(815, 815, 380, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        # self.pushButton_login.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.364, x2:0.995025, y2:0.784, stop:0 rgba(20, 15, 186, 255), stop:1 rgba(0, 255, 255, 255));\n"
        # "color: rgb(0, 0, 0);")
        self.pushButton_login.setCheckable(False)
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login.setEnabled(True)
        self.pushButton_login.setStyleSheet("QPushButton::hover"
                                            "{"
                                            "background-color: #38ACEC;"
                                            "color: black;"
                                            "}")
        self.pushButton_FR.setStyleSheet("QPushButton::hover"
                                         "{"
                                         "background-color : #38ACEC;"
                                         "color: black;"
                                         "}")
        self.pushButton_login.clicked.connect(self.on_click1)


        # Title
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(565, 30, 291, 131))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(0, 255, 255);\n"
                                       "background-color: rgb(0, 0, 0);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName(u"label_title")

        # Subtitle
        self.label_subtitle = QtWidgets.QLabel(self.centralwidget)
        self.label_subtitle.setGeometry(QtCore.QRect(520, 150, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_subtitle.setFont(font)
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setWordWrap(False)
        self.label_subtitle.setObjectName("label_subtitle")

        #Description
        self.label_description = QtWidgets.QLabel(self.centralwidget)
        self.label_description.setGeometry(QtCore.QRect(485, 190, 470, 120))
        font = QtGui.QFont()
        font.setFamily("Coursera")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: white;\n"
                                       "background-color: rgb(0, 0, 0);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName(u"label_description")

        music = pyglet.resource.media("Authentication.wav")
        music.play()

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        # Loading the GIF
        self.movie_FR = QMovie("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\gif\\Authentication2.gif")
        self.label_FR.setMovie(self.movie_FR)

        self.startAnimation()

        # Start Animation

    def startAnimation(self):
        self.movie_FR.start()

        # Stop Animation(According to need)

    def stopAnimation(self):
        self.movie_FR.stop()
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "FrontWindow"))
        self.label_title.setText(QtCore.QCoreApplication.translate("MainWindow", "IDA"))
        self.pushButton_FR.setText(QtCore.QCoreApplication.translate("MainWindow", "FACE  RECOGNITION"))
        self.label_subtitle.setText(QtCore.QCoreApplication.translate("MainWindow", "YOUR OWN VIRTUAL ASSISTANT"))
        self.label_description.setText(QtCore.QCoreApplication.translate("MainWindow", "Welcome to our application.\nHello, I am IDA, your own personal assistant.\nDeveloped By Group 3.\nFor accessing me,\n kindly login through Face Recognition or\n you can also login through Username and Password.\nThankyou. Have a good day."))
        self.pushButton_login.setText(QtCore.QCoreApplication.translate("MainWindow", "LOGIN/REGISTER"))

    def on_click(self):
        os.system("python C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\app_gui.py")

    def on_click1(self):
        os.system("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\Login_register\\login-register.py")