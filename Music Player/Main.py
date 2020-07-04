from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QScrollArea, QSplitter, QPushButton, QLabel
import sys
import Upper_left_pane as ULP
import Upper_right_pane as URP
import bottom_pane as BP

class View (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setFixedSize(1025, 700)
        self.mainLayout = QVBoxLayout()
        self._centralwidget = QWidget(self)
        self.setCentralWidget(self._centralwidget)
        self._centralwidget.setLayout(self.mainLayout)
        self.upper_pane()
        self.mainLayout.addLayout(self.lower_pane())
    def upper_pane(self):
        upper_pane_layout = QHBoxLayout()
        left_pane_layout = QVBoxLayout()
        middle_pane_layout = QVBoxLayout()
        right_pane_layout = QVBoxLayout()
        w1 = QLabel("HEllo")
        w2 = QLabel("HEllsdo")
        w3 = QLabel("HEllsdfo")
        w4 = QLabel("HElledfrtgyho")
        w5 = QLabel("HElledfrtgyho")
        w6 = QLabel("HElledfrtgyho")

        # left_pane_layout.addWidget(w1)
        # left_pane_layout.addWidget(w2)
        upper_pane_layout.addWidget(ULP.View())
        left_pane_layout.addStretch(1)
        middle_pane_layout.addWidget(w3)
        middle_pane_layout.addWidget(w4)
        middle_pane_layout.addStretch(1)
        upper_pane_layout.addLayout(middle_pane_layout)
        upper_pane_layout.addWidget(URP.View())

        self.mainLayout.addLayout(upper_pane_layout,1)
    def lower_pane(self):
        lay = QHBoxLayout()
        lay.addWidget(BP.View())
        return lay

app = QApplication([])
window = View()
window.setStyleSheet('''
QMainWindow{
    background-color: rbg(255,0,255);
}
                      ''')
window.show()
sys.exit(app.exec_())
