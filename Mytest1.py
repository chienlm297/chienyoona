import sys
from os import path

import cv2
import numpy as np

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QImage



# class RecordVideo(QtCore.QObject):
#   image_data = QtCore.pyqtSignal(np.ndarray)

#   def __init__(self, camera_port=0):
#     super().__init__()
#     self.camera = cv2.VideoCapture(camera_port)

#   def read_data(self):
#     read, data = self.camera.read()
#     if read:
#       self.image_data.emit(data)


class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_port)

        self.timer = QtCore.QBasicTimer()

    def start_recording(self):
        self.timer.start(0, self)

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        read, data = self.camera.read()
        if read:
            self.image_data.emit(data)

class showFrame(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.frame = QtGui.QImage()
  
  def image_data_slot(self, image_data):
    self.frame = self.get_qimage(image_data)
    if self.frame.size() != self.size():
      self.setFixedSize(self.frame.size())
    
    self.update()

  def get_qimage(self, image: np.ndarray):
    height, width, colors = image.shape
    bytesPerLine = 3* width

    image = QImage(image.data, width, height, bytesPerLine, QImage.Format_BGR888)
    image = image.rgbSwapped()
    return image

class MainWindow(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.show_frame_widget = showFrame()
    self.record_video = RecordVideo()

    image_data_slot = self.show_frame_widget.image_data_slot
    self.record_video.image_data.connect(image_data_slot)

    layout = QtWidgets.QVBoxLayout()

    layout.addWidget(self.show_frame_widget)
    self.start_button = QtWidgets.QPushButton('Start')
    layout.addWidget(self.start_button)

    self.start_button.clicked.connect(self.record_video.start_recording)
    self.setLayout(layout)

def main():
  App = QtWidgets.QApplication(sys.argv)

  main_window = QtWidgets.QMainWindow()
  main_widget = MainWindow()
  main_window.setCentralWidget(main_widget)
  main_window.show()
  sys.exit(App.exec_())

if __name__ == "__main__":
    main()