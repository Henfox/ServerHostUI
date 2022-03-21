# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIiEDzGo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 240)
        MainWindow.setMinimumSize(QSize(500, 200))
        MainWindow.setMaximumSize(QSize(1231241, 1231241))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color:rgba(19, 14, 34,0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.ServerList = QTableWidget(self.centralwidget)
        if (self.ServerList.columnCount() < 1):
            self.ServerList.setColumnCount(1)
        brush = QBrush(QColor(19, 14, 13, 255))
        brush.setStyle(Qt.SolidPattern)
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(89, 254, 149));
        __qtablewidgetitem.setForeground(brush);
        self.ServerList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.ServerList.setObjectName(u"ServerList")
        self.ServerList.setEnabled(True)
        self.ServerList.setGeometry(QRect(10, 10, 432, 216))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ServerList.sizePolicy().hasHeightForWidth())
        self.ServerList.setSizePolicy(sizePolicy1)
        self.ServerList.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(10)
        self.ServerList.setFont(font2)
        self.ServerList.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.ServerList.setFocusPolicy(Qt.NoFocus)
        self.ServerList.setContextMenuPolicy(Qt.NoContextMenu)
        self.ServerList.setAutoFillBackground(False)
        self.ServerList.setStyleSheet(u"QTableWidget {\n"
"	border-radius: 5px;\n"
"	background-color:rgba(255, 255, 255, 0);\n"
"	font: 87 10pt \"Arial Black\";\n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	padding: 5px;\n"
"	margin-top:5px;\n"
"		border-radius: 5px;\n"
"	background-color:rgb(39, 34, 54);\n"
"	color:rgb(141, 123, 195);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 137, 64, 255), stop:1 rgba(210, 64, 255, 255));\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"			border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 137, 64, 255), stop:1 rgba(210, 64, 255, 255));\n"
"}")
        self.ServerList.setLineWidth(0)
        self.ServerList.setMidLineWidth(0)
        self.ServerList.setAutoScrollMargin(1)
        self.ServerList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ServerList.setProperty("showDropIndicator", False)
        self.ServerList.setDragDropOverwriteMode(False)
        self.ServerList.setAlternatingRowColors(False)
        self.ServerList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ServerList.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ServerList.setTextElideMode(Qt.ElideMiddle)
        self.ServerList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ServerList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ServerList.setShowGrid(False)
        self.ServerList.setSortingEnabled(False)
        self.ServerList.setWordWrap(False)
        self.ServerList.setCornerButtonEnabled(False)
        self.ServerList.setRowCount(0)
        self.ServerList.setColumnCount(1)
        self.ServerList.horizontalHeader().setVisible(True)
        self.ServerList.horizontalHeader().setCascadingSectionResizes(True)
        self.ServerList.horizontalHeader().setMinimumSectionSize(0)
        self.ServerList.horizontalHeader().setDefaultSectionSize(115)
        self.ServerList.horizontalHeader().setHighlightSections(False)
        self.ServerList.horizontalHeader().setProperty("showSortIndicator", False)
        self.ServerList.horizontalHeader().setStretchLastSection(True)
        self.ServerList.verticalHeader().setVisible(False)
        self.ServerList.verticalHeader().setDefaultSectionSize(30)
        self.ServerList.verticalHeader().setHighlightSections(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(0, 0, 600, 240))
        self.frame.setStyleSheet(u"border-radius: 25px;\n"
"background-color:rgb(19, 14, 34);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.startButton = QPushButton(self.frame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(False)
        self.startButton.setGeometry(QRect(480, 50, 90, 30))
        self.startButton.setStyleSheet(u"QPushButton{background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(121, 194, 27, 255), stop:1 rgba(38, 194, 27, 255));\n"
"border-radius: 5px;\n"
"font: 87 8pt \"Arial Black\";\n"
"}\n"
"QPushButton::hover{\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(133, 214, 30, 255), stop:1 rgba(48, 244, 34, 255));\n"
"border: 1px solid rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(110, 176, 24, 255), stop:1 rgba(38, 196, 27, 255));\n"
"border: 1px solid rgb(0, 0, 0)\n"
"}\n"
"QPushButton::disabled{\n"
"color: rgba(0, 0, 0,150);\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(121, 194, 27, 150), stop:1 rgba(38, 194, 27, 150))\n"
"}")
        self.cancelButton = QPushButton(self.frame)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(480, 160, 90, 30))
        self.cancelButton.setStyleSheet(u"QPushButton{background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(212, 33, 27, 255), stop:1 rgba(212, 27, 107, 255));\n"
"border-radius: 5px;\n"
"font: 87 8pt \"Arial Black\";\n"
"}\n"
"QPushButton::hover{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(244, 43, 36, 255), stop:1 rgba(251, 32, 127, 255));\n"
"border: 1px solid rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(178, 28, 23, 255), stop:1 rgba(167, 21, 84, 255));\n"
"border: 1px solid rgb(0, 0, 0)\n"
"}")
        self.cancelButton.setCheckable(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 220, 101, 16))
        self.label.setStyleSheet(u"color: rgb(39, 34, 54)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.ServerList.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.ServerList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Server", None));
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Created by: Henfox", None))
    # retranslateUi

