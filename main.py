import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
import glob
import os
from engine.initial_window import Ui_initilizer
from engine.list_window import Ui_Form
FORMATS = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')


class SubWindow(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self, *args, obj=None, **kwargs):
        super(SubWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_initilizer):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_folder)
        self.sub_window = None

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory()
        images = [x for x in glob.glob(f"{folder}/*") if os.path.splitext(x)[-1].lower() in FORMATS]
        images = sorted(images)
        self.sub_window = SubWindow(images=images)
        self.sub_window.show()
        self.close()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
