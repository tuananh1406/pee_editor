from PyQt5 import QtWidgets, QtGui, uic
from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QSizePolicy, QTreeWidgetItem
from PyQt5.QtGui import QPixmap, QImage, QIntValidator, QIcon
from PIL import Image
import numpy as np
import cv2, glob, shutil, sys, os, base64
import variable

class PeeEditorWindow(QtWidgets.QMainWindow):

    def __init__(self):
        # Load UI
        super(PeeEditorWindow, self).__init__()
        uic.loadUi('PeeEditor.ui', self)
        self.setWindowTitle("PeeEditor - Zalo 0359156732")
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
            if path_img.split(".")[-1] not in ["png", "jpg", "jpeg", "PNG", "JPG", "JPEG"]:
                self.error_message("Không Hỗ Trợ File",
                                   "Định dạng file hỗ trợ: .jpg or .png or .jpeg")
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
            print("open_file_item: ", str(e))

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

    # ----- Thực hiện lệnh khi chọn folder hình ảnh cuối cùng ----- #
    def _clicked_item_treewidget(self):
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
        list_img = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg")
        for img in list_img:
            path_img = path + "/" + img
            self.mImgList.append(path_img)
            self.show_images_selected(path_img)

#  =================================== Thêm Khung Sản Phẩm =================================== #
    # ----- Chọn đến file khung sản phẩm muốn thêm ----- #
    def add_frame_button(self):
        path, _ = QFileDialog.getOpenFileName(self, "Chọn Khung Của Bạn", self.path_project)
        if path == "":
            return
        if path.split(".")[-1] not in ["png", "jpg", "jpeg", "PNG", "JPG", "JPEG"]:
            self.error_message("Sai định dạng", "Chỉ hỗ trợ các định dạng: .jpg or .png or .jpeg")
        else:
            self.khung_select = path
            self.show_frame_image(path)
            self.check_remove_ai.setChecked(False)

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
            print(str(e))

    # ----- Thêm khung sản phẩm và các lựa chọn vào thư viện ----- #
    def aplly_addFrames_storage(self):
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

    def download_image_notGB(self):
        if self.path_khung:
            path_saveImg = QtWidgets.QFileDialog.getSaveFileName(self, "Lưu File", str(self.path_khung))[0]
            if path_saveImg == "":
                return
            shutil.copy(self.path_khung, path_saveImg)
            QtWidgets.QMessageBox.information(self, "Thành Công", "Lưu Hình Ảnh Thành Công...")

    #  =================================== Thêm Logo Sản Phẩm =================================== #
    # ----- Lựa chọn đường dẫn logo ----- #
    def choose_logo_path(self):
        path, _ = QFileDialog.getOpenFileName(self, "Chọn Logo Của Bạn", self.path_khung)
        if path == "":
            return
        if path.split(".")[-1] not in ["png", "jpg", "jpeg", "PNG", "JPG", "JPEG"]:
            self.error_message("Sai định dạng", "Chỉ hỗ trợ các định dạng: .jpg or .png or .jpeg")
        else:
            if self.mImgList == []:
                self.error_message("Cảnh báo", "Vui lòng thêm ảnh sản phẩm!")
                return
            self.show_logo_image(path)
            self.logo_selected = path

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
            print(e)

#  =============================== Thay đổi thông số hình ảnh logo =============================== #
    # ----- Áp dụng các thông số của logo ----- #
    def aplly_logo_clicked(self):
        if self.logo_selected is None:
            return
        self.size_percent = self.size_LogoValue.value()
        self.pxLeft_logo = self.left_LogoValue.value()
        self.pxTop_logo = self.top_LogoValue.value()
        self.list_product_widget.clear()
        for img_path in self.mImgList:
            self.show_images_selected(img_path)

    # ----- Xóa logo đã thêm vào ----- #
    def remove_logo_clicked(self):
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
                import SaveForm
                SaveForm.SaveForm(self.path_project, "Only")
                img = Image.open(img_select)
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
            import SaveForm
            SaveForm.SaveForm(self.path_project, "All")
            pathSave_folder = pathSave_folder + "/" + os.path.basename(self.path_folder) + "-pee_export"
            if os.path.isdir(pathSave_folder) is False:
                os.mkdir(pathSave_folder)
            for dirpath, dirnames, filenames in os.walk(self.path_folder):
                directory_level = dirpath.replace(self.path_folder, "")
                if os.path.isdir(pathSave_folder + directory_level) is False:
                    os.mkdir(pathSave_folder + directory_level)
                num = 1
                for f in filenames:
                    img_select = dirpath + "/" + f
                    text_name = self.text_as_by_seo(str(os.path.basename(dirpath)))
                    if variable.seo_name is True:
                        path_saveFolder = pathSave_folder + directory_level + "/" + text_name + "-" + str(num) + ".jpg"
                    else:
                        path_saveFolder = pathSave_folder + directory_level + "/" + f
                    img = Image.open(img_select)
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
                                          "- Zalo: 0359156732\n"
                                          "- FB: ............\n")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PeeEditorWindow()
    window.show()
    sys.exit(app.exec_())
