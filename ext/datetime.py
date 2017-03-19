from PyQt5 import QtWidgets
from time import strftime


class DateTime(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self.parent = parent

        self.formats = ["%A, %d. %B %Y %H:%M",
                        "%A, %d. %B %Y",
                        "%d. %B %Y %H:%M",
                        "%d.%m.%Y %H:%M",
                        "%d. %B %Y",
                        "%d %m %Y",
                        "%d.%m.%Y",
                        "%x",
                        "%X",
                        "%H:%M"]

        self.initUI()

    def initUI(self):
        self.box = QtWidgets.QComboBox(self)

        for i in self.formats:
            self.box.addItem(strftime(i))

        insert = QtWidgets.QPushButton("Вставити", self)
        insert.clicked.connect(self.insert)

        cancel = QtWidgets.QPushButton("Відмінити", self)
        cancel.clicked.connect(self.close)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.box, 0, 0, 1, 2)
        layout.addWidget(insert, 1, 0)
        layout.addWidget(cancel, 1, 1)

        self.setGeometry(300, 300, 400, 80)
        self.setWindowTitle("Дата і час")
        self.setLayout(layout)

    def insert(self):
        cursor = self.parent.text.textCursor()
        datetime = strftime(self.formats[self.box.currentIndex()])
        cursor.insertText(datetime)
        self.close()
