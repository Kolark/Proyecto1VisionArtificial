#Import libraries
import sys,re
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import Clases
import cv2

chars = Clases.Tools.Characteristics()

#.ui file path
uiFile = "./ui/MainUI.ui"
#Load ui file
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)
#Capture video
captura = cv2.VideoCapture(0)


class UIWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # self.btnCalibrar.clicked.connect(self.viewCam)
        self.timer = QTimer()
        self.btnEmpezar.clicked.connect(self.controlTimer)
        self.timer.timeout.connect(self.viewCam)
    def printxd(self):
        print("calibrado")
    
    def Ejecutar(self):
        print("ah")
    
    def viewCam(self):
        print("Viewing Cam")
    # read image in BGR format
        disponible, fotograma = captura.read()
    # convert image to RGB format
        fotograma = cv2.cvtColor(fotograma, cv2.COLOR_BGR2RGB)
    # get image infos
        height, width, channel = fotograma.shape
        step = channel * width
    # create QImage from image
        qImg = QImage(fotograma.data, width, height, step, QImage.Format_RGB888)
    # show image in img_label
        self.qlabel.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(30)
            # update control_bt text
            self.btnEmpezar.setText("Parar")
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.btnEmpezar.setText("Empezar")

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())