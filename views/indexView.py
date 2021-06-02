# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indexView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class indexView(object):
    def setupUi(self, indexView):
        if not indexView.objectName():
            indexView.setObjectName(u"indexView")
        indexView.resize(903, 513)
        self.pushButtonFile = QPushButton(indexView)
        self.pushButtonFile.setObjectName(u"pushButtonFile")
        self.pushButtonFile.setGeometry(QRect(260, 30, 381, 41))
        self.widgetAudio = QWidget(indexView)
        self.widgetAudio.setObjectName(u"widgetAudio")
        self.widgetAudio.setGeometry(QRect(10, 141, 421, 361))
        self.widgetAudioProcesado = QWidget(indexView)
        self.widgetAudioProcesado.setObjectName(u"widgetAudioProcesado")
        self.widgetAudioProcesado.setGeometry(QRect(439, 140, 451, 361))
        self.label = QLabel(indexView)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 100, 181, 21))
        self.label_2 = QLabel(indexView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(580, 100, 181, 21))

        self.retranslateUi(indexView)

        QMetaObject.connectSlotsByName(indexView)
    # setupUi

    def retranslateUi(self, indexView):
        indexView.setWindowTitle(QCoreApplication.translate("indexView", u"Form", None))
        self.pushButtonFile.setText(QCoreApplication.translate("indexView", u"File", None))
        self.label.setText(QCoreApplication.translate("indexView", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Audio Normal</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("indexView", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Audio Procesado</span></p></body></html>", None))
    # retranslateUi

