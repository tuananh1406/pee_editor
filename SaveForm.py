import sys, os, cv2, configparser, glob, shutil
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from datetime import datetime
import variable

"""____________________________ Lớp Xứ Lý Chính ______________________________"""
class SaveForm(QtWidgets.QDialog):

    def __init__(self, path_project, type):
        # Load UI
        super(SaveForm, self).__init__()
        uic.loadUi(path_project + "/SaveForm.ui", self)
        self.setWindowTitle("Save as option...")
        self.choosePath_save.clicked.connect(self.choose_saveas_path)
        if type == "Only":
            self.seoInput_name.setChecked(False)
            self.seoInput_name.setDisabled(True)
        else:
            self.seoInput_name.setChecked(True)
            self.seoInput_name.setDisabled(False)
        self.exec_()

    def choose_saveas_path(self):
        if self.checkMD5_code.isChecked() == True:
            variable.md5_code = True
        else:
            variable.md5_code = False

        if self.seoInput_name.isChecked() == True:
            variable.seo_name = True
        else:
            variable.seo_name = False

        if self.pixel500.isChecked() == True:
            variable.pixel_value = 500
        if self.pixel720.isChecked() == True:
            variable.pixel_value = 720
        if self.pixel1000.isChecked() == True:
            variable.pixel_value = 1000
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SaveForm()
    sys.exit(app.exec_())