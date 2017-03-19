from PyQt5 import QtWidgets

from PyQt5 import QtGui

import re


class Find(QtWidgets.QDialog):
    def __init__(self, parent=None):

        QtWidgets.QDialog.__init__(self, parent)

        self.parent = parent

        self.lastStart = 0

        self.initUI()

    def initUI(self):

        findButton = QtWidgets.QPushButton("Знайти", self)
        findButton.clicked.connect(self.find)

        replaceButton = QtWidgets.QPushButton("Замінити", self)
        replaceButton.clicked.connect(self.replace)

        allButton = QtWidgets.QPushButton("Замінити все", self)
        allButton.clicked.connect(self.replaceAll)

        self.normalRadio = QtWidgets.QRadioButton("Тест", self)

        regexRadio = QtWidgets.QRadioButton("Регулярний вираз", self)

        self.findField = QtWidgets.QTextEdit(self)
        self.findField.resize(250, 50)

        self.replaceField = QtWidgets.QTextEdit(self)
        self.replaceField.resize(250, 50)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.findField, 1, 0, 1, 4)
        layout.addWidget(self.normalRadio, 2, 2)
        layout.addWidget(regexRadio, 2, 3)
        layout.addWidget(findButton, 2, 0, 1, 2)

        layout.addWidget(self.replaceField, 3, 0, 1, 4)
        layout.addWidget(replaceButton, 4, 0, 1, 2)
        layout.addWidget(allButton, 4, 2, 1, 2)

        self.setGeometry(300, 300, 360, 250)
        self.setWindowTitle("Знайти та замінити")
        self.setLayout(layout)

        self.normalRadio.setChecked(True)

    def find(self):

        text = self.parent.text.toPlainText()
        query = self.findField.toPlainText()

        if self.normalRadio.isChecked():
            self.lastStart = text.find(query, self.lastStart + 1)
            if self.lastStart >= 0:
                end = self.lastStart + len(query)
                self.moveCursor(self.lastStart, end)
            else:
                self.lastStart = 0
                self.parent.text.moveCursor(QtGui.QTextCursor.End)
        else:
            pattern = re.compile(query)
            match = pattern.search(text, self.lastStart + 1)
            if match:
                self.lastStart = match.start()
                self.moveCursor(self.lastStart, match.end())
            else:
                self.lastStart = 0
                self.parent.text.moveCursor(QtGui.QTextCursor.End)

    def replace(self):
        cursor = self.parent.text.textCursor()
        if cursor.hasSelection():
            cursor.insertText(self.replaceField.toPlainText())
            self.parent.text.setTextCursor(cursor)

    def replaceAll(self):

        self.lastStart = 0
        self.find()

        while self.lastStart:
            self.replace()
            self.find()

    def moveCursor(self, start, end):
        cursor = self.parent.text.textCursor()
        cursor.setPosition(start)
        cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, end - start)
        self.parent.text.setTextCursor(cursor)
