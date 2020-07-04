from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QCheckBox, QGroupBox, QMenu, QPushButton
from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QPalette

import sys
class View (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setFixedWidth(225)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.left_pane_upper())
        self.mainLayout.addWidget(self.left_pane_middle())
        self.mainLayout.addWidget(self.left_pane_bottom())
        self.setLayout(self.mainLayout)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('red'))
        self.setPalette(palette)
        # self.mainLayout.addStretch(1)

    def left_pane_upper(self):
        groupBox = QGroupBox("User Assistance")
        Btn1 = QPushButton("&PROFILE")
        Btn1.setFixedSize(175,50)
        Btn2 = QPushButton("&BROWSER")
        Btn2.setFixedSize(175,50)
        Btn3 = QPushButton("&HISTORY")
        Btn3.setFixedSize(175,50)
        vbox = QVBoxLayout()
        vbox.addWidget(Btn1)
        vbox.addWidget(Btn2)
        vbox.addWidget(Btn3)
        vbox.addStretch(0)
        groupBox.setFixedWidth(200)
        groupBox.setMinimumHeight(220)
        groupBox.setLayout(vbox)
        return groupBox

    def left_pane_middle(self):
        groupBox = QGroupBox("Your Liberary")
        Btn1 = QPushButton("&Recently Played")
        Btn1.setFixedSize(175,30)
        Btn2 = QPushButton("&Liked")
        Btn2.setFixedSize(175,30)
        Btn3 = QPushButton("&Playlist")
        Btn3.setFixedSize(175,30)
        vbox = QVBoxLayout()
        vbox.addWidget(Btn1)
        vbox.addWidget(Btn2)
        vbox.addWidget(Btn3)
        groupBox.setFixedWidth(200)
        groupBox.setMinimumHeight(300)
        vbox.addStretch(0)
        groupBox.setLayout(vbox)
        return groupBox

    def left_pane_bottom(self):
        NewPlaylist = QPushButton("New Playlist")
        NewPlaylist.setFixedSize(200,50)
        return NewPlaylist




if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = View()
    clock.show()
    sys.exit(app.exec_())
