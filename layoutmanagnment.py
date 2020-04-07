from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class window(QDialog):
  def __init__(self):
    super().__init__()

    self.title = 'Layout managenment'
    self.left = 500
    self.top = 200
    self.width = 500
    self.height = 250

    self.InitWindow()


    self.show()

  def InitWindow(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)
      self.createLayout()
      vbox = QVBoxLayout()
      vbox.addWidget(self.groupBox)
      self.setLayout(vbox)


  def createLayout(self):
    self.groupBox = QGroupBox("what is your Favorite Sport")
    hboxlayout = QHBoxLayout()

    button = QPushButton("Football", self)
    button.setMinimumHeight(40)
    hboxlayout.addWidget(button)

    button1 = QPushButton("Half life", self)
    button1.setMinimumHeight(40)
    hboxlayout.addWidget(button1)

    button2 = QPushButton("Fifa", self)
    button2.setMinimumHeight(40)
    hboxlayout.addWidget(button2)

    self.groupBox.setLayout(hboxlayout)




if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = window()
    sys.exit(App.exec())


# Bài này hướng dẫn tạo một group box gồm các button và tạo ra các layout để làm việc. :3