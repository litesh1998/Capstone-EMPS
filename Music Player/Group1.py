from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget)
import sys


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        left_pane = QVBoxLayout()
        left_pane.addWidget(self.createExampleGroup())
        left_pane.addWidget(self.createExampleGroup())
        self.setLayout(left_pane)
        self.setWindowTitle("PyQt5 Group Box")
        self.resize(100, 700)

    def createExampleGroup(self):
        groupBox = QGroupBox("")
        Btn1 = QPushButton("&PROFILE")
        Btn2 = QPushButton("&LIKED")
        Btn3 = QPushButton("&HISTORY")
        vbox = QVBoxLayout()
        vbox.addWidget(Btn1)
        vbox.addWidget(Btn2)
        vbox.addWidget(Btn3)
        vbox.addStretch(0)
        groupBox.setFixedSize(100,300)
        groupBox.setLayout(vbox)

        return groupBox



if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())
