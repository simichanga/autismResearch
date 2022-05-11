from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import randint
import index
#import speech
import sys

#class AnotherWindow(QWidget):
#    def __init__(self):
#       super().__init__()
#        layout = QVBoxLayout()
#        self.label = QLabel("Welcome To Guess The Word Game!" )
#        layout.addWidget(self.label)
#        self.setLayout(layout)
#        self.setWindowTitle("Guess The Word Game!")
#        self.setGeometry(500,500,900,500)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #self.setGeometry(500, 500, 900, 500)
        self.resize(1500,900)
        self.setWindowTitle("My window")
        self.label = QtWidgets.QLabel()
        self.w = None
        self.button1 = QtWidgets.QPushButton()
        self.button2 = QtWidgets.QPushButton()
        self.button3 = QtWidgets.QPushButton()
        self.iniUI()

    # Buttons
    def iniUI(self):
        w = QtWidgets.QWidget()
        self.setCentralWidget(w)
        grid = QtWidgets.QGridLayout(w)

        self.button1.setText("Press Here To Talk")
        self.button1.setMinimumWidth(150)
        self.button1.setFont(QFont("Arial", 15))
        self.button1.setStyleSheet("background-color: 	#191970")
        #self.button1.clicked.connect(speech)
        
        self.button2.setText("Press Here To Write")
        self.button2.setFont(QFont("Arial", 15))
        self.button2.setStyleSheet("background-color: #87CEFA")
        #self.button2.clicked.connect( the option to write instead of speaking)

        self.button3.setText("Press Here To Start The Game")
        self.button3.setFont(QFont("Arial",15))
        self.button3.setStyleSheet("background-color: #6495ED")
        self.button3.clicked.connect(self.show_new_window)
        
        grid.addWidget(self.button1, 0, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        grid.addWidget(self.button2, 0, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        grid.addWidget(self.button3, 0, 1, QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = start_main_page()
        self.w.show()
picture= """
    MainWindow {
        background-image: url("C:/Users/Alexa/Documents/GitHub/autismResearch/interface/neural.png");
        background-repeat: no-repeat;
        background-position: center;
    }
"""

def window():
    app = QApplication(sys.argv)
    app.setStyleSheet(picture)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

window()
