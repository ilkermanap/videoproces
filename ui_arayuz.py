# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created: Sat Jan  5 13:51:44 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlgArayuz(object):
    def setupUi(self, dlgArayuz):
        dlgArayuz.setObjectName("dlgArayuz")
        dlgArayuz.resize(1206, 785)
        self.verticalLayout = QtGui.QVBoxLayout(dlgArayuz)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDosyaAdi = QtGui.QLabel(dlgArayuz)
        self.lblDosyaAdi.setObjectName("lblDosyaAdi")
        self.horizontalLayout.addWidget(self.lblDosyaAdi)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(dlgArayuz)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editFrameNo = QtGui.QLineEdit(dlgArayuz)
        self.editFrameNo.setObjectName("editFrameNo")
        self.horizontalLayout.addWidget(self.editFrameNo)
        self.btnAnaliz = QtGui.QPushButton(dlgArayuz)
        self.btnAnaliz.setObjectName("btnAnaliz")
        self.horizontalLayout.addWidget(self.btnAnaliz)
        self.btnDosyaSec = QtGui.QPushButton(dlgArayuz)
        self.btnDosyaSec.setObjectName("btnDosyaSec")
        self.horizontalLayout.addWidget(self.btnDosyaSec)
        self.btnYuzDosyasi = QtGui.QPushButton(dlgArayuz)
        self.btnYuzDosyasi.setObjectName("btnYuzDosyasi")
        self.horizontalLayout.addWidget(self.btnYuzDosyasi)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblResim = QtGui.QLabel(dlgArayuz)
        self.lblResim.setMinimumSize(QtCore.QSize(300, 600))
        self.lblResim.setObjectName("lblResim")
        self.horizontalLayout_2.addWidget(self.lblResim)
        self.lblSkin = QtGui.QLabel(dlgArayuz)
        self.lblSkin.setMinimumSize(QtCore.QSize(300, 600))
        self.lblSkin.setObjectName("lblSkin")
        self.horizontalLayout_2.addWidget(self.lblSkin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lblHistogram = QtGui.QLabel(dlgArayuz)
        self.lblHistogram.setMinimumSize(QtCore.QSize(0, 100))
        self.lblHistogram.setObjectName("lblHistogram")
        self.verticalLayout.addWidget(self.lblHistogram)
        self.sliderFrame = QtGui.QSlider(dlgArayuz)
        self.sliderFrame.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFrame.setObjectName("sliderFrame")
        self.verticalLayout.addWidget(self.sliderFrame)

        self.retranslateUi(dlgArayuz)
        QtCore.QObject.connect(self.editFrameNo, QtCore.SIGNAL("returnPressed()"), dlgArayuz.loadFrame)
        QtCore.QObject.connect(self.btnAnaliz, QtCore.SIGNAL("clicked()"), dlgArayuz.analyze)
        QtCore.QObject.connect(self.btnDosyaSec, QtCore.SIGNAL("clicked()"), dlgArayuz.loadFile)
        QtCore.QObject.connect(self.sliderFrame, QtCore.SIGNAL("sliderReleased()"), dlgArayuz.loadFrame)
        QtCore.QObject.connect(self.btnYuzDosyasi, QtCore.SIGNAL("clicked()"), dlgArayuz.face_file)
        QtCore.QMetaObject.connectSlotsByName(dlgArayuz)

    def retranslateUi(self, dlgArayuz):
        dlgArayuz.setWindowTitle(QtGui.QApplication.translate("dlgArayuz", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDosyaAdi.setText(QtGui.QApplication.translate("dlgArayuz", "Dosya adi", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlgArayuz", "Frame No:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAnaliz.setText(QtGui.QApplication.translate("dlgArayuz", "Analize basla", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDosyaSec.setText(QtGui.QApplication.translate("dlgArayuz", "Dosya Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.btnYuzDosyasi.setText(QtGui.QApplication.translate("dlgArayuz", "Yuz dosyasi sec", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResim.setText(QtGui.QApplication.translate("dlgArayuz", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSkin.setText(QtGui.QApplication.translate("dlgArayuz", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHistogram.setText(QtGui.QApplication.translate("dlgArayuz", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

