"""
ZetCode PyQt5 tutorial

In this example, we receive data from
a QInputDialog dialog.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import os
import sys
# from io import open

from PyQt5 import QtWidgets, QtGui

dir_path = os.path.dirname(os.path.realpath(__file__))


class MainDialog(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

    def show_info_dialog(self):

        QtWidgets.QMessageBox.about(self, "Блокнот ++", "Автор: <a href='https://github.com/VasokKiselicya'>"
                                                        "Киселиця Василь</a>")

    def get_message_with_text(self, message):
        QtWidgets.QMessageBox.information(self, "Блокнот ++", message)

    def save_file_dialog(self, info):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Зберегти як', dir_path, filter='*.txt')
        file_name = file_name[0]

        # Cancel Pressed
        if not file_name:
            return

        if '.txt' != file_name[-4:]:
            file_name += '.txt'

        with open(file_name, 'w') as f:
            f.write(info)

        self.get_message_with_text("Файл успішно збережено")
        return file_name

    def open_file_dialog(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Відкрити файл', dir_path, filter='*.txt')

        if not file_name[0]:
            return None, None

        file = open(file_name[0])
        data = file.read()
        return data, file_name[0]

    def save_photo_dialog(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Зберегти як', dir_path, filter='*.png')
        file_name = file_name[0]

        if not file_name:
            return

        if '.png' != file_name[-4:]:
            file_name += '.png'

        return file_name

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainDialog()
    sys.exit(app.exec_())
