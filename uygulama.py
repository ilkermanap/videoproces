from PySide.QtGui import *
from PySide.QtCore import *
from ui_arayuz import Ui_dlgArayuz
import sys
import random, time
from video import *
import cv2

class MainWindow(QDialog, Ui_dlgArayuz):
    def __init__(self, app = None):
        super(MainWindow, self).__init__()
        self.app = app
        self.video = None
        self.setupUi(self)
        self.show()
        
    def loadFrame(self, frameno=None):
        if frameno is None:
            state, picture = self.video.export_image()
            if state:
                newp = cv2.cvtColor(picture.image, cv2.COLOR_BGR2RGB)
                qimg = QImage(newp,newp.shape[1], newp.shape[0], QImage.Format_RGB888)
                pixmap01 = QPixmap.fromImage(qimg)
                self.lblResim.setPixmap(pixmap01)

                count, skin = picture.check_skin()
                skin = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)
            
                qskin = QImage(skin,skin.shape[1],
                                    skin.shape[0], QImage.Format_RGB888)
                pixmap02 = QPixmap.fromImage(qskin)
                self.lblSkin.setPixmap(pixmap02)
                

    def analyze(self):
        
        numframes = int(self.video.info.frame_count)
        for i in range(numframes):
            
            pass
    def loadFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '.')
        self.video = VideoFile(fname)
        self.lblDosyaAdi.setText(fname)
        self.video.locate_frame(30)
        self.loadFrame()



        pass
    
        

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)

    




