from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
class Window(QMainWindow, QDialog):
  def __init__(self):
    super().__init__()
    self.title = "Minh Chien"
    self.top = 100
    self.left = 100
    self.width = 800
    self.height = 300

    self.UiButtons(QRect(100, 100, 111, 50))
    self.UiButtons(QRect(50, 20, 111, 50))
    self.InitWindow()

  def UiButtons(self, location = None):
    button = QPushButton('Click me!', self)
    # button.move(50, 50)
    button.setGeometry(location)
    button.setIcon(QtGui.QIcon('home.jpg'))
    button.setIconSize(QtCore.QSize(50, 50))
    button.setToolTip('This is click me button') # hien thi khi di chuyen chuot vao buttuon
    button.clicked.connect(self.clickMe)

  def create_layout(self):
    self.groupBox = QGroupBox("This is Your Favorite Singer")
    hboxlayout = QHBoxLayout()
    

  def clickMe(self):
    print('Hello world')
    sys.exit()

  def InitWindow(self):
    # self.setWindowIcon(QtGui.QIcon('home.jpg'))
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())