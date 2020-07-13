from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from functools import partial
from PyQt5.QtCore import pyqtSlot
import threading
import os


class Ui_Form(object):

    def __init__(self, *args, images, colorizer):
        super(Ui_Form, self).__init__(*args)
        self.images = images
        self.title_image = self.images[0]
        self.colorizer = colorizer
        self.on_colorizing = False

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color: rgb(50, 54, 57);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 111, 31))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
                                 "font-size: 20px;")
        self.label.setObjectName("label")

        self.label_p = QtWidgets.QLabel(Form)
        self.label_p.setGeometry(QtCore.QRect(30, 530, 450, 31))
        self.label_p.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font-size: 10px;")
        self.label_p.setObjectName("label_p")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 112, 160))
        self.label_2.setMaximumSize(QtCore.QSize(112, 160))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.indicator = QtWidgets.QLabel(Form)
        self.indicator.setGeometry(QtCore.QRect(30, 290, 111, 31))
        self.indicator.setStyleSheet("color:rgb(255, 255, 255);\n"
                                 "font-size: 15px;")
        self.indicator.setObjectName("indicator")

        self.processed = QtWidgets.QLabel(Form)
        self.processed.setGeometry(QtCore.QRect(30, 320, 112, 160))
        self.processed.setMaximumSize(QtCore.QSize(112, 160))
        self.processed.setText("")
        self.processed.setScaledContents(True)
        self.processed.setObjectName("processed")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 30, 111, 31))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "font-size: 20px;")
        self.label_4.setObjectName("label_4")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(200, 69, 550, 440))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(25)
        self.gridLayout.setObjectName("gridLayout")
        self.set_images()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(180, 30, 21, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 540, 100, 32))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(89, 97, 106);\n"
                                        "border-style: solid;\n"
                                        "border-width: 1px;\n"
                                        "border-color:rgb(129, 142, 154);\n"
                                        "border-radius: 5px;\n"
                                        "alignment: center;\n"
                                        "")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.convert)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def convert(self):
        self.set_progress("Colorizing ...")
        if not self.on_colorizing:
            t = threading.Thread(target=self.colorizer.colorize, args=(self.title_image, self.images, self))
            t.start()
        else:
            self.set_progress('Busy')

    def set_images(self):
        size = 25 + (len(self.images) // 3) * 195
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(500, size))
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 533, size))
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 491, size))
        for i, img in enumerate(self.images):
            image = QtWidgets.QLabel(self.gridLayoutWidget)
            image.setMaximumSize(QtCore.QSize(112, 160))
            image.setText("")
            image.setPixmap(QtGui.QPixmap(img))
            image.setScaledContents(True)
            image.setObjectName(f"img{i}")
            image.mousePressEvent = partial(self.set_title_image, img)
            row, col = i // 3, i % 3
            self.gridLayout.addWidget(image, row, col, 1, 1)
        self.label_2.setPixmap(QtGui.QPixmap(self.title_image))

    def set_title_image(self, title_image: str, event: QtGui.QMouseEvent):
        self.title_image = title_image
        self.label_2.setPixmap(QtGui.QPixmap(self.title_image))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Title Image"))
        self.label_p.setText(_translate("Form", "Progress"))
        self.label_4.setText(_translate("Form", "Images"))
        self.indicator.setText(_translate("Form", "Generated"))
        self.pushButton_2.setText(_translate("Form", "Convert"))

    @pyqtSlot()
    def set_progress(self, text):
        _translate = QtCore.QCoreApplication.translate
        self.label_p.setText(f"Progress: {text}")
        self.label_p.adjustSize()
