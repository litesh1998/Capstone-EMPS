from PyQt5.QtWidgets import QApplication, QGroupBox,QMainWindow, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QScrollArea, QSplitter, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QPalette
from PyQt5.QtCore import QThreadPool
import sys
import Upper_left_pane as ULP
import Upper_right_pane as URP
import bottom_pane as BP
from time import sleep
import vlc
from functools import partial
from Worker import Worker
# from arduino import *
from client import client
from arduino import arduino
#import C:/Users/Lipi/OneDrive/Documents/GitHub/Capstone-EMPS/backend/client/caller2.py as CA

# some_file.py
import os
import sys

#insert at 1, 0 is the script path (or '' in REPL)
cwd = os.path.abspath("../")
# print(cwd)
sys.path.insert(1, os.path.join(cwd, "faceEmotionDetector"))
import faceEmotion

# from client import callfunc, play_song

# playsongs = callfunc()
# print(playsongs)

class View (QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.setWindowTitle("Music Player")
        self.setFixedSize(1025, 700)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(15,15,15))
        self.setPalette(palette)
        self.mainLayout = QVBoxLayout()
        self._centralwidget = QWidget(self)
        self.setCentralWidget(self._centralwidget)
        self._centralwidget.setLayout(self.mainLayout)
        self.upper_pane_layout = QHBoxLayout()
        self.upper_pane()
        self.mainLayout.addLayout(self.lower_pane())
        self.vlcPlaylist = []
        self.c = client()
        self.a = arduino()
        self.a.addSubscriberForUP(self.c.handlerForUp)
        self.a.addSubscriberForDOWN(self.c.handlerForDown)
        self.a.addSubscriberForLEFT(self.c.handlerForLeft)
        self.a.addSubscriberForRIGHT(self.c.handlerForRight)


    def upper_pane(self):
       
        # left_pane_layout = QVBoxLayout()
        self.middle_pane_layout = QVBoxLayout()

        # self.groupBox = QGroupBox()
        self.playlist_layout = QVBoxLayout()

        playlist_heading = QLabel("PLAYLIST")
        playlist_heading.setStyleSheet("font-size: 20px; color: #ffffff; margin-bottom: 10px;")

        self.playlist_layout.addWidget(playlist_heading)
        
        # self.groupBox.setLayout(self.playlist_layout)

        self.playlist_widget = QScrollArea()
        # self.playlist_widget.setWidget(self.groupBox)

        # # left_pane_layout.addStretch(1)
        # # right_pane_layout = QVBoxLayout()

        # playlist_layout = QVBoxLayout()

        # playlist_heading = QLabel("PLAYLIST")
        # playlist_heading.setStyleSheet("font-size: 20px; color: #ffffff; margin-bottom: 10px;")

        # playlist_widget = QScrollArea()
        # playlist_layout.addWidget(playlist_heading)

        # for song in playsongs:
        #     button = QPushButton(song['name'])
        #     # button.se
        #     i = partial(self.helloprint, song['id'])
        #     # print("i= ",i)
        #     button.clicked.connect(i)
        #     playlist_layout.addWidget(button)

        # # middle_pane_layout.addStretch(1)

        self.playlist_layout.addWidget(self.playlist_widget)


        self.middle_pane_layout.addLayout(self.playlist_layout)

        self.upper_pane_layout.addWidget(ULP.View(self))
        self.upper_pane_layout.addLayout(self.middle_pane_layout)
        self.upper_pane_layout.addWidget(URP.View())

        self.mainLayout.addLayout(self.upper_pane_layout,1)

    # def helloprint(self, songid):
    #     w = Worker(self.playSong, songid)
    #     self.threadpool.start(w)

    # def playSong(self,songid):
    #     print(songid)
    #     play_song(songid)

    def lower_pane(self):
        lay = QHBoxLayout()
        lay.addWidget(BP.View(self))
        return lay

# def quitEverything():
#     app.exec_()
#     del Worker
app = QApplication([])
window = View()
window.setStyleSheet('''
Ui_MainWindow{
    background-color: rbg(255,0,255);
}
                      ''')
window.show()
sys.exit(app.exec_())
