from PyQt5.QtWidgets import  QGridLayout ,QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QDialog):
  def __init__(self):
    super().__init__()

    self.title = 'Grid Layout'
    self.left = 500
    self.top = 200
    self.width = 500
    self.height = 250

    self.InitWindow()


  def InitWindow(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)
    self.CreateLayout()
    vbox = QVBoxLayout()
    vbox.addWidget(self.groupBox)
    self.setLayout(vbox)

    self.show()

  def CreateLayout(self):
    self.groupBox = QGroupBox('What is your Favorite Programming Language')
    gridLayout = QGridLayout()

    # Khoi tao cac component trong layout
    button = QPushButton("Python", self)
    button.setMaximumHeight(40)
    gridLayout.addWidget(button, 0, 0)

    button1 = QPushButton("C++", self)
    button1.setMaximumHeight(40)
    gridLayout.addWidget(button1, 1, 1)


    button2 = QPushButton("Javascript", self)
    button2.setMaximumHeight(40)
    gridLayout.addWidget(button2, 2, 2)


    self.groupBox.setLayout(gridLayout)






if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())