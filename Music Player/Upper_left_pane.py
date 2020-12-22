from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *

from client import callfunc, play_song
from functools import partial
from Worker import Worker
import os, sys, time

cwd = os.path.abspath("../")
sys.path.insert(1, os.path.join(cwd, "faceEmotionDetector"))

import faceEmotion

class View (QWidget):
    def __init__(self, parent):
        super().__init__()
        self.main = parent
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
        
        detect = QPushButton("&Detect")
        detect.setFixedSize(175,30)
        detect.setStyleSheet("color: black;")
        detect.clicked.connect(self.detect)

        vbox = QVBoxLayout()
        vbox.addWidget(Btn1)
        vbox.addWidget(Btn2)
        vbox.addWidget(Btn3)
        vbox.addWidget(detect)

        groupBox.setFixedWidth(200)
        groupBox.setMinimumHeight(300)
        vbox.addStretch(0)
        groupBox.setLayout(vbox)
        return groupBox

    def detect(self):
        faceEmotion.faceEmotion()
        emotion = faceEmotion.returnEmotion()
        
        # print(emotion);
        playsongs = callfunc(emotion)


        

        # left_pane_layout.addStretch(1)
        # right_pane_layout = QVBoxLayout()

        # playlist_layout = QVBoxLayout()

        # playlist_heading = QLabel("PLAYLIST")
        # playlist_heading.setStyleSheet("font-size: 20px; color: #ffffff; margin-bottom: 10px;")

        # playlist_widget = QScrollArea()
        # playlist_layout.addWidget(playlist_heading)
        for song in playsongs:
            button = QPushButton(song['name'])
            # button.se
            i = partial(self.helloprint, song['id'])
            # print("i= ",i)
            button.clicked.connect(i)
            self.main.playlist_layout.addWidget(button)

        # self.main.playlist_widget.setWidget(self.main.playlist_layout)
        # middle_pane_layout.addStretch(1)


        self.main.playlist_layout.addWidget(self.main.playlist_widget)

        self.main.middle_pane_layout.addLayout(self.main.playlist_layout)
        self.main.upper_pane_layout.addLayout(self.main.middle_pane_layout)


    def helloprint(self, songid):
        w = Worker(self.playSong, songid)
        self.main.threadpool.start(w)

    def playSong(self,songid):
        print(songid)
        play_song(songid)

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
