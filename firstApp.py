from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 841, 511))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("/home/yoona/Pictures/81041837_2692472010836155_3651594724206182400_o.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(0, 510, 411, 41))
        self.cat.setObjectName("cat")
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(410, 510, 391, 41))
        self.dog.setObjectName("dog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dog.clicked.connect(self.show_capture)
        self.cat.clicked.connect(self.show_cat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "CAT"))
        self.dog.setText(_translate("MainWindow", "DOG"))

    def show_capture(self):
      cap = cv2.VideoCapture(0)
      while True:
        _, self.frame = cap.read()
        print("log 49",self.frame)
        if not _:
          sys.exit()
        self.show_dog(self.frame)


    def show_dog(self, image):
        # self.image = cv2.imread("/home/yoona/Pictures/83381484_2692456974170992_2892531474513264640_o.jpg")
        print(image)
        self.image = image
        self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.photo.setPixmap(QtGui.QPixmap.fromImage(self.image))


    def show_cat(self):
        self.photo.setPixmap(QtGui.QPixmap("/home/yoona/Pictures/81041837_2692472010836155_3651594724206182400_o.jpg"))
        cap = cv2.VideoCapture('/home/yoona/Videos/Webcam/realFace.webm')
        while (cap.isOpened()):
          ret, frame = cap.read()
          if not ret:
            break
          frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
          pix = QtGui.QPixmap.fromImage(img)
          self.photo.setPixmap(pix)
          if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cap.release()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())