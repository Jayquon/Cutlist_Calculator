# Coded by Jayquon Coblentz
# Version 4.5.1


from PyQt5.QtWidgets import *
from cutlist_app import Ui_Cutlist_App
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
from funcs import open_xlsx, get_types, stock_calc


# Handle high resolution displays:
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class CutlistCalculatorApp(QMainWindow, Ui_Cutlist_App):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self)
        self.browse_btn.clicked.connect(self.browsefiles)
        self.load_btn.clicked.connect(self.fileload)
        self.load_btn.clicked.connect(self.board_type)
        self.calculate_btn.clicked.connect(self.calculate)

        # Remove default title bar
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set initial position of window
        self.initialPosition = self.pos()

        self.show()

        def moveApp(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.initialPosition)
                self.initialPosition = event.globalPos()
                event.accept()

        self.title_frame.mouseMoveEvent = moveApp

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, "Open XLSX", "C:", "Excel files (*.xlsx)")
        self.filename.setText(fname[0])

    def fileload(self):
        try:
            self.errors.setText("")
            list_name = open_xlsx(self.filename.text())
            self.cutlist_name.setText(list_name)
        except:
            self.errors.setText("Error: Invalid File/ Formatting")
            print("No directory")

    def board_type(self):
        types = get_types()
        self.material_type.clear()
        self.material_type.addItem("TYPE")
        self.material_type.model().item(0).setEnabled(False)
        for type in types:
            self.material_type.addItem(type)

    def calculate(self):
        stock_used = stock_calc(self.stock_len.text(), self.material_type.currentText(), int(self.quantity.text()))
        if type(stock_used) is list:
            self.errors.setText("")
            self.treated_stock.setText(f"Treated Stock: {stock_used[0]}")
            self.untreated_stock.setText(f"UnTreated Stock: {stock_used[1]}")
        else:
            self.errors.setText(f"Error: {stock_used}")
            self.treated_stock.setText("Treated Stock:")
            self.untreated_stock.setText("UnTreated Stock:")

    # Handle mouse position
    def mousePressEvent(self, event):
        self.initialPosition = event.globalPos()
