# -*- coding: utf-8 -*-

import sys
import os

from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
from PyQt5.QtCore import Qt
from ext import *


class Main(QtWidgets.QMainWindow):

    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img')

    NEW = os.path.join(dir_path, 'new.png')
    OPEN = os.path.join(dir_path, 'open.png')
    SAVE = os.path.join(dir_path, 'save.png')
    SAVE_AS = os.path.join(dir_path, 'save_how.png')
    SAVE_PHOTO = os.path.join(dir_path, 'photo.png')
    PRINT = os.path.join(dir_path, 'print.png')

    DELETE = os.path.join(dir_path, 'delete.png')
    REMAKE = os.path.join(dir_path, 'remake.png')
    REPLACE = os.path.join(dir_path, 'replace.png')
    FIND = os.path.join(dir_path, 'find.png')

    COPY = os.path.join(dir_path, 'copy.png')
    CUT = os.path.join(dir_path, 'cut.png')
    PASTE = os.path.join(dir_path, 'paste.png')

    REDO = os.path.join(dir_path, 'redo.png')
    UNDO = os.path.join(dir_path, 'undo.png')
    ABOUT = os.path.join(dir_path, 'about.png')

    NOTEPAD = os.path.join(dir_path, 'notepad.png')

    CALENDAR = os.path.join(dir_path, 'calendar.png')
    CALCULATOR = os.path.join(dir_path, 'calculator.png')
    TABLE = os.path.join(dir_path, 'table.png')
    IMAGE = os.path.join(dir_path, 'image.png')
    BULLETS_LIST = os.path.join(dir_path, 'bullets_list.png')
    NUMBERS_LIST = os.path.join(dir_path, 'numbers_list.png')

    FONT_COLOR = os.path.join(dir_path, 'font_color.png')
    BACKGROUND_COLOR = os.path.join(dir_path, 'background_color.png')
    BOLD = os.path.join(dir_path, 'bold.png')
    ITALIC = os.path.join(dir_path, 'italic.png')
    UNDERSCORE = os.path.join(dir_path, 'underline.png')

    ALIGN_LEFT = os.path.join(dir_path, 'left_align.png')
    ALIGN_RIGHT = os.path.join(dir_path, 'right_align.png')
    ALIGN_CENTER = os.path.join(dir_path, 'center_align.png')
    ALIGN_JUSTIFY = os.path.join(dir_path, 'justify_align.png')

    LEFT_INDENT = os.path.join(dir_path, 'left-indent.png')
    RIGHT_INDENT = os.path.join(dir_path, 'right-indent.png')

    STRIKE = os.path.join(dir_path, 'strike.png')
    SUPERSCRIPT = os.path.join(dir_path, 'superscript.png')
    SUBSCRIPT = os.path.join(dir_path, 'subscript.png')

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.filename = ""

        self.changesSaved = True

        self.initUI()

    def initToolbar(self):

        self.newAction = QtWidgets.QAction(QtGui.QIcon(self.NEW), "Новий файл", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Створити новий документ")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon(self.OPEN), "Відкрити файл", self)
        self.openAction.setStatusTip("Відкрити існуючий документ")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon(self.SAVE), "Зберегти", self)
        self.saveAction.setStatusTip("Зберегти документ")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.printAction = QtWidgets.QAction(QtGui.QIcon(self.PRINT), "Друк", self)
        self.printAction.setStatusTip("Друк документу")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.printHandler)

        self.previewAction = QtWidgets.QAction(QtGui.QIcon(self.SAVE_PHOTO), "Попередній перегляд", self)
        self.previewAction.setStatusTip("Перегляд сторінки перед друком")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        self.findAction = QtWidgets.QAction(QtGui.QIcon(self.REPLACE), "Знайти та замінити", self)
        self.findAction.setStatusTip("Знайти та замінити слова в документі")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(find.Find(self).show)

        self.cutAction = QtWidgets.QAction(QtGui.QIcon(self.CUT), "Вирізати", self)
        self.cutAction.setStatusTip("Видалити та скопіювати текст")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtWidgets.QAction(QtGui.QIcon(self.COPY), "Копіювати", self)
        self.copyAction.setStatusTip("Копіювати текст")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtWidgets.QAction(QtGui.QIcon(self.PASTE), "Вставити", self)
        self.pasteAction.setStatusTip("Вставити раніше скопійований текст")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtWidgets.QAction(QtGui.QIcon(self.UNDO), "Скасувати", self)
        self.undoAction.setStatusTip("Скасовує останню дію")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtWidgets.QAction(QtGui.QIcon(self.REDO), "Повторити", self)
        self.redoAction.setStatusTip("Повторює останню скасовану дію")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        dateTimeAction = QtWidgets.QAction(QtGui.QIcon(self.CALENDAR), "Вставляє поточну дату та час", self)
        dateTimeAction.setStatusTip("Вставляє поточну дату та час")
        dateTimeAction.setShortcut("Ctrl+D")
        dateTimeAction.triggered.connect(datetime.DateTime(self).show)

        wordCountAction = QtWidgets.QAction(QtGui.QIcon(self.CALCULATOR),
                                            "Переглянути кількість слів та символів", self)

        wordCountAction.setStatusTip("Переглянути кількість слів та символів")
        wordCountAction.setShortcut("Ctrl+W")
        wordCountAction.triggered.connect(self.wordCount)

        tableAction = QtWidgets.QAction(QtGui.QIcon(self.TABLE), "Вставити таблицю", self)
        tableAction.setStatusTip("Вставити таблицю")
        tableAction.setShortcut("Ctrl+T")
        tableAction.triggered.connect(table.Table(self).show)

        imageAction = QtWidgets.QAction(QtGui.QIcon(self.IMAGE), "Вставити зображення", self)
        imageAction.setStatusTip("Вставити зображення")
        imageAction.setShortcut("Ctrl+Shift+I")
        imageAction.triggered.connect(self.insertImage)

        bulletAction = QtWidgets.QAction(QtGui.QIcon(self.BULLETS_LIST), "Вставити маркований список", self)
        bulletAction.setStatusTip("Вставити маркований список")
        bulletAction.setShortcut("Ctrl+Shift+B")
        bulletAction.triggered.connect(self.bulletList)

        numberedAction = QtWidgets.QAction(QtGui.QIcon(self.NUMBERS_LIST), "Вставити нумерований список", self)
        numberedAction.setStatusTip("Вставити нумерований список")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)

        self.toolbar = self.addToolBar("Налаштування")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.findAction)
        self.toolbar.addAction(dateTimeAction)
        self.toolbar.addAction(wordCountAction)
        self.toolbar.addAction(tableAction)
        self.toolbar.addAction(imageAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)

        self.addToolBarBreak()

    def initFormatbar(self):

        fontBox = QtWidgets.QFontComboBox(self)
        fontBox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))

        fontSize = QtWidgets.QSpinBox(self)

        fontSize.setSuffix(" pt")

        fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))

        fontSize.setValue(14)

        fontColor = QtWidgets.QAction(QtGui.QIcon(self.FONT_COLOR), "Змінити колір тексту", self)
        fontColor.triggered.connect(self.fontColorChanged)

        boldAction = QtWidgets.QAction(QtGui.QIcon(self.BOLD), "Жирний", self)
        boldAction.triggered.connect(self.bold)

        italicAction = QtWidgets.QAction(QtGui.QIcon(self.ITALIC), "Курсив", self)
        italicAction.triggered.connect(self.italic)

        underlAction = QtWidgets.QAction(QtGui.QIcon(self.UNDERSCORE), "Підкреслений", self)
        underlAction.triggered.connect(self.underline)

        strikeAction = QtWidgets.QAction(QtGui.QIcon(self.STRIKE), "Закреслений", self)
        strikeAction.triggered.connect(self.strike)

        superAction = QtWidgets.QAction(QtGui.QIcon(self.SUPERSCRIPT), "Надрядковий", self)
        superAction.triggered.connect(self.superScript)

        subAction = QtWidgets.QAction(QtGui.QIcon(self.SUBSCRIPT), "Підрядковий", self)
        subAction.triggered.connect(self.subScript)

        alignLeft = QtWidgets.QAction(QtGui.QIcon(self.ALIGN_LEFT), "Вирівнювання по лівому краю", self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QtWidgets.QAction(QtGui.QIcon(self.ALIGN_CENTER), "Вирівнювання по центру", self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QtWidgets.QAction(QtGui.QIcon(self.ALIGN_RIGHT), "Вирівнювання по правому краю", self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QtWidgets.QAction(QtGui.QIcon(self.ALIGN_JUSTIFY), "Вирівнювання по ширині рядка", self)
        alignJustify.triggered.connect(self.alignJustify)

        indentAction = QtWidgets.QAction(QtGui.QIcon(self.RIGHT_INDENT), "Добавити відступ", self)
        indentAction.setShortcut("Ctrl+Tab")
        indentAction.triggered.connect(self.indent)

        dedentAction = QtWidgets.QAction(QtGui.QIcon(self.LEFT_INDENT), "Видалити відступ", self)
        dedentAction.setShortcut("Shift+Tab")
        dedentAction.triggered.connect(self.dedent)

        backColor = QtWidgets.QAction(QtGui.QIcon(self.BACKGROUND_COLOR), "Змінити колір фону", self)
        backColor.triggered.connect(self.highlight)

        self.formatbar = self.addToolBar("Форматування")

        self.formatbar.addWidget(fontBox)
        self.formatbar.addWidget(fontSize)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)

        self.formatbar.addSeparator()

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)
        self.formatbar.addAction(strikeAction)
        self.formatbar.addAction(superAction)
        self.formatbar.addAction(subAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)

        self.formatbar.addSeparator()

        self.formatbar.addAction(indentAction)
        self.formatbar.addAction(dedentAction)

    def initMenubar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("Файл")
        edit = menubar.addMenu("Редагування")
        view = menubar.addMenu("Налаштування")
        about = menubar.addMenu("Інформація")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        edit.addAction(self.findAction)

        toolbarAction = QtWidgets.QAction("Головна панель", self)
        toolbarAction.triggered.connect(self.toggleToolbar)

        formatbarAction = QtWidgets.QAction("Панель форматуавння", self)
        formatbarAction.triggered.connect(self.toggleFormatbar)

        statusbarAction = QtWidgets.QAction("Інформаційна панель", self)
        statusbarAction.triggered.connect(self.toggleStatusbar)

        infoAction = QtWidgets.QAction("Про Блокнот++", self)
        infoAction.setShortcut("F1")
        infoAction.triggered.connect(self.show_info_dialog)

        view.addAction(toolbarAction)
        view.addAction(formatbarAction)
        view.addAction(statusbarAction)

        about.addAction(infoAction)

    def show_info_dialog(self):
        QtWidgets.QMessageBox.about(self, "Блокнот ++", "Автор: <a href='https://github.com/VasokKiselicya'>"
                                                        "Киселиця Василь</a>")

    def initUI(self):

        self.text = QtWidgets.QTextEdit(self)

        self.text.setTabStopWidth(33)

        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        self.setCentralWidget(self.text)

        self.statusbar = self.statusBar()

        self.text.cursorPositionChanged.connect(self.cursorPosition)

        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.context)

        self.text.textChanged.connect(self.changed)

        self.setGeometry(200, 50, 800, 600)
        self.setWindowTitle("Блокнот ++")
        self.setWindowIcon(QtGui.QIcon("img/notepad.png"))

    def changed(self):
        self.changesSaved = False

    def closeEvent(self, event):

        if self.changesSaved:

            event.accept()

        else:

            popup = QtWidgets.QMessageBox(self)

            popup.setIcon(QtWidgets.QMessageBox.Warning)
            popup.setWindowTitle("Блокнот++")

            popup.setText("Додкумент змнінено!")

            popup.setInformativeText("Ви бажаєте зберегти зміни?")

            popup.setStandardButtons(QtWidgets.QMessageBox.Save |
                                     QtWidgets.QMessageBox.Cancel |
                                     QtWidgets.QMessageBox.Discard)

            popup.setDefaultButton(QtWidgets.QMessageBox.Save)

            answer = popup.exec_()

            if answer == QtWidgets.QMessageBox.Save:
                self.save()

            elif answer == QtWidgets.QMessageBox.Discard:
                event.accept()

            else:
                event.ignore()

    def context(self, pos):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        if table:

            menu = QtWidgets.QMenu(self)

            appendRowAction = QtWidgets.QAction("Додати рядок", self)
            appendRowAction.triggered.connect(lambda: table.appendRows(1))

            appendColAction = QtWidgets.QAction("Додати колонку", self)
            appendColAction.triggered.connect(lambda: table.appendColumns(1))

            removeRowAction = QtWidgets.QAction("Видалити рядок", self)
            removeRowAction.triggered.connect(self.removeRow)

            removeColAction = QtWidgets.QAction("Видалити колонку", self)
            removeColAction.triggered.connect(self.removeCol)

            insertRowAction = QtWidgets.QAction("Вставити рядок", self)
            insertRowAction.triggered.connect(self.insertRow)

            insertColAction = QtWidgets.QAction("Вставити колонку", self)
            insertColAction.triggered.connect(self.insertCol)

            mergeAction = QtWidgets.QAction("Об'єднати колонки", self)
            mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

            if not cursor.hasSelection():
                mergeAction.setEnabled(False)

            splitAction = QtWidgets.QAction("Split cells", self)

            cell = table.cellAt(cursor)

            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                splitAction.triggered.connect(lambda: table.splitCell(cell.row(), cell.column(), 1, 1))

            else:
                splitAction.setEnabled(False)

            menu.addAction(appendRowAction)
            menu.addAction(appendColAction)

            menu.addSeparator()

            menu.addAction(removeRowAction)
            menu.addAction(removeColAction)

            menu.addSeparator()

            menu.addAction(insertRowAction)
            menu.addAction(insertColAction)

            menu.addSeparator()

            menu.addAction(mergeAction)
            menu.addAction(splitAction)

            pos = self.mapToGlobal(pos)

            if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)

            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)

            menu.move(pos)

            menu.show()

        else:

            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse, QtCore.QPoint())

            self.text.contextMenuEvent(event)

    def removeRow(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.removeRows(cell.row(), 1)

    def removeCol(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.removeColumns(cell.column(), 1)

    def insertRow(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.insertRows(cell.row(), 1)

    def insertCol(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.insertColumns(cell.column(), 1)

    def toggleToolbar(self):

        state = self.toolbar.isVisible()

        self.toolbar.setVisible(not state)

    def toggleFormatbar(self):

        state = self.formatbar.isVisible()

        self.formatbar.setVisible(not state)

    def toggleStatusbar(self):

        state = self.statusbar.isVisible()

        self.statusbar.setVisible(not state)

    def new(self):

        spawn = Main()

        spawn.show()

    def open(self):

        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Відкрити файл', ".", "(*.writer)")[0]

        if self.filename:
            with open(self.filename, "rt") as file:
                self.text.setText(file.read())

    def save(self):

        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Зберегти файл')[0]

        if self.filename:

            if not self.filename.endswith(".writer"):
                self.filename += ".writer"

            with open(self.filename, "wt") as file:
                file.write(self.text.toHtml())

            self.changesSaved = True

    def preview(self):

        preview = QtPrintSupport.QPrintPreviewDialog()

        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def printHandler(self):

        dialog = QtPrintSupport.QPrintDialog()

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def cursorPosition(self):

        cursor = self.text.textCursor()

        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Рядок: {} | Символ: {}".format(line, col))

    def wordCount(self):

        wc = wordcount.WordCount(self)

        wc.getText()

        wc.show()

    def insertImage(self):

        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Вставити зображення', ".", "Images (*.png *.xpm *.jpg *.bmp *.gif)")[0]

        if filename:

            image = QtGui.QImage(filename)

            if image.isNull():

                popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                              "Виникла помилка!",
                                              "Неможливо завантажити дане зображення",
                                              QtWidgets.QMessageBox.Ok,
                                              self)
                popup.show()

            else:

                cursor = self.text.textCursor()

                cursor.insertImage(image, filename)

    def fontColorChanged(self):

        color = QtWidgets.QColorDialog.getColor()

        self.text.setTextColor(color)

    def highlight(self):

        color = QtWidgets.QColorDialog.getColor()

        self.text.setTextBackgroundColor(color)

    def bold(self):

        if self.text.fontWeight() == QtGui.QFont.Bold:

            self.text.setFontWeight(QtGui.QFont.Normal)

        else:

            self.text.setFontWeight(QtGui.QFont.Bold)

    def italic(self):

        state = self.text.fontItalic()

        self.text.setFontItalic(not state)

    def underline(self):

        state = self.text.fontUnderline()

        self.text.setFontUnderline(not state)

    def strike(self):

        fmt = self.text.currentCharFormat()

        fmt.setFontStrikeOut(not fmt.fontStrikeOut())

        self.text.setCurrentCharFormat(fmt)

    def superScript(self):

        fmt = self.text.currentCharFormat()

        align = fmt.verticalAlignment()

        if align == QtGui.QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)

        else:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        self.text.setCurrentCharFormat(fmt)

    def subScript(self):

        fmt = self.text.currentCharFormat()

        align = fmt.verticalAlignment()

        if align == QtGui.QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)

        else:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        self.text.setCurrentCharFormat(fmt)

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def indent(self):

        cursor = self.text.textCursor()

        if cursor.hasSelection():

            temp = cursor.blockNumber()

            cursor.setPosition(cursor.anchor())

            diff = cursor.blockNumber() - temp

            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            for n in range(abs(diff) + 1):
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)
                cursor.insertText("\t")
                cursor.movePosition(direction)
        else:
            cursor.insertText("\t")

    def handleDedent(self, cursor):

        cursor.movePosition(QtGui.QTextCursor.StartOfLine)
        line = cursor.block().text()

        if line.startswith("\t"):
            cursor.deleteChar()
        else:
            for char in line[:8]:
                if char != " ":
                    break
                cursor.deleteChar()

    def dedent(self):

        cursor = self.text.textCursor()

        if cursor.hasSelection():
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.anchor())

            diff = cursor.blockNumber() - temp

            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            for n in range(abs(diff) + 1):
                self.handleDedent(cursor)
                cursor.movePosition(direction)
        else:
            self.handleDedent(cursor)

    def bulletList(self):

        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):

        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)


def main():
    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
