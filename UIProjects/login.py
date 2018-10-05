# -*- coding: utf-8 -*-

"""
Module implementing Dg_01.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
import sys

from Ui_login import Ui_Dg_01




class Dg_01(QDialog, Ui_Dg_01):
    def __init__(self, parent=None):
        super(Dg_01, self).__init__(parent)
        self.setupUi(self)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dg_01 = QDialog()
    ui = Ui_Dg_01()
    ui.setupUi(Dg_01)
    Dg_01.show()
    sys.exit(app.exec_())