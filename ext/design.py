import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport

from ext.open_dialog import MainDialog

dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img')


class UIMainWindow:

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

    def __init__(self):
        self.central_widget = None
        self.horizontal_layout = None
        self.text_edit = None
        self.status_bar = None
        self.main_tool_bar = None
        self.menu_bar = None
        self.menu_about = None
        self.menu_edit = None
        self.menu_file = None

        self.action_new = None
        self.action_open = None
        self.action_save = None
        self.action_save_as = None
        self.action_save_photo = None
        self.action_print = None

        self.action_replace = None
        self.action_remake = None
        self.action_find = None
        self.action_delete = None

        self.action_copy = None
        self.action_cut = None
        self.action_paste = None
        self.action_color = None
        self.action_background_color = None
        self.action_background_edit_color = None
        self.action_font = None
        self.action_undo = None
        self.action_redo = None

        self.action_about_notepad = None

        self.file_path = ''
        self.dialog = MainDialog()
        self.value_of_copy = None

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(513, 361)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontal_layout.setContentsMargins(11, 11, 11, 11)
        self.horizontal_layout.setSpacing(6)
        self.horizontal_layout.setObjectName("horizontal_layout")

        self.text_edit = QtWidgets.QTextEdit(self.central_widget)
        self.text_edit.setObjectName("text_edit")

        self.horizontal_layout.addWidget(self.text_edit)

        main_window.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 513, 21))
        self.menu_bar.setObjectName("menuBar")

        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menuFile")

        self.menu_edit = QtWidgets.QMenu(self.menu_bar)
        self.menu_edit.setObjectName("menuEdit")

        self.menu_about = QtWidgets.QMenu(self.menu_bar)
        self.menu_about.setObjectName("menuAbout")

        main_window.setMenuBar(self.menu_bar)

        self.main_tool_bar = QtWidgets.QToolBar(main_window)
        self.main_tool_bar.setMovable(True)
        self.main_tool_bar.setObjectName("mainToolBar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.main_tool_bar)

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("statusBar")
        main_window.setStatusBar(self.status_bar)

        self.action_new = QtWidgets.QAction(main_window)
        self.action_new.setEnabled(True)
        self.action_new.setIcon(QtGui.QIcon(self.NEW))
        self.action_new.setObjectName("actionNew")
        self.action_new.setShortcut('Ctrl+N')
        self.action_new.triggered.connect(lambda x: self.on_triggered(self.action_new.objectName()))

        self.action_open = QtWidgets.QAction(main_window)
        self.action_open.setIcon(QtGui.QIcon(self.OPEN))
        self.action_open.setObjectName("actionOpen")
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.triggered.connect(lambda x: self.on_triggered(self.action_open.objectName()))

        self.action_save = QtWidgets.QAction(main_window)
        self.action_save.setIcon(QtGui.QIcon(self.SAVE))
        self.action_save.setObjectName("actionSave")
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.triggered.connect(lambda x: self.on_triggered(self.action_save.objectName()))

        self.action_save_as = QtWidgets.QAction(main_window)
        self.action_save_as.setIcon(QtGui.QIcon(self.SAVE_AS))
        self.action_save_as.setObjectName("actionSave_as")
        self.action_save_as.setShortcut('Ctrl+Shift+S')
        self.action_save_as.triggered.connect(lambda x: self.on_triggered(self.action_save_as.objectName()))

        self.action_save_photo = QtWidgets.QAction(main_window)
        self.action_save_photo.setIcon(QtGui.QIcon(self.SAVE_PHOTO))
        self.action_save_photo.setObjectName("saveAsPhoto")
        self.action_save_photo.setShortcut('Ctrl+B')
        self.action_save_photo.triggered.connect(lambda x: self.on_triggered(self.action_save_photo.objectName()))

        self.action_find = QtWidgets.QAction(main_window)
        self.action_find.setIcon(QtGui.QIcon(self.FIND))
        self.action_find.setObjectName("actionFind")
        self.action_find.setShortcut('Ctrl+Shift+F')
        self.action_find.triggered.connect(lambda x: self.on_triggered(self.action_find.objectName()))

        self.action_replace = QtWidgets.QAction(main_window)
        self.action_replace.setIcon(QtGui.QIcon(self.REPLACE))
        self.action_replace.setObjectName("actionReplace")
        self.action_replace.setShortcut('Ctrl+Shift+R')
        self.action_replace.triggered.connect(lambda x: self.on_triggered(self.action_replace.objectName()))

        self.action_remake = QtWidgets.QAction(main_window)
        self.action_remake.setIcon(QtGui.QIcon(self.REMAKE))
        self.action_remake.setObjectName("actionRemake")
        self.action_remake.setShortcut('Ctrl+Shift+M')
        self.action_remake.triggered.connect(lambda x: self.on_triggered(self.action_remake.objectName()))

        self.action_delete = QtWidgets.QAction(main_window)
        self.action_delete.setIcon(QtGui.QIcon(self.DELETE))
        self.action_delete.setObjectName("actionDelete")
        self.action_delete.setShortcut('Ctrl+Shift+D')
        self.action_delete.triggered.connect(lambda x: self.on_triggered(self.action_delete.objectName()))

        self.action_cut = QtWidgets.QAction(main_window)
        self.action_cut.setIcon(QtGui.QIcon(self.CUT))
        self.action_cut.setObjectName("actionCut")
        self.action_cut.setShortcut('Ctrl+X')

        self.action_copy = QtWidgets.QAction(main_window)
        self.action_copy.setIcon(QtGui.QIcon(self.COPY))
        self.action_copy.setObjectName("actionCopy")
        self.action_copy.setShortcut('Ctrl+C')

        self.action_paste = QtWidgets.QAction(main_window)
        self.action_paste.setIcon(QtGui.QIcon(self.PASTE))
        self.action_paste.setObjectName("actionPaste")
        self.action_paste.setShortcut('Ctrl+V')

        self.action_redo = QtWidgets.QAction(main_window)
        self.action_redo.setIcon(QtGui.QIcon(self.REDO))
        self.action_redo.setObjectName("actionRedo")
        self.action_redo.setShortcut('Ctrl+Z')

        self.action_undo = QtWidgets.QAction(main_window)
        self.action_undo.setIcon(QtGui.QIcon(self.UNDO))
        self.action_undo.setObjectName("actionUndo")
        self.action_undo.setShortcut('Ctrl+Shift+Z')

        self.action_about_notepad = QtWidgets.QAction(main_window)
        self.action_about_notepad.setEnabled(True)
        self.action_about_notepad.setIcon(QtGui.QIcon(self.ABOUT))
        self.action_about_notepad.setObjectName("actionAbout_Notepad")
        self.action_about_notepad.setShortcut('F1')
        self.action_about_notepad.triggered.connect(lambda x: self.on_triggered(
            self.action_about_notepad.objectName()))

        self.action_font = QtWidgets.QAction(main_window)
        self.action_font.setObjectName("actionFont")

        self.action_color = QtWidgets.QAction(main_window)
        self.action_color.setObjectName("actionColor")

        self.action_background_color = QtWidgets.QAction(main_window)
        self.action_background_color.setObjectName("actionBackground_Color")

        self.action_background_edit_color = QtWidgets.QAction(main_window)
        self.action_background_edit_color.setObjectName("actionBackgroung_Color_Edit_Text")

        self.action_print = QtWidgets.QAction(main_window)
        self.action_print.setIcon(QtGui.QIcon(self.PRINT))
        self.action_print.setObjectName("actionPrint")
        self.action_print.setShortcut('Ctrl+P')
        self.action_print.triggered.connect(lambda x: self.on_triggered(
            self.action_print.objectName()))

        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addAction(self.action_save_photo)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_find)
        self.menu_file.addAction(self.action_replace)
        self.menu_file.addAction(self.action_remake)
        self.menu_file.addAction(self.action_delete)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_print)

        self.menu_edit.addAction(self.action_cut)
        self.menu_edit.addAction(self.action_copy)
        self.menu_edit.addAction(self.action_paste)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_redo)
        self.menu_edit.addAction(self.action_undo)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_font)
        self.menu_edit.addAction(self.action_color)
        self.menu_edit.addAction(self.action_background_color)
        self.menu_edit.addAction(self.action_background_edit_color)

        self.menu_about.addAction(self.action_about_notepad)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_edit.menuAction())
        self.menu_bar.addAction(self.menu_about.menuAction())

        self.main_tool_bar.addAction(self.action_new)
        self.main_tool_bar.addAction(self.action_open)
        self.main_tool_bar.addAction(self.action_save)
        self.main_tool_bar.addAction(self.action_save_as)
        self.main_tool_bar.addAction(self.action_save_photo)
        self.main_tool_bar.addAction(self.action_print)

        self.main_tool_bar.addSeparator()
        self.main_tool_bar.addAction(self.action_cut)
        self.main_tool_bar.addAction(self.action_paste)
        self.main_tool_bar.addSeparator()
        self.main_tool_bar.addAction(self.action_about_notepad)

        self.translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def actionAbout_Notepad(self):
        self.dialog.show_info_dialog()

    # def actionCopy(self):
    #     self.value_of_copy =

    def actionSave_as(self):
        self.dialog.save_file_dialog(self.text_edit.toPlainText())

    def actionSave(self):
        if self.file_path:
            with open(self.file_path, 'w') as f:
                f.write(self.text_edit.toPlainText())
        else:
            self.file_path = self.dialog.save_file_dialog(self.text_edit.toPlainText())

    def actionOpen(self):
        data, file_name = self.dialog.open_file_dialog()

        if file_name:
            return

        self.text_edit.setText(data)
        self.file_path = file_name

    def saveAsPhoto(self):
        path = self.dialog.save_photo_dialog()

        if not path:
            return

        screen = self.text_edit.grab()
        screen.save(path)
        self.dialog.get_message_with_text("Фото успішно збережено")

    def actionNew(self):
        self.text_edit.setText('')
        self.file_path = ''

    def actionPrint(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        screen = self.text_edit.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()

    def on_triggered(self, *args, **kwargs):

        if not args:
            return

        action = args[0]

        print(args, kwargs)

        if hasattr(self, action):
            method = getattr(self, action)
            method()
        else:
            return

    def translate_ui(self, main_window):
        # _translate = QtCore.QCoreApplication.translate
        # main_window.setWindowTitle(_translate("main_window", "Лабораторна робота №1"))
        main_window.setWindowTitle("Лабораторна робота №1")
        self.menu_file.setTitle("Файл")
        self.menu_edit.setTitle("Змінити")
        self.menu_about.setTitle("Інформація")
        self.action_new.setText("Створити")
        self.action_open.setText("Відкрити")
        self.action_save.setText("Зберегти")
        self.action_save_as.setText("Зберегти як")
        self.action_save_photo.setText("Зберегти текст як картинку")
        self.action_find.setText("Знайти")
        self.action_replace.setText("Замінити")
        self.action_remake.setText("Перетворити")
        self.action_delete.setText("Видалити")
        self.action_cut.setText("Вирізати")
        self.action_copy.setText("Копіювати")
        self.action_paste.setText("Вставити")
        self.action_redo.setText("Скасувати")
        self.action_undo.setText("Повторити")
        self.action_about_notepad.setText("Про Notepad")
        self.action_font.setText("Шрифт")
        self.action_color.setText("Колір")
        self.action_background_color.setText("Колір фону")
        self.action_background_edit_color.setText("Колір фону редагованого тексту")
        self.action_print.setText("Друк")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    ui = UIMainWindow()
    ui.setup_ui(window)

    window.setWindowIcon(QtGui.QIcon(ui.NOTEPAD))
    app.setWindowIcon(QtGui.QIcon(ui.NOTEPAD))

    window.show()

    sys.exit(app.exec_())
