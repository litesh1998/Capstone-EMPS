from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QPushButton,QLabel,QListWidget
from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPalette, QPixmap
import sys

class View (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Try")
        self.setFixedSize(225,570)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('red'))
        self.setPalette(palette)
        self.mainlayout = QVBoxLayout()
        # self.mainlayout.addStretch(1)
        self.setLayout(self.mainlayout)
        self.mainlayout.addWidget(self.label())
        self.mainlayout.addWidget(self.list_())
        

    def label(self):
        label = QLabel("Song Queue")
        label.setStyleSheet("font-size:25px;font-family:'Serif';font-weight:bold")
        return label
    
    def list_(self):
        list_ = QListWidget()
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('red'))
        list_.setPalette(palette)
        return list_

        
        

if '__name__' == "__main__":
    app = QApplication([])
    window = View()
    window.show()
    sys.exit(app.exec_())
