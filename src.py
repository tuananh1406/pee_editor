from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QSizePolicy, QTreeWidgetItem
from PyQt5.QtGui import QPixmap, QImage, QIntValidator, QIcon
from PIL import Image
import numpy as np
import cv2, glob, shutil, sys, os, base64

class variable:
    # coding=utf-8
    md5_code = True
    seo_name = True
    pixel_value = 500

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 179)
        Form.setStyleSheet("")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 161))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"  color: #333333;\n"
"  background-color: #e0e0e0;\n"
"  border-radius: 5px;\n"
"  font-weight: bold;\n"
"  font-size: 12px;\n"
"}\n"
"\n"
"QGroupBox > * {\n"
"  color: #333333;\n"
"  background-color: transparent;\n"
"}")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.seoInput_name = QtWidgets.QCheckBox(self.groupBox)
        self.seoInput_name.setGeometry(QtCore.QRect(230, 30, 141, 20))
        self.seoInput_name.setStyleSheet("QCheckBox {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"  color: #828282;\n"
"  background-color: #bdbdbd;\n"
"  border: none;\n"
"}")
        self.seoInput_name.setChecked(True)
        self.seoInput_name.setObjectName("seoInput_name")
        self.checkMD5_code = QtWidgets.QCheckBox(self.groupBox)
        self.checkMD5_code.setGeometry(QtCore.QRect(20, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.checkMD5_code.setFont(font)
        self.checkMD5_code.setStyleSheet("QCheckBox {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"  color: #828282;\n"
"  background-color: #bdbdbd;\n"
"  border: none;\n"
"}")
        self.checkMD5_code.setChecked(True)
        self.checkMD5_code.setObjectName("checkMD5_code")
        self.pixel500 = QtWidgets.QRadioButton(self.groupBox)
        self.pixel500.setGeometry(QtCore.QRect(20, 70, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pixel500.setFont(font)
        self.pixel500.setStyleSheet("QRadioButton {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  color: #828282;\n"
"  background-color: #bdbdbd;\n"
"  border: none;\n"
"}")
        self.pixel500.setChecked(True)
        self.pixel500.setObjectName("pixel500")
        self.pixel720 = QtWidgets.QRadioButton(self.groupBox)
        self.pixel720.setGeometry(QtCore.QRect(140, 70, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pixel720.setFont(font)
        self.pixel720.setStyleSheet("QRadioButton {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  color: #828282;\n"
"  background-color: #bdbdbd;\n"
"  border: none;\n"
"}")
        self.pixel720.setObjectName("pixel720")
        self.pixel1000 = QtWidgets.QRadioButton(self.groupBox)
        self.pixel1000.setGeometry(QtCore.QRect(260, 70, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pixel1000.setFont(font)
        self.pixel1000.setStyleSheet("QRadioButton {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  color: #828282;\n"
"  background-color: #bdbdbd;\n"
"  border: none;\n"
"}")
        self.pixel1000.setObjectName("pixel1000")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(20, 100, 341, 1))
        self.line_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.choosePath_save = QtWidgets.QPushButton(self.groupBox)
        self.choosePath_save.setGeometry(QtCore.QRect(130, 120, 131, 31))
        self.choosePath_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choosePath_save.setStyleSheet("QPushButton {\n"
"  border: 1px solid #2d9cdb;\n"
"  padding: 4px;\n"
"  border-radius: 2px;\n"
"  background-color: transparent;\n"
"  color: #333333;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  color: #828282;\n"
"  background-color: #bdbdbd;\n"
"  border: none;\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"  padding: 5px 20px;\n"
"}\n"
"")
        self.choosePath_save.setObjectName("choosePath_save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Save From..."))
        self.seoInput_name.setText(_translate("Form", "Seo by Input Name"))
        self.checkMD5_code.setText(_translate("Form", "Thay đổi MD5 Code"))
        self.pixel500.setText(_translate("Form", "500 x 500 px"))
        self.pixel720.setText(_translate("Form", "720 x 720 px"))
        self.pixel1000.setText(_translate("Form", "1000 x 1000 px"))
        self.choosePath_save.setToolTip(_translate("Form", "<html><head/><body><p>All changes are undone and the first image is restored.</p></body></html>"))
        self.choosePath_save.setText(_translate("Form", "Lưu Với Lựa Chọn"))

"""____________________________ Lớp Xứ Lý Chính ______________________________"""
class SaveForm(QtWidgets.QDialog, Ui_Form):
    def __init__(self, path_project, type):
        # ------------ GUI library User --------------
        super(SaveForm, self).__init__()
        self.setupUi(self)
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

class Ui_PiMage(object):
    def setupUi(self, PiMage):
        PiMage.setObjectName("PiMage")
        PiMage.resize(1032, 708)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PiMage.sizePolicy().hasHeightForWidth())
        PiMage.setSizePolicy(sizePolicy)
        PiMage.setStyleSheet("QWidget {\n"
"  background-color: #f2f2f2;\n"
"  color: #333333;\n"
"}\n"
"\n"
"QMenuBar {\n"
"  background-color: #fff;\n"
"  margin: 0px;\n"
"  border-bottom: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background-color: #fff;\n"
"  color: #333333;\n"
"  padding: 4px 10px;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  background-color: #2d9cdb;\n"
"  color: #fff;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QMenu {\n"
"  background-color: #fff;\n"
"  color: #333333;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  color: #bdbdbd;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  padding: 5px 25px;\n"
"  border: 1px;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QMenu::item:disabled {\n"
"  color: #828282;\n"
"  background-color: #bdbdbd;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  background-color: #2f80ed;\n"
"  color: #fff;\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QGroupBox {\n"
"  color: #333333;\n"
"  background-color: #e0e0e0;\n"
"  border-radius: 5px;\n"
"  font-weight: bold;\n"
"  font-size: 12px;\n"
"}\n"
"\n"
"QGroupBox > * {\n"
"  color: #333333;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"  border: 1px solid #2d9cdb;\n"
"  padding: 4px;\n"
"  border-radius: 2px;\n"
"  background-color: transparent;\n"
"  color: #333333;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  color: #828282;\n"
"  background-color: #bdbdbd;\n"
"  border: none;\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"  padding: 5px 20px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"  padding: 5px;\n"
"  border: none;\n"
"  background-color: #fff;\n"
"  border-radius: 5px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(PiMage)
        self.centralwidget.setObjectName("centralwidget")
        self.filtersGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.filtersGroupBox.setGeometry(QtCore.QRect(10, 410, 1011, 251))
        self.filtersGroupBox.setObjectName("filtersGroupBox")
        self.list_khung_san_pham = QtWidgets.QListWidget(self.filtersGroupBox)
        self.list_khung_san_pham.setGeometry(QtCore.QRect(230, 20, 511, 221))
        self.list_khung_san_pham.setStyleSheet("QListWidget {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"  border-radius: 5px;\n"
"  background-color: transparent;\n"
"  color: #333333;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"  color: #fff;\n"
"  background-color: #2d9cdb;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}")
        self.list_khung_san_pham.setMovement(QtWidgets.QListView.Free)
        self.list_khung_san_pham.setFlow(QtWidgets.QListView.LeftToRight)
        self.list_khung_san_pham.setProperty("isWrapping", True)
        self.list_khung_san_pham.setViewMode(QtWidgets.QListView.IconMode)
        self.list_khung_san_pham.setObjectName("list_khung_san_pham")
        self.toolBox = QtWidgets.QToolBox(self.filtersGroupBox)
        self.toolBox.setGeometry(QtCore.QRect(750, 20, 251, 221))
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet("QToolBox {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    background: #009deb;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QToolBox::tab:first {\n"
"    background: #4ade00;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QToolBox::tab:last {\n"
"    background: #f95300;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    color: white;\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 249, 157))
        self.page.setObjectName("page")
        self.rightToolsGroupBox_4 = QtWidgets.QGroupBox(self.page)
        self.rightToolsGroupBox_4.setGeometry(QtCore.QRect(0, 0, 251, 171))
        self.rightToolsGroupBox_4.setTitle("")
        self.rightToolsGroupBox_4.setObjectName("rightToolsGroupBox_4")
        self.addFrame_clicked = QtWidgets.QPushButton(self.rightToolsGroupBox_4)
        self.addFrame_clicked.setGeometry(QtCore.QRect(200, 0, 41, 21))
        self.addFrame_clicked.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addFrame_clicked.setObjectName("addFrame_clicked")
        self.brightnessTextLabel_14 = QtWidgets.QLabel(self.rightToolsGroupBox_4)
        self.brightnessTextLabel_14.setGeometry(QtCore.QRect(60, 0, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.brightnessTextLabel_14.setFont(font)
        self.brightnessTextLabel_14.setStyleSheet("QLabel {\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"  background-color: transparent;\n"
"}")
        self.brightnessTextLabel_14.setObjectName("brightnessTextLabel_14")
        self.imageKhungAdd = QtWidgets.QLabel(self.rightToolsGroupBox_4)
        self.imageKhungAdd.setGeometry(QtCore.QRect(10, 30, 121, 121))
        self.imageKhungAdd.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.imageKhungAdd.setStyleSheet("QLabel {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"  background-color: transparent;\n"
"}")
        self.imageKhungAdd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageKhungAdd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageKhungAdd.setLineWidth(1)
        self.imageKhungAdd.setText("")
        self.imageKhungAdd.setScaledContents(True)
        self.imageKhungAdd.setAlignment(QtCore.Qt.AlignCenter)
        self.imageKhungAdd.setObjectName("imageKhungAdd")
        self.check_remove_ai = QtWidgets.QCheckBox(self.rightToolsGroupBox_4)
        self.check_remove_ai.setGeometry(QtCore.QRect(150, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.check_remove_ai.setFont(font)
        self.check_remove_ai.setObjectName("check_remove_ai")
        self.apllyFrames_clicked = QtWidgets.QPushButton(self.rightToolsGroupBox_4)
        self.apllyFrames_clicked.setGeometry(QtCore.QRect(150, 120, 91, 31))
        self.apllyFrames_clicked.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apllyFrames_clicked.setObjectName("apllyFrames_clicked")
        self.download_ImgNotGB = QtWidgets.QPushButton(self.rightToolsGroupBox_4)
        self.download_ImgNotGB.setGeometry(QtCore.QRect(10, 0, 31, 21))
        self.download_ImgNotGB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_ImgNotGB.setObjectName("download_ImgNotGB")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 249, 157))
        self.page_2.setObjectName("page_2")
        self.rightToolsGroupBox_3 = QtWidgets.QGroupBox(self.page_2)
        self.rightToolsGroupBox_3.setGeometry(QtCore.QRect(0, 0, 251, 171))
        self.rightToolsGroupBox_3.setTitle("")
        self.rightToolsGroupBox_3.setObjectName("rightToolsGroupBox_3")
        self.brightnessTextLabel_7 = QtWidgets.QLabel(self.rightToolsGroupBox_3)
        self.brightnessTextLabel_7.setGeometry(QtCore.QRect(140, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.brightnessTextLabel_7.setFont(font)
        self.brightnessTextLabel_7.setAlignment(QtCore.Qt.AlignCenter)
        self.brightnessTextLabel_7.setObjectName("brightnessTextLabel_7")
        self.apllyLogo_clicked = QtWidgets.QPushButton(self.rightToolsGroupBox_3)
        self.apllyLogo_clicked.setGeometry(QtCore.QRect(200, 120, 41, 31))
        self.apllyLogo_clicked.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apllyLogo_clicked.setObjectName("apllyLogo_clicked")
        self.imageLogoAdd = QtWidgets.QLabel(self.rightToolsGroupBox_3)
        self.imageLogoAdd.setGeometry(QtCore.QRect(60, 40, 71, 71))
        self.imageLogoAdd.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.imageLogoAdd.setStyleSheet("QLabel {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"  background-color: transparent;\n"
"}")
        self.imageLogoAdd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLogoAdd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageLogoAdd.setLineWidth(1)
        self.imageLogoAdd.setText("")
        self.imageLogoAdd.setScaledContents(True)
        self.imageLogoAdd.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLogoAdd.setObjectName("imageLogoAdd")
        self.addLogo_clicked = QtWidgets.QPushButton(self.rightToolsGroupBox_3)
        self.addLogo_clicked.setGeometry(QtCore.QRect(70, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.addLogo_clicked.setFont(font)
        self.addLogo_clicked.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addLogo_clicked.setObjectName("addLogo_clicked")
        self.brightnessTextLabel_8 = QtWidgets.QLabel(self.rightToolsGroupBox_3)
        self.brightnessTextLabel_8.setGeometry(QtCore.QRect(0, 50, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.brightnessTextLabel_8.setFont(font)
        self.brightnessTextLabel_8.setAlignment(QtCore.Qt.AlignCenter)
        self.brightnessTextLabel_8.setObjectName("brightnessTextLabel_8")
        self.left_LogoValue = QtWidgets.QSpinBox(self.rightToolsGroupBox_3)
        self.left_LogoValue.setGeometry(QtCore.QRect(70, 130, 51, 20))
        self.left_LogoValue.setStyleSheet("QSpinBox {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}")
        self.left_LogoValue.setWrapping(False)
        self.left_LogoValue.setFrame(True)
        self.left_LogoValue.setAlignment(QtCore.Qt.AlignCenter)
        self.left_LogoValue.setReadOnly(False)
        self.left_LogoValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.left_LogoValue.setAccelerated(False)
        self.left_LogoValue.setKeyboardTracking(True)
        self.left_LogoValue.setMinimum(0)
        self.left_LogoValue.setMaximum(1000)
        self.left_LogoValue.setProperty("value", 0)
        self.left_LogoValue.setObjectName("left_LogoValue")
        self.brightnessTextLabel_10 = QtWidgets.QLabel(self.rightToolsGroupBox_3)
        self.brightnessTextLabel_10.setGeometry(QtCore.QRect(40, 110, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.brightnessTextLabel_10.setFont(font)
        self.brightnessTextLabel_10.setAlignment(QtCore.Qt.AlignCenter)
        self.brightnessTextLabel_10.setObjectName("brightnessTextLabel_10")
        self.top_LogoValue = QtWidgets.QSpinBox(self.rightToolsGroupBox_3)
        self.top_LogoValue.setGeometry(QtCore.QRect(10, 70, 41, 20))
        self.top_LogoValue.setStyleSheet("QSpinBox {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}")
        self.top_LogoValue.setWrapping(False)
        self.top_LogoValue.setFrame(True)
        self.top_LogoValue.setAlignment(QtCore.Qt.AlignCenter)
        self.top_LogoValue.setReadOnly(False)
        self.top_LogoValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.top_LogoValue.setAccelerated(False)
        self.top_LogoValue.setKeyboardTracking(True)
        self.top_LogoValue.setMinimum(0)
        self.top_LogoValue.setMaximum(1000)
        self.top_LogoValue.setProperty("value", 0)
        self.top_LogoValue.setObjectName("top_LogoValue")
        self.size_LogoValue = QtWidgets.QSpinBox(self.rightToolsGroupBox_3)
        self.size_LogoValue.setGeometry(QtCore.QRect(140, 70, 41, 20))
        self.size_LogoValue.setStyleSheet("QSpinBox {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}")
        self.size_LogoValue.setWrapping(False)
        self.size_LogoValue.setFrame(True)
        self.size_LogoValue.setAlignment(QtCore.Qt.AlignCenter)
        self.size_LogoValue.setReadOnly(False)
        self.size_LogoValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.size_LogoValue.setAccelerated(False)
        self.size_LogoValue.setKeyboardTracking(True)
        self.size_LogoValue.setMinimum(1)
        self.size_LogoValue.setMaximum(100)
        self.size_LogoValue.setProperty("value", 100)
        self.size_LogoValue.setObjectName("size_LogoValue")
        self.removeLogo_clicked = QtWidgets.QPushButton(self.rightToolsGroupBox_3)
        self.removeLogo_clicked.setGeometry(QtCore.QRect(200, 10, 41, 21))
        self.removeLogo_clicked.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeLogo_clicked.setObjectName("removeLogo_clicked")
        self.line = QtWidgets.QFrame(self.rightToolsGroupBox_3)
        self.line.setGeometry(QtCore.QRect(190, 10, 1, 141))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.brightnessTextLabel_9 = QtWidgets.QLabel(self.rightToolsGroupBox_3)
        self.brightnessTextLabel_9.setGeometry(QtCore.QRect(0, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.brightnessTextLabel_9.setFont(font)
        self.brightnessTextLabel_9.setAlignment(QtCore.Qt.AlignCenter)
        self.brightnessTextLabel_9.setObjectName("brightnessTextLabel_9")
        self.toolBox.addItem(self.page_2, "")
        self.tree_folder_open = QtWidgets.QTreeWidget(self.filtersGroupBox)
        self.tree_folder_open.setGeometry(QtCore.QRect(10, 20, 211, 221))
        self.tree_folder_open.setStyleSheet("QTreeWidget {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}")
        self.tree_folder_open.setObjectName("tree_folder_open")
        self.tree_folder_open.headerItem().setText(0, "1")
        self.list_product_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_product_widget.setGeometry(QtCore.QRect(10, 10, 1011, 391))
        self.list_product_widget.setStyleSheet("QListWidget {\n"
"  border-radius: 5px;\n"
"  background-color: #e0e0e0;\n"
"  border: 1px solid #2d9cdb;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  background-color: transparent;\n"
"  color: #333333;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"  color: #fff;\n"
"  background-color: #2d9cdb;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"  color: #fff;\n"
"  background-color: #2f80ed;\n"
"}")
        self.list_product_widget.setFlow(QtWidgets.QListView.LeftToRight)
        self.list_product_widget.setProperty("isWrapping", True)
        self.list_product_widget.setViewMode(QtWidgets.QListView.IconMode)
        self.list_product_widget.setObjectName("list_product_widget")
        PiMage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PiMage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        PiMage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PiMage)
        self.statusbar.setObjectName("statusbar")
        PiMage.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(PiMage)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_Only = QtWidgets.QAction(PiMage)
        self.actionSave_Only.setObjectName("actionSave_Only")
        self.actionSave_as = QtWidgets.QAction(PiMage)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionQuit = QtWidgets.QAction(PiMage)
        self.actionQuit.setObjectName("actionQuit")
        self.action_Information = QtWidgets.QAction(PiMage)
        self.action_Information.setObjectName("action_Information")
        self.action_Contact = QtWidgets.QAction(PiMage)
        self.action_Contact.setObjectName("action_Contact")
        self.actionOpen_Folder = QtWidgets.QAction(PiMage)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.active_WithKey = QtWidgets.QAction(PiMage)
        self.active_WithKey.setObjectName("active_WithKey")
        self.menuFile.addAction(self.active_WithKey)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Only)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.action_Information)
        self.menuEdit.addAction(self.action_Contact)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(PiMage)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PiMage)

    def retranslateUi(self, PiMage):
        _translate = QtCore.QCoreApplication.translate
        PiMage.setWindowTitle(_translate("PiMage", "PiMage"))
        self.filtersGroupBox.setTitle(_translate("PiMage", "Tùy Biến"))
        self.addFrame_clicked.setToolTip(_translate("PiMage", "<html><head/><body><p>All changes are undone and the first image is restored.</p></body></html>"))
        self.addFrame_clicked.setText(_translate("PiMage", "+"))
        self.brightnessTextLabel_14.setText(_translate("PiMage", "Thêm Khung Sản Phẩm:"))
        self.check_remove_ai.setText(_translate("PiMage", "Remove AI...."))
        self.apllyFrames_clicked.setToolTip(_translate("PiMage", "<html><head/><body><p>All changes are undone and the first image is restored.</p></body></html>"))
        self.apllyFrames_clicked.setText(_translate("PiMage", "Thêm"))
        self.download_ImgNotGB.setToolTip(_translate("PiMage", "<html><head/><body><p>All changes are undone and the first image is restored.</p></body></html>"))
        self.download_ImgNotGB.setText(_translate("PiMage", "DL"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("PiMage", "...Thêm Khung Của Bạn..."))
        self.brightnessTextLabel_7.setText(_translate("PiMage", "Size:"))
        self.apllyLogo_clicked.setToolTip(_translate("PiMage", "<html><head/><body><p>All changes are undone and the first image is restored.</p></body></html>"))
        self.apllyLogo_clicked.setText(_translate("PiMage", "OK"))
        self.addLogo_clicked.setToolTip(_translate("PiMage", "<html><head/><body><p>All changes are undone and the first image is restored.</p></body></html>"))
        self.addLogo_clicked.setText(_translate("PiMage", "Logo"))
        self.brightnessTextLabel_8.setText(_translate("PiMage", "| Lề Trên"))
        self.brightnessTextLabel_10.setText(_translate("PiMage", "-  Lề Trái ( 0-> 1000)"))
        self.removeLogo_clicked.setToolTip(_translate("PiMage", "<html><head/><body><p>All changes are undone and the first image is restored.</p></body></html>"))
        self.removeLogo_clicked.setText(_translate("PiMage", "X"))
        self.brightnessTextLabel_9.setText(_translate("PiMage", "0 -> 1000"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("PiMage", "....Thêm Logo Của Bạn...."))
        self.menuFile.setTitle(_translate("PiMage", "File"))
        self.menuEdit.setTitle(_translate("PiMage", "Hỗ Trợ"))
        self.actionOpen_File.setText(_translate("PiMage", "(Chọn)  Hình Ảnh"))
        self.actionSave_Only.setText(_translate("PiMage", "(Lưu) Hình Ảnh"))
        self.actionSave_as.setText(_translate("PiMage", "(Lưu) Thư Mục Hình Ảnh..."))
        self.actionQuit.setText(_translate("PiMage", "Đóng Chương Trình ()"))
        self.action_Information.setText(_translate("PiMage", "Thông Tin Phần Mềm"))
        self.action_Contact.setText(_translate("PiMage", "Liên Hệ Hỗ Trợ"))
        self.actionOpen_Folder.setText(_translate("PiMage", "(Chọn) Thư Mục Hình Ảnh"))
        self.active_WithKey.setText(_translate("PiMage", "Active With Key..."))

class PeeEditorWindow(QtWidgets.QMainWindow, Ui_PiMage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("PeeEditor - Zalo 0799246958")
        self.setWindowIcon(QtGui.QIcon("iconWindows.png"))

        # Các biến đầu vào
        self.image_filter_exist = False
        self.path_folder = ""
        # self.path_img = ""
        self.path_khung = ""
        self.khung_select = ""
        self.mImgList = []
        self.path_project = os.getcwd()
        self.frames_storage = self.path_project + "/frames"

        # --------------------
        self.loadList_frames_product()                                  # Hiển thị các khung sản phẩm trong LIB
        self.setDefault_Value_logo()                                    # Các thông số cài đặt ban đầu của Logo

        # ---------------------
        self.khung_selected = None
        self.logo_selected = None

        # ---------------------

        self.check_active_program()

        # Cấu hình cho cây thư mục (QtreeWidget)
        self.tree_folder_open.setHeaderLabels(["File Name or Folder Name"])
        self.tree_folder_open.setIconSize(QtCore.QSize(14, 14))
        self.tree_folder_open.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tree_folder_open.itemClicked.connect(self._clicked_item_treewidget)

        self.actionQuit.triggered.connect(self.close_project)

        # # --- connections --- #
        self.actionOpen_File.triggered.connect(self.open_file_item)
        self.actionOpen_Folder.triggered.connect(self.open_folder_item)
        self.actionSave_Only.triggered.connect(self.save_only_image)
        self.actionSave_as.triggered.connect(self.save_as_all_image)

        self.addFrame_clicked.clicked.connect(self.add_frame_button)
        self.check_remove_ai.stateChanged.connect(self.remove_background)
        self.apllyFrames_clicked.clicked.connect(self.aplly_addFrames_storage)
        self.download_ImgNotGB.clicked.connect(self.download_image_notGB)

        self.list_khung_san_pham.itemDoubleClicked.connect(self._add_khung_on_top)

        self.addLogo_clicked.clicked.connect(self.choose_logo_path)
        self.apllyLogo_clicked.clicked.connect(self.aplly_logo_clicked)
        self.removeLogo_clicked.clicked.connect(self.remove_logo_clicked)

        self.action_Information.triggered.connect(self.show_Information)
        self.action_Contact.triggered.connect(self.contact_dev)
        self.active_WithKey.triggered.connect(self.active_with_key)

# =============================== Các hàm khởi tạo và dùng chung =============================== #
    # ----- Ẩn các chức năng ----- #
    def check_active_program(self):
        msmdspdm = open(self.path_project + "/msmdspdm.txt", "r")
        base64_message = str(msmdspdm.readlines()[0])
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        if str(message) == "not_activated":
            self.actionOpen_File.setDisabled(True)
            self.actionOpen_Folder.setDisabled(True)
            self.actionSave_Only.setDisabled(True)
            self.actionSave_as.setDisabled(True)

            self.addFrame_clicked.setDisabled(True)
            self.apllyFrames_clicked.setDisabled(True)
            self.check_remove_ai.setDisabled(True)

            self.addLogo_clicked.setDisabled(True)
            self.removeLogo_clicked.setDisabled(True)
            self.apllyLogo_clicked.setDisabled(True)
        if str(message) == "activated":
            self.actionOpen_File.setDisabled(False)
            self.actionOpen_Folder.setDisabled(False)
            self.actionSave_Only.setDisabled(False)
            self.actionSave_as.setDisabled(False)

            self.addFrame_clicked.setDisabled(False)
            self.apllyFrames_clicked.setDisabled(False)
            self.check_remove_ai.setDisabled(False)

            self.addLogo_clicked.setDisabled(False)
            self.removeLogo_clicked.setDisabled(False)
            self.apllyLogo_clicked.setDisabled(False)

    def active_with_key(self):
        try:
            key_input, status = QtWidgets.QInputDialog.getText(self, 'Active With Key...', 'Nhập Key Active:')
            if status:
                if key_input:
                    key_list = []
                    qtattributionsscanner = open(self.path_project + "/qtattributionsscanner.txt", "r")
                    qtattributionsscanner = qtattributionsscanner.readlines()
                    for base64_message in qtattributionsscanner:
                        base64_bytes = str(base64_message).encode('ascii')
                        message_bytes = base64.b64decode(base64_bytes)
                        message = message_bytes.decode('ascii')
                        key_list.append(str(message))
                    if key_input in key_list:
                        msmdspdm = open(self.path_project + "/msmdspdm.txt", "w")
                        msmdspdm.write("YWN0aXZhdGVk")
                        msmdspdm.close()
                        QtWidgets.QMessageBox.information(self, "Actived Successfully", "Chúc Mừng, Bạn Đã Actived Thành Công!")
                        self.check_active_program()
                    else:
                        self.error_message("Thông Báo", "Key Active Không Hợp Lệ!")
                else: pass
            else: pass
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    # ----- Các thông số mặc định ban đầu ----- #
    def setDefault_Value_logo(self):
        self.size_percent = self.size_LogoValue.value()
        self.pxLeft_logo = self.left_LogoValue.value()
        self.pxTop_logo = self.top_LogoValue.value()

    # ----- Hiển thị các khung sản phẩm có sẵn trong thư viện ----- #
    def loadList_frames_product(self):
        self.list_khung_san_pham.clear()
        self.mFramesList = []
        os.chdir(self.frames_storage)
        list_img = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg")
        for num in range(1, len(list_img) + 1):
            path_img = self.frames_storage + "/khung-" + str(num) + ".png"
            self.mFramesList.append(path_img)
            self.show_frames_product(path_img)

    # ----- Hàm hiển thị khung ảnh sản phẩm ----- #
    def show_frames_product(self, path):
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            self.icons = QtWidgets.QListWidgetItem(QtGui.QIcon(pixmap), None)
            self.iconSize = QtCore.QSize(110, 110)
            self.list_khung_san_pham.setIconSize(self.iconSize)
            self.list_khung_san_pham.addItem(self.icons)

    # ----- Lấy icon các item trong Qtree ----- #
    def get_icon_item_win(self, path):
        fileInfo = QtCore.QFileInfo(path)
        fileIcon = QtWidgets.QFileIconProvider()
        icon = QtGui.QIcon(fileIcon.icon(fileInfo))
        return icon

    # ----- Cửa sổ hiển thị lỗi ----- #
    def error_message(self, title, msg):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(msg)
        msgbox.setIcon(msgbox.Critical)
        msgbox.exec_()

    # ----- Tạo cây thư mục ----- #
    def create_tree_structure(self, startpath, tree):
        for element in os.listdir(startpath):
            path_info = startpath + "/" + element
            if os.path.isdir(path_info):
                parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
                self.create_tree_structure(path_info, parent_itm)
                fileInfo = QtCore.QFileInfo(path_info)
                fileIcon = QtWidgets.QFileIconProvider()
                icon = QtGui.QIcon(fileIcon.icon(fileInfo))
                parent_itm.setIcon(0, QIcon(icon))
            else:
                if path_info.split(".")[-1] in ["png", "jpg", "jpeg", "PNG", "JPG", "JPEG"]:
                    parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
                    fileInfo = QtCore.QFileInfo(path_info)
                    fileIcon = QtWidgets.QFileIconProvider()
                    icon = QtGui.QIcon(fileIcon.icon(fileInfo))
                    parent_itm.setIcon(0, QIcon(icon))

    # ----- Đóng chương trình ----- #
    def close_project(self):
        self.close()

    # ----- Kiểm tra kích thước hình ảnh ----- #
    def check_size_input_image(self, pixmap):
        if pixmap.width() > pixmap.height():
            pixmap = pixmap.copy(QtCore.QRect(int((pixmap.width() / 2) - (pixmap.height() / 2)), 0, pixmap.height(), pixmap.height()))
        elif pixmap.width() < pixmap.height():
            pixmap = pixmap.copy(QtCore.QRect(0, int((pixmap.height() / 2) - (pixmap.width() / 2)), pixmap.width(), pixmap.width()))
        else:
            pixmap = pixmap
        return pixmap

#  =================================== Thêm Dữ Liệu Hình Ảnh =================================== #

    # ----- Chọn hình ảnh cần chỉnh sửa ----- #
    def open_file_item(self):
        try:
            path_img, _ = QFileDialog.getOpenFileName(self, "Chọn Hình Ảnh", self.path_project)
            if path_img == "":
                return
            if path_img.split(".")[-1] not in ["png", "jpg", "jpeg", "jfif", "PNG", "JPG", "JPEG", "JFIF"]:
                self.error_message("Không Hỗ Trợ File",
                                   "Định dạng file hỗ trợ: .jpg or .png or .jpeg or .jfif")
            else:
                self.mImgList = []
                self.tree_folder_open.clear()
                self.list_product_widget.clear()
                self.remove_logo_clicked()
                self.khung_selected = None
                self.logo_selected = None
                self.imageLogoAdd.clear()
                self.size_LogoValue.setValue(100)
                self.left_LogoValue.setValue(0)
                self.top_LogoValue.setValue(0)
                self.path_folder = ""
                parent_itm = QTreeWidgetItem(self.tree_folder_open, [os.path.basename(path_img)])
                icon = self.get_icon_item_win(path_img)
                parent_itm.setIcon(0, QIcon(icon))
                self.mImgList.append(path_img)
                self.show_images_selected(str(path_img))
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    # ----- Hiển thị danh sách hình ảnh được lựa chọn ----- #
    def show_images_selected(self, path):
        base_pixmap = QtGui.QPixmap(path)
        base_pixmap = self.check_size_input_image(base_pixmap)
        base_pixmap = base_pixmap.scaled(int(1000), int(1000))
        if self.khung_selected is not None:
            khung_pixmap = QtGui.QPixmap(self.khung_selected)
            khung_pixmap = khung_pixmap.scaled(int(1000), int(1000))
            painter = QtGui.QPainter(base_pixmap)
            painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
            painter.drawPixmap(QtCore.QPoint(), khung_pixmap)
            painter.end()
        if self.logo_selected is not None:
            logo_pixmap = QtGui.QPixmap(self.logo_selected)
            width = int(logo_pixmap.width() * self.size_percent / 100)
            height = int(logo_pixmap.height() * self.size_percent / 100)
            logo_pixmap = logo_pixmap.scaled(int(width), int(height))
            painter = QtGui.QPainter(base_pixmap)
            painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
            painter.drawPixmap(QtCore.QPoint(int(self.pxLeft_logo), int(self.pxTop_logo)), logo_pixmap)
            painter.end()
        if not base_pixmap.isNull():
            self.icons = QtWidgets.QListWidgetItem(QtGui.QIcon(base_pixmap), None)
            self.iconSize = QtCore.QSize(180, 180)
            self.list_product_widget.setIconSize(self.iconSize)
            self.list_product_widget.addItem(self.icons)

    # ----- Chọn 'Folder Hình Ảnh' - 'Folder Chứa Folder Hình Ảnh' ----- #
    def open_folder_item(self):
        try:
            check = False
            path_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Chọn Folder Hình Ảnh", self.path_project)
            if path_folder == "":
                return
            self.path_folder = path_folder
            self.tree_folder_open.clear()
            self.khung_selected = None
            self.logo_selected = None
            self.imageLogoAdd.clear()
            self.size_LogoValue.setValue(100)
            self.left_LogoValue.setValue(0)
            self.top_LogoValue.setValue(0)
            self.create_tree_structure(self.path_folder, self.tree_folder_open)
            self.list_product_widget.clear()
            self.remove_logo_clicked()
            for a in os.listdir(self.path_folder):
                if os.path.isdir(self.path_folder + "/" + a): check = True
            if check is False:
                self.show_list_item_folder(self.path_folder)
            # self.reload_imageLabel()
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    # ----- Thực hiện lệnh khi chọn folder hình ảnh cuối cùng ----- #
    def _clicked_item_treewidget(self):
        try:
            if self.path_folder == "":
                return
            path = self.path_folder + self.get_path_item_tree()
            if os.path.isdir(path) == False:
                return
            else:
                check = False
                for a in os.listdir(path):
                    if os.path.isdir(path + "/" + a): check = True
                if check is False:
                    self.list_product_widget.clear()
                    self.show_list_item_folder(path)
                else:
                    return
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    # ----- Lấy tên hình ảnh khi lựa chọn list Image ----- #
    def get_path_item_tree(self):
        for sel in self.tree_folder_open.selectedIndexes():
            val = "/"+sel.data()
            while sel.parent().isValid():
                sel = sel.parent()
                val = "/" + sel.data() + val
            return val

    # ----- Hiển thị hình ảnh trong folder được chọn ----- #
    def show_list_item_folder(self, path):
        self.mImgList = []
        os.chdir(path)
        list_img = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.jfif")
        for img in list_img:
            path_img = path + "/" + img
            self.mImgList.append(path_img)
            self.show_images_selected(path_img)

#  =================================== Thêm Khung Sản Phẩm =================================== #
    # ----- Chọn đến file khung sản phẩm muốn thêm ----- #
    def add_frame_button(self):
        try:
            path, _ = QFileDialog.getOpenFileName(self, "Chọn Khung Của Bạn", self.path_project)
            if path == "":
                return
            if path.split(".")[-1] not in ["png", "jpg", "jpeg", "jfif", "PNG", "JPG", "JPEG", "JFIF"]:
                self.error_message("Sai định dạng", "Chỉ hỗ trợ các định dạng: .jpg or .png or .jpeg or .jfif")
            else:
                self.khung_select = path
                self.show_frame_image(path)
                self.check_remove_ai.setChecked(False)
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    # ----- Hiển thị khung sản phẩm vừa thêm vào ----- #
    def show_frame_image(self, path):
        self.imageKhungAdd.clear()
        self.path_khung = path
        pixmap = QPixmap(path)
        width, height = self.scale_khung_insert(pixmap.width(), pixmap.height())
        pixmap = pixmap.scaled(int(width), int(height))
        self.imageKhungAdd.setPixmap(pixmap)

    # ----- Tỷ lệ hiển thị khung sản phẩm ----- #
    def scale_khung_insert(self, width, height):
        k = self.imageKhungAdd.frameGeometry().height() / height
        if width * k <= self.imageKhungAdd.frameGeometry().width():
            w = width * k
            h = self.imageKhungAdd.frameGeometry().height()
        else:
            k = self.imageKhungAdd.frameGeometry().width() / width
            w = self.imageKhungAdd.frameGeometry().width()
            h = height * k
        return w, h

    # ----- Tự động xóa Background cho khung sản phẩm ----- #
    def remove_background(self):
        try:
            if self.khung_select == "":
                return
            if self.check_remove_ai.isChecked():
                img = cv2.imread(self.khung_select)
                # convert to graky
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # threshold input image as mask
                mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]
                # negate mask
                mask = 255 - mask
                # apply morphology to remove isolated extraneous noise
                # use borderconstant of black since foreground touches the edges
                kernel = np.ones((3, 3), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                # anti-alias the mask -- blur then stretch
                # blur alpha channel
                mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=2, sigmaY=2, borderType=cv2.BORDER_DEFAULT)
                # linear stretch so that 127.5 goes to 0, but 255 stays 255
                mask = (2 * (mask.astype(np.float32)) - 255.0).clip(0, 255).astype(np.uint8)
                # put mask into alpha channel
                result = img.copy()
                result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
                result[:, :, 3] = mask
                path = self.path_project + "/frame_add.png"
                cv2.imwrite(path, result)
                self.show_frame_image(path)
            else:
                self.show_frame_image(self.khung_select)
        except Exception as e:
            self.error_message("Cảnh Báo", str("Tên File Không Được Có Dấu Hoặc Ký Tự Đặc Biệt!"))

    # ----- Thêm khung sản phẩm và các lựa chọn vào thư viện ----- #
    def aplly_addFrames_storage(self):
        try:
            if self.khung_select == "":
                return
            name = str(int(len(os.listdir(self.frames_storage))) + 1)
            dst = self.frames_storage + "/khung-" + name + ".png"
            if self.check_remove_ai.isChecked():
                shutil.copy(self.path_project + "/frame_add.png", dst)
                self.loadList_frames_product()
            else:
                shutil.copy(self.khung_select, dst)
                self.loadList_frames_product()
            self.khung_select = ""
            self.imageKhungAdd.clear()
            self.path_khung = ""
            self.check_remove_ai.setChecked(False)
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    def download_image_notGB(self):
        try:
            if self.path_khung:
                path_saveImg = QtWidgets.QFileDialog.getSaveFileName(self, "Lưu File", str(self.path_khung))[0]
                if path_saveImg == "":
                    return
                shutil.copy(self.path_khung, path_saveImg)
                QtWidgets.QMessageBox.information(self, "Thành Công", "Lưu Hình Ảnh Thành Công...")
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    #  =================================== Thêm Logo Sản Phẩm =================================== #
    # ----- Lựa chọn đường dẫn logo ----- #
    def choose_logo_path(self):
        try:
            path, _ = QFileDialog.getOpenFileName(self, "Chọn Logo Của Bạn", self.path_khung)
            if path == "":
                return
            if path.split(".")[-1] not in ["png", "jpg", "jpeg", "jfif", "PNG", "JPG", "JPEG", "JFIF"]:
                self.error_message("Sai định dạng", "Chỉ hỗ trợ các định dạng: .jpg or .png or .jpeg or .jfif")
            else:
                if self.mImgList == []:
                    self.error_message("Cảnh báo", "Vui lòng thêm ảnh sản phẩm!")
                    return
                self.show_logo_image(path)
                self.logo_selected = path
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    # ----- Hiển thị logo sản phẩm ----- #
    def show_logo_image(self, path):
        self.imageLogoAdd.clear()
        pixmap = QPixmap(path)
        width, height = self.scale_logo_insert(pixmap.width(), pixmap.height())
        pixmap = pixmap.scaled(int(width), int(height))
        self.imageLogoAdd.setPixmap(pixmap)

    # ----- Tỷ lệ hiển thị logo sản phẩm ----- #
    def scale_logo_insert(self, width, height):
        k = self.imageLogoAdd.frameGeometry().height() / height
        if width * k <= self.imageLogoAdd.frameGeometry().width():
            w = width * k
            h = self.imageLogoAdd.frameGeometry().height()
        else:
            k = self.imageLogoAdd.frameGeometry().width() / width
            w = self.imageLogoAdd.frameGeometry().width()
            h = height * k
        return w, h

#  =================================== Lựa Chọn Khung Sản Phẩm =================================== #
    # ----- Chèn khung sản phẩm vào hình ảnh----- #
    def _add_khung_on_top(self):
        try:
            if self.mImgList == [] or self.mFramesList == []:
                return
            a = [x.row() for x in self.list_khung_san_pham.selectedIndexes()]
            self.khung_selected = self.mFramesList[a[0]]
            self.list_product_widget.clear()
            for img_path in self.mImgList:
                self.show_images_selected(img_path)
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

#  =============================== Thay đổi thông số hình ảnh logo =============================== #
    # ----- Áp dụng các thông số của logo ----- #
    def aplly_logo_clicked(self):
        try:
            if self.logo_selected is None:
                return
            self.size_percent = self.size_LogoValue.value()
            self.pxLeft_logo = self.left_LogoValue.value()
            self.pxTop_logo = self.top_LogoValue.value()
            self.list_product_widget.clear()
            for img_path in self.mImgList:
                self.show_images_selected(img_path)
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    # ----- Xóa logo đã thêm vào ----- #
    def remove_logo_clicked(self):
        try:
            if self.logo_selected is None:
                return
            self.imageLogoAdd.clear()
            self.logo_selected = None
            self.size_LogoValue.setValue(100)
            self.left_LogoValue.setValue(0)
            self.top_LogoValue.setValue(0)
            self.list_product_widget.clear()
            for img_path in self.mImgList:
                self.show_images_selected(img_path)
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

# =================================== Các hàm lưu trữ hình ảnh =================================== #
    def save_only_image(self):
        try:
            a = [x.row() for x in self.list_product_widget.selectedIndexes()]
            if a:
                img_select = self.mImgList[a[0]]
                file_name = os.path.splitext(os.path.basename(self.mImgList[a[0]]))[0]
                path_saveImg = QtWidgets.QFileDialog.getSaveFileName(self, "Lưu File", str(file_name) + ".png")[0]
                if path_saveImg == "":
                    return
                SaveForm(self.path_project, "Only")
                img = Image.open(img_select)
                img = img.convert('RGB')
                width, height = img.size
                if width > height: img = img.crop((int((width / 2) - (height / 2)), 0, int((width / 2) + (height / 2)), int(height)))
                elif width < height: img = img.crop((0, int((height / 2) - (width / 2)), int(width), int((height / 2) + (width / 2))))
                else: pass
                img = img.resize((int(1000), int(1000)), Image.ANTIALIAS)
                if self.khung_selected is not None:
                    khung = Image.open(self.khung_selected)
                    khung = khung.resize((int(1000), int(1000)), Image.ANTIALIAS)
                    img.paste(khung, (0, 0), khung)
                if self.logo_selected is not None:
                    logo = Image.open(self.logo_selected)
                    width_logo, height_logo = logo.size
                    width = int(width_logo * self.size_percent / 100)
                    height = int(height_logo * self.size_percent / 100)
                    logo = logo.resize((int(width), int(height)), Image.ANTIALIAS)
                    img.paste(logo, (self.pxLeft_logo, self.pxTop_logo), logo)
                img = img.resize((int(variable.pixel_value), int(variable.pixel_value)), Image.ANTIALIAS)
                img.save(path_saveImg, quality=95)
                QtWidgets.QMessageBox.information(self, "Thành Công", "Lưu Hình Ảnh Thành Công...")
            else:
                self.error_message("Thông Báo", "Vui lòng chọn một hình ảnh cần lưu")
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    def save_as_all_image(self):
        try:
            if self.path_folder == "":
                self.error_message("Cảnh báo", "Bạn chưa thêm dữ liệu hoặc dữ liệu bạn thêm không phải thư mục!")
                return
            pathSave_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Chọn Folder Lưu", self.path_folder)
            if pathSave_folder == "":
                return
            SaveForm(self.path_project, "All")
            pathSave_folder = pathSave_folder + "/" + os.path.basename(self.path_folder) + "-pee_export"
            if os.path.isdir(pathSave_folder) is False:
                os.mkdir(pathSave_folder)
            for dirpath, dirnames, filenames in os.walk(self.path_folder):
                directory_level = dirpath.replace(self.path_folder, "")
                if os.path.isdir(pathSave_folder + directory_level) is False:
                    os.mkdir(pathSave_folder + directory_level)
                num = 1
                for f in filenames:
                    if os.path.splitext(f)[1] not in [".png", ".jpg", ".jpeg", ".jfif", ".PNG", ".JPG", ".JPEG", ".JFIF"]:
                        pass
                    else:
                        img_select = dirpath + "/" + f
                        text_name = self.text_as_by_seo(str(os.path.basename(dirpath)))
                        if variable.seo_name is True:
                            path_saveFolder = pathSave_folder + directory_level + "/" + text_name + "-" + str(num) + ".jpg"
                        else:
                            path_saveFolder = pathSave_folder + directory_level + "/" + f
                        img = Image.open(img_select)
                        img = img.convert('RGB')
                        width, height = img.size
                        if width > height:
                            img = img.crop((int((width / 2) - (height / 2)), 0, int((width / 2) + (height / 2)), int(height)))
                        elif width < height:
                            img = img.crop((0, int((height / 2) - (width / 2)), int(width), int((height / 2) + (width / 2))))
                        else:
                            pass
                        img = img.resize((int(1000), int(1000)), Image.ANTIALIAS)
                        if self.khung_selected is not None:
                            khung = Image.open(self.khung_selected)
                            khung = khung.resize((int(1000), int(1000)), Image.ANTIALIAS)
                            img.paste(khung, (0, 0), khung)
                        if self.logo_selected is not None:
                            logo = Image.open(self.logo_selected)
                            width_logo, height_logo = logo.size
                            width = int(width_logo * self.size_percent / 100)
                            height = int(height_logo * self.size_percent / 100)
                            logo = logo.resize((int(width), int(height)), Image.ANTIALIAS)
                            img.paste(logo, (self.pxLeft_logo, self.pxTop_logo), logo)
                        img = img.resize((int(variable.pixel_value), int(variable.pixel_value)), Image.ANTIALIAS)
                        img.save(path_saveFolder, quality=95)
                        num = num + 1
            QtWidgets.QMessageBox.information(self, "Thành Công", "Lưu Thư Mục Thành Công...")
        except Exception as e:
            self.error_message("Cảnh Báo", str(e))

    def text_as_by_seo(self, text):
        special_char = "@_!#$%^&*()<>?/\|}{~:;[']"
        for i in special_char:
            text = text.replace(i, '')
            text = text.replace(" ", '-')
            text = text.lower()
        return text

# =================================== Thông tin phần mềm =================================== #
    def show_Information(self):
        QtWidgets.QMessageBox.information(self, "Thông Tin Phần Mềm",
                                          "- Tên Phần Mềm: PeeEditor Ver 1.0\n"
                                          "- Mục đích: Đóng khung sản phẩm tự động\n"
                                          "- Ngày tạo: 20/7/2021\n")

    def contact_dev(self):
        QtWidgets.QMessageBox.information(self, "Liên Hệ Hỗ Trợ",
                                          "- Zalo: 0799246958\n"
                                          "- FB: https://www.facebook.com/---------/\n")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PeeEditorWindow()
    window.show()
    sys.exit(app.exec_())