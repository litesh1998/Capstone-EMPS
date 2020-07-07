from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QGroupBox, QMenu, QPushButton,QLabel, QSlider
from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout, QGridLayout, QLayout
from PyQt5.QtGui import QPainter, QColor, QPalette, QPixmap
import sys



class View (QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.centralWidget = QtWidgets.QWidget(self.parent)
        self.setWindowTitle("Music Player")
        self.setFixedSize(1000, 100)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(25,25,25))
        self.setPalette(palette)
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.songInfo())
        self.mainLayout.addLayout(self.musicBar())
        self.mainLayout.addLayout(self.options())


    def songInfo(self):
        lMain = QHBoxLayout()
        vlSub = QVBoxLayout()
        hlSub = QHBoxLayout()
        '''Set song image'''
        songImg = QLabel("IMG")
        songImg.setFixedSize(80,80)
        songImg.setStyleSheet("background-color: lightgreen;")
        path = "img/main.png"
        pic = QPixmap(path)
        like = QPushButton("+")
        like.setFixedSize(20,20)
        like.setStyleSheet("background-color: lightgreen")
        # songImg.setPixmap(pic)
        title = QLabel("This Is The Song Title")
        title.setStyleSheet("padding:2px,0px,20px,20px;color:white;font-family:'Serif'")
        artist = QLabel("Artist Name")
        artist.setStyleSheet("padding:0px,5px,20px,20px;color:white;font-family:'Serif'")
        hlSub.addWidget(title)
        hlSub.addWidget(like)
        vlSub.addLayout(hlSub)
        vlSub.addWidget(artist)
        hlSub.addStretch(0)
        lMain.addWidget(songImg)
        lMain.addLayout(vlSub)
        lMain.addStretch(0)
        lMain.setSizeConstraint(QHBoxLayout.SetFixedSize)
        return lMain

    def musicBar(self):
        lMain = QVBoxLayout()
        slUpper = QHBoxLayout()
        '''Widgets'''

        self.timeSlider = QtWidgets.QSlider(self.centralWidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        #progress_bar = QSlider()
        #progress_bar.setOrientation(Qt.Horizontal)
        self.timeSlider.setFixedSize(400,20)
        self.timeSlider.setStyleSheet("padding:")
        #Shuffel = QPushButton("Shuf")
        #Shuffel.setFixedSize(50,40)
        self.previousButton = QtWidgets.QPushButton(self.centralWidget)
        #Previous = QPushButton("Prev")
        self.previousButton.setFixedSize(50,40)
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        #Play = QPushButton("Play")
        self.playButton.setFixedSize(50,40)
        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        #next = QPushButton("Next")
        self.nextButton.setFixedSize(50,40)
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setFixedSize(50,40)


        #repeat = QPushButton("Rep")
        #repeat.setFixedSize(50,40)
        #slUpper.addWidget(Shuffel)
        slUpper.addWidget(self.previousButton)
        slUpper.addWidget(self.playButton)
        slUpper.addWidget(self.nextButton)
        slUpper.addWidget(self.stopButton)
        #slUpper.addWidget(repeat)
        slUpper.setAlignment(Qt.AlignCenter)
        lMain.addLayout(slUpper)
        lMain.addWidget(self.timeSlider)
        lMain.addStretch(1)
        self.mainLayout.addLayout(lMain)

    def options(self):
        lMain = QHBoxLayout()
        v1Sub = QVBoxLayout()
        self.volumeSlider = QtWidgets.QSlider(self.centralWidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)

        #mute_unmute = QPushButton("Vol")
        #mute_unmute.setFixedSize(50,40)
        #sound_slider = QSlider()
        #sound_slider.setOrientation(Qt.Horizontal)
        self.volumeSlider.setFixedSize(100,10)
        fullscrn = QPushButton("FullScrn")
        fullscrn.setFixedSize(50,40)
        fullscrn.clicked.connect(self.fullscreen_mode)
        #v1Sub.addWidget(mute_unmute)
        v1Sub.addWidget(self.volumeSlider)
        lMain.addLayout(v1Sub)
        lMain.addWidget(fullscrn)
        lMain.setAlignment(Qt.AlignRight)
        self.mainLayout.addLayout(lMain)

    def fullscreen_mode(self):
        self.parent.showFullScreen()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = View()
    clock.show()
    clock.setStyleSheet('''
    # QPushButton{
    #     Height: 40px;
    #     Width: 50px;
    # }
    # ''')
    sys.exit(app.exec_())
