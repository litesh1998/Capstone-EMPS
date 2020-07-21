from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget
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
#import C:/Users/Lipi/OneDrive/Documents/GitHub/Capstone-EMPS/backend/client/caller2.py as CA

# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, 'C:/Users/Lipi/OneDrive/Documents/GitHub/Capstone-EMPS/backend/client')
from client import callfunc, play_song

playsongs = callfunc()
print(playsongs)

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
        self.upper_pane()
        self.mainLayout.addLayout(self.lower_pane())
    def upper_pane(self):
        upper_pane_layout = QHBoxLayout()
        # left_pane_layout = QVBoxLayout()
        middle_pane_layout = QVBoxLayout()

        # left_pane_layout.addStretch(1)
        # right_pane_layout = QVBoxLayout()

        playlist_layout = QVBoxLayout()

        playlist_heading = QLabel("PLAYLIST")
        playlist_heading.setStyleSheet("font-size: 20px; color: #ffffff; margin-bottom: 10px;")

        playlist_widget = QScrollArea()
        
        for song in playsongs:
            button = QPushButton(song['name'])
            # button.se
            i = partial(self.helloprint, song['id'])
            # print("i= ",i)
            button.clicked.connect(i)
            playlist_layout.addWidget(button)

        # middle_pane_layout.addStretch(1)
        playlist_layout.addWidget(playlist_heading)

        playlist_layout.addWidget(playlist_widget)

        middle_pane_layout.addLayout(playlist_layout)

        upper_pane_layout.addWidget(ULP.View())
        upper_pane_layout.addLayout(middle_pane_layout)
        upper_pane_layout.addWidget(URP.View())

        self.mainLayout.addLayout(upper_pane_layout,1)

    def helloprint(self, songid):
        w = Worker(self.playSong, songid)
        self.threadpool.start(w)

    def playSong(self,songid):
        print(songid)
        play_song(songid)

    def lower_pane(self):
        lay = QHBoxLayout()
        lay.addWidget(BP.View(self))
        return lay

app = QApplication([])
window = View()
window.setStyleSheet('''
Ui_MainWindow{
    background-color: rbg(255,0,255);
}
                      ''')
window.show()
sys.exit(app.exec_())
