from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui
from PySide2 import QtXml
import glob
import os
from engine.initial_window import Ui_initilizer
from engine.colorize import Colorizer
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
        self.colorizer = colorizer

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory()
        images = [x for x in glob.glob(f"{folder}/*") if os.path.splitext(x)[-1].lower() in FORMATS]
        images = sorted(images)
        self.sub_window = SubWindow(images=images, colorizer=colorizer)
        self.sub_window.show()
        self.close()

    def set_image(self, url):
        self.label.setPixmap(QtGui.QPixmap(url))


if __name__ == '__main__':
    appctxt = ApplicationContext()
    colorizer = Colorizer(appctxt.get_resource('model/colorizer.h5'), appctxt.get_resource('model/upscaler.h5'))
    window = MainWindow()
    window.set_image(appctxt.get_resource('images/nutshellbox.png'))
    window.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
