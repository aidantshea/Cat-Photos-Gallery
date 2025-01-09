"""
this is the main application script
"""

import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

basedir: str = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cat Application Meow")

        widget = QLabel()
        widget.setPixmap(QPixmap(os.path.join(basedir, "CatImages", "Image206.jpeg")))
        self.setCentralWidget(widget)


# initiate execution stack
app = QApplication([])
window = MainWindow()
window.show()
app.exec()