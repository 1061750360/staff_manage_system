# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\computer\PycharmProjects\UIProjects\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

import SMS_rc
import sys
from socket import *
import re
import time
from Ui_info_manage import *

IP_PORT = ('127.0.0.1', 8888)
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.connect(IP_PORT)

class Ui_Dg_01(object):
    def __init__(self,Dg_01):
        self.setupUi(Dg_01)

    def setupUi(self, Dg_01):
        Dg_01.setObjectName("Dg_01")
        Dg_01.resize(421, 301)
        Dg_01.setMinimumSize(QtCore.QSize(421, 301))
        Dg_01.setMaximumSize(QtCore.QSize(421, 301))
        self.form = Dg_01
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/SMS/resource/window_icon/1208279.gif"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dg_01.setWindowIcon(icon)
        Dg_01.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dg_01)
        self.label.setGeometry(QtCore.QRect(10, 0, 401, 291))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("../../Desktop/SMS/resource/bg_img/bg_0.jpg"))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Dg_01)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 120, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dg_01)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dg_01)
        self.pushButton.setGeometry(QtCore.QRect(200, 210, 61, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dg_01)
        QtCore.QMetaObject.connectSlotsByName(Dg_01)

    def retranslateUi(self, Dg_01):
        _translate = QtCore.QCoreApplication.translate
        Dg_01.setWindowTitle(_translate("Dg_01", "登录"))
        Dg_01.setWhatsThis(_translate("Dg_01", "登陆页面"))
        self.label_2.setText(_translate("Dg_01", "用户名:"))
        self.label_3.setText(_translate("Dg_01", "密  码:"))
        self.label_4.setText(_translate("Dg_01", "欢迎使用员工管理系统"))
        self.pushButton.setText(_translate("Dg_01", "登录"))
        self.pushButton.clicked.connect(self.jump_to_mainwindow)


    def jump_to_mainwindow(self):
        a = self.do_login()
        if a == 1:
            self.form.hide()
            self.app1 = QtWidgets.QApplication(sys.argv)
            self.mainwindow = QtWidgets.QMainWindow()
            self.ui = MainWindow()
            self.ui.setupUi(self.mainwindow)
            self.mainwindow.show()
            self.app1.exec_()

    def do_login(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if not name or not password:
            QtWidgets.QMessageBox.warning(self.form,"警告","用户名或密码为空",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)
            return 0
        else:
            msg = "Ll$" + name + "#" + password
            while True:
                sockfd.send(msg.encode())
                data = sockfd.recv(1024).decode()
                if data == 'login failed':
                    QtWidgets.QMessageBox.warning(self.form, "登录失败", "用户名或密码错误",
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                  QtWidgets.QMessageBox.Yes)
                    return 0
                elif data == 'admin login ok':  # 若管理员登录成功，则跳转到管理员登录界面
                    return 1
                elif data == 'user login ok':  # 若普通用户登录成功，则跳转到普通用户登录界面
                    QtWidgets.QMessageBox.warning(self.form, "跳转失败", "普通用户界面正在维修。。。",
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                  QtWidgets.QMessageBox.Yes)
                    return 0
            sockfd.close()

class MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.mainwindow = MainWindow
        self.pushButton.clicked.connect(lambda: self.select_staff_info(self.lineEdit.text()))
        self.pushButton_13.clicked.connect(self.clear_staff_info)
        self.pushButton_4.clicked.connect(self.add_staff_info)
        self.pushButton_3.clicked.connect(self.delete_staff_info)
        self.pushButton_2.clicked.connect(self.update_staff_info)


    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)


    #清空lineEdit内的信息
    def clear_staff_info(self):
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_21.setText("")
        self.lineEdit_22.setText("")
        self.lineEdit_23.setText("")
        self.lineEdit_24.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.comboBox_3.setCurrentIndex(0)
        self.lineEdit_25.setText("")
        self.lineEdit_26.setText("")
        self.lineEdit_11.setText("")

    #添加员工信息
    def add_staff_info(self):
        pid = self.lineEdit_2.text()
        pjid = self.lineEdit_8.text()
        pdid = self.lineEdit_9.text()
        pname = self.lineEdit_3.text()
        pgender = self.lineEdit_21.text()
        pbirth = self.lineEdit_23.text()
        pindate = self.lineEdit_24.text()
        pschoolage = self.lineEdit_22.text()
        pphone = self.lineEdit_4.text()
        paddress = self.lineEdit_5.text()
        psalary = self.lineEdit_7.text()
        phobby = self.lineEdit_6.text()
        pdept = self.lineEdit_10.text()
        status = self.comboBox_3.currentIndex()
        ppassword = self.lineEdit_11.text()
        tup = (pid, pjid, pdid, pname, pgender, pbirth,
               pindate, pschoolage, pphone, paddress,
               psalary, phobby, pdept, str(status), ppassword)
        L = (pid, pjid, pdid, pname, pgender, pschoolage, pphone, paddress,
             psalary, phobby, pdept, str(status), ppassword)
        s = 0
        for i in L:
            if i == "":
                s += 1
            if re.findall(r"\W", "".join(L)):
                s += 1
        if s > 0:
            QtWidgets.QMessageBox.warning(self.mainwindow, "添加失败", "员工信息中含有特殊符号或为空",
                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                      QtWidgets.QMessageBox.Yes)
            return 0
        tup = "As$" + "#".join(tup)
        sockfd.send(tup.encode())
        msg = sockfd.recv(1024).decode()
        if msg == "exists":
            QtWidgets.QMessageBox.warning(self.mainwindow, "添加失败", "该员工ID已存在",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)
        elif msg == "add ok":
            QtWidgets.QMessageBox.warning(self.mainwindow, "添加成功", "员工信息已添加",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)
        else:
            QtWidgets.QMessageBox.warning(self.mainwindow, "添加失败", msg,
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)


    #删除员工信息
    def delete_staff_info(self):
        pass


    def update_staff_info(self):
        pass

    #查询员工信息
    def select_staff_info(self,pid):
        if not re.match(r"^\d+$",pid):
            QtWidgets.QMessageBox.warning(self.mainwindow, "查询失败", "输入错误",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)
            return 0
        pid = "Ss$" + pid
        sockfd.send(pid.encode())
        msg = sockfd.recv(1024).decode()
        if msg == "not exists":
            QtWidgets.QMessageBox.warning(self.mainwindow, "查询失败", "查无此人",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)
        else:
            msg = msg.split("#")
            self.lineEdit_2.setText(msg[0])
            self.lineEdit_3.setText(msg[3])
            self.lineEdit_21.setText(msg[4])
            self.lineEdit_22.setText(msg[7])
            self.lineEdit_23.setText(msg[5])
            self.lineEdit_24.setText(msg[6])
            self.lineEdit_4.setText(msg[8])
            self.lineEdit_5.setText(msg[9])
            self.lineEdit_6.setText(msg[11])
            self.lineEdit_7.setText(msg[10])
            self.lineEdit_8.setText(msg[1])
            self.lineEdit_9.setText(msg[2])
            self.lineEdit_10.setText(msg[12])
            self.comboBox_3.setCurrentIndex(int(msg[15]))
            self.lineEdit_25.setText(msg[13])
            self.lineEdit_26.setText(msg[14])
            self.lineEdit_11.setText(msg[16])




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dg_01 = QtWidgets.QDialog()
    ui = Ui_Dg_01(Dg_01)
    Dg_01.show()
    sys.exit(app.exec_())

