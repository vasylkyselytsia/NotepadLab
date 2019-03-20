from PyQt5 import QtCore, QtGui, QtWidgets


class UI(object):

    def __init__(self):
        self.button_box = None
        self.text_input = None
        self.list_widget = None
        self.clear_btn = None
        self.add_btn = None

    def setup_ui(self, my_ui):
        my_ui.setObjectName('name')
        my_ui.resize(411, 247)
        self.button_box = QtWidgets.QDialogButtonBox(my_ui)
        self.button_box.setGeometry(QtCore.QRect(20, 210, 381, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close)

    def translate_ui(self, mu_id, title='Лабораторна робота №1'):
        _translate = QtCore.QCoreApplication.translate
        mu_id.setWindowTitle(_translate(p_str="name", p_str_1=title))
        self.clear_btn.setText()
