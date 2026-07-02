# Coded by Jayquon Coblentz
# Version 4.5.1


from main import CutlistCalculatorApp
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = CutlistCalculatorApp()
sys.exit(app.exec_())
