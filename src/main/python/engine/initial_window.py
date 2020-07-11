# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property


class Ui_initilizer(object):

    def setupUi(self, initilizer):
        initilizer.setObjectName("initilizer")
        initilizer.resize(300, 400)
        initilizer.setMaximumSize(QtCore.QSize(300, 400))
        initilizer.setAutoFillBackground(False)
        initilizer.setStyleSheet("background-color: rgb(50, 54, 57);\n"
                                 "")
        self.pushButton = QtWidgets.QPushButton(initilizer)
        self.pushButton.setGeometry(QtCore.QRect(100, 320, 100, 32))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(89, 97, 106);\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "border-color:rgb(129, 142, 154);\n"
                                      "border-radius: 5px;\n"
                                      "alignment: center;\n"
                                      "")
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(initilizer)
        self.label.setGeometry(QtCore.QRect(80, 90, 150, 150))
        self.label.setStyleSheet("border-radius: 8px;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(-6)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(initilizer)
        self.label_2.setGeometry(QtCore.QRect(90, 260, 131, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "text-align: center;\n"
                                   "font-size: 15px;")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(initilizer)
        self.label_3.setGeometry(QtCore.QRect(70, 40, 181, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "text-align: center;\n"
                                   "font-size: 25px;")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(initilizer)
        self.label_4.setGeometry(QtCore.QRect(90, 241, 131, 20))
        self.label_4.setStyleSheet("color: rgba(255, 255, 255, 100);\n"
                                   "text-align: center;\n"
                                   "font-size: 10px;")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setWordWrap(False)
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(initilizer)
        QtCore.QMetaObject.connectSlotsByName(initilizer)

    def retranslateUi(self, initilizer):
        _translate = QtCore.QCoreApplication.translate
        initilizer.setWindowTitle(_translate("initilizer", "Colorizer"))
        self.pushButton.setText(_translate("initilizer", "Choose Folder"))
        self.label_2.setText(_translate("initilizer", "nutshellbox-public"))
        self.label_3.setText(_translate("initilizer", "Manga Colorizer"))
        self.label_4.setText(_translate("initilizer", "dev by"))
