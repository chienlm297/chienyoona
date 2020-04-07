from PyQt5.QtWidgets import QLabel, QGridLayout ,QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QDialog):
  def __init__(self):
    super().__init__()

    self.title = 'Qlabel'
    self.left = 500
    self.top = 200
    self.width = 500
    self.height = 250

    self.InitWindow()

  def InitWindow(self):
    self.setWindowIcon(QtGui.QIcon('home.jpg'))
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    vbox = QVBoxLayout()
    label = QLabel("This is PyQt5 Label")
    vbox.addWidget(label)

    label1 = QLabel("This is my app PyQt5")
    label1.setStyleSheet('color:red')
    vbox.addWidget(label1)
    self.setLayout(vbox)


    self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())   