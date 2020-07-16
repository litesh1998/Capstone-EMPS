from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu
from PyQt5.QtWidgets import QCheckBox, QGroupBox, QMenu, QPushButton, QFileDialog
from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QPalette
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent

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
        palette.setColor(QPalette.Window, QColor(25,25,25))
        self.setPalette(palette)
        # self.mainLayout.addStretch(1)
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()

    def left_pane_upper(self):
        groupBox = QGroupBox("User Assistance")
        groupBox.setStyleSheet("color: white;")
        Btn1 = QPushButton("&PROFILE")
        Btn1.setFixedSize(175,50)
        Btn1.setStyleSheet("color: black;")
        # self.menuFIle = QtWidgets.QMenu(self)
        # self.menuFIle.setTitle("BROWSER")
        # Btn2 = QPushButton("&BROWSER")
        # self.menuFIle.setFixedSize(175,50)
        # self.menuFIle.setStyleSheet("color: black;")
        Btn2 = QPushButton("&BROWSE")
        Btn2.setFixedSize(175,50)
        Btn2.setStyleSheet("color: black;")
        Btn2.clicked.connect(self.getFile)
        # dlg = QFileDialog()
        # dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("Audio files (*.mp3 *.wav *.m4a)")
        Btn3 = QPushButton("&HISTORY")
        Btn3.setFixedSize(175,50)
        Btn3.setStyleSheet("color: black;")
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
        groupBox = QGroupBox("Your Library")
        groupBox.setStyleSheet("color: white;")
        Btn1 = QPushButton("&Recently Played")
        Btn1.setFixedSize(175,30)
        Btn1.setStyleSheet("color: black;")
        Btn2 = QPushButton("&Liked Songs")
        Btn2.setFixedSize(175,30)
        Btn2.setStyleSheet("color: black;")
        Btn3 = QPushButton("&Playlist")
        Btn3.setGeometry(0,70,175,50)
        #Btn3.setFixedSize(175,30)
        Btn3.setStyleSheet("color: black;")
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

    # Linked to Browser button (Btn2) in Upper_left_pane.py
    def getFile(self):
        song = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Audio files (*.mp3 *.wav *.m4a)")

        if song[0] != '':
            url = QUrl.fromLocalFile(song[0])
            if self.playlist.mediaCount() == 0:
                self.playlist.addMedia(QMediaContent(url))
                self.player.setPlaylist(self.playlist)
                self.player.play()
                #self.userAction =1
            else:
                self.playlist.addMedia(QMediaContent(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = View()
    clock.show()
    sys.exit(app.exec_())
