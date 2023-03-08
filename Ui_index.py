# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1107, 712)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(810, 10, 16, 711))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(870, 40, 151, 61))
        self.pushButton_3.setIconSize(QSize(20, 20))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(870, 400, 151, 61))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(870, 220, 151, 61))
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(870, 590, 151, 61))
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 811, 711))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 821, 711))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 100, 751, 171))
        font = QFont()
        font.setPointSize(60)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"\n"
"color: rgb(7, 243, 255, 240);\n"
"background-color: rgb(255, 255, 255, 50);\n"
"")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 410, 251, 91))
        font1 = QFont()
        font1.setPointSize(25)
        self.label_4.setFont(font1)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(7, 243, 255, 240);\n"
"background-color: rgb(255, 255, 255, 50);\n"
"")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(530, 410, 241, 91))
        font2 = QFont()
        font2.setPointSize(22)
        self.label_5.setFont(font2)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"color: rgb(7, 243, 255, 240);\n"
"background-color: rgb(255, 255, 255, 50);")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 640, 480))
        font3 = QFont()
        font3.setPointSize(6)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 580, 511, 81))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(7, 243, 255, 240);\n"
"background-color: rgb(255, 255, 255, 50);")
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-9, -6, 831, 721))
        self.stackedWidget.addWidget(self.page)
        self.label_7.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tableWidget = QTableWidget(self.page_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 791, 711))
        self.verticalScrollBar = QScrollBar(self.page_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(789, 0, 31, 701))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4eba\u8138\u5f55\u5165", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8003\u52e4\u4fe1\u606f", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4eba\u8138\u6253\u5361", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u4e3b\u9875", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:60pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6253\u5361\u6210\u529f", None))
        self.label_7.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u5de5\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u6253\u5361\u65f6\u95f4", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u8fdf\u5230", None));
    # retranslateUi

