# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Documents/GitHub/Weather_App/weather_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 750))
        background = QPixmap("photos/Screenshot 2023-03-28 at 15.32.16.png") # copy path
        background_label = QLabel(parent=MainWindow)
        background_label.setPixmap(background)
        background_label.setGeometry(0, 0, background.width(), background.height())
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn_search.setGeometry(QtCore.QRect(820, 120, 111, 41))
        self.main_btn_search.setStyleSheet("font: 75 18pt \"Times New Roman\";\n"
"\n"
"  background-color: rgba(255,255,255,0.7);\n"
"")
        self.main_btn_search.setObjectName("main_btn_search")
        self.main_lbl_mainheading = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_mainheading.setGeometry(QtCore.QRect(80, 20, 801, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.main_lbl_mainheading.setFont(font)
        self.main_lbl_mainheading.setStyleSheet("color: rgb(255, 186, 121);")
        self.main_lbl_mainheading.setAlignment(QtCore.Qt.AlignCenter)
        self.main_lbl_mainheading.setObjectName("main_lbl_mainheading")
        self.main_lbl_headingcity = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_headingcity.setGeometry(QtCore.QRect(480, 120, 81, 41))
        self.main_lbl_headingcity.setStyleSheet("font: 75 24pt \"Times New Roman\";")
        self.main_lbl_headingcity.setObjectName("main_lbl_headingcity")
        self.main_lbl_showcityname = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_showcityname.setGeometry(QtCore.QRect(490, 220, 481, 71))
        self.main_lbl_showcityname.setStyleSheet("font: 75 48pt \"Times New Roman\";")
        self.main_lbl_showcityname.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_lbl_showcityname.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_lbl_showcityname.setAlignment(QtCore.Qt.AlignCenter)
        self.main_lbl_showcityname.setObjectName("main_lbl_showcityname")
        self.main_lbl_showweathericon = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_showweathericon.setGeometry(QtCore.QRect(530, 300, 181, 131))
        self.main_lbl_showweathericon.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.main_lbl_showweathericon.setStyleSheet("font: 75 56pt \"Times New Roman\";")
        self.main_lbl_showweathericon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_lbl_showweathericon.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_lbl_showweathericon.setAlignment(QtCore.Qt.AlignCenter)
        self.main_lbl_showweathericon.setObjectName("main_lbl_showweathericon")
        self.main_lbl_showtemperature = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_showtemperature.setGeometry(QtCore.QRect(740, 300, 191, 61))
        self.main_lbl_showtemperature.setStyleSheet("font: 75 36pt \"Times New Roman\";")
        self.main_lbl_showtemperature.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_lbl_showtemperature.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_lbl_showtemperature.setObjectName("main_lbl_showtemperature")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(560, 480, 411, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_2.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.main_lbl_headingpopulation = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_headingpopulation.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.main_lbl_headingpopulation.setObjectName("main_lbl_headingpopulation")
        self.gridLayout.addWidget(self.main_lbl_headingpopulation, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(55, 1000))
        self.label.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.main_lbl_headingstate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_headingstate.setMaximumSize(QtCore.QSize(150, 16777215))
        self.main_lbl_headingstate.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.main_lbl_headingstate.setObjectName("main_lbl_headingstate")
        self.gridLayout.addWidget(self.main_lbl_headingstate, 2, 0, 1, 1)
        self.main_lbl_showpopulation = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_showpopulation.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.main_lbl_showpopulation.setText("")
        self.main_lbl_showpopulation.setObjectName("main_lbl_showpopulation")
        self.gridLayout.addWidget(self.main_lbl_showpopulation, 1, 2, 1, 1)
        self.main_lbl_headingcountry = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_headingcountry.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.main_lbl_headingcountry.setObjectName("main_lbl_headingcountry")
        self.gridLayout.addWidget(self.main_lbl_headingcountry, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(21, 23))
        self.label_3.setMaximumSize(QtCore.QSize(55, 1000))
        self.label_3.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.main_lbl_showcountry = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_showcountry.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.main_lbl_showcountry.setText("")
        self.main_lbl_showcountry.setObjectName("main_lbl_showcountry")
        self.gridLayout.addWidget(self.main_lbl_showcountry, 0, 2, 1, 1)
        self.main_lbl_showstate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_showstate.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.main_lbl_showstate.setText("")
        self.main_lbl_showstate.setObjectName("main_lbl_showstate")
        self.gridLayout.addWidget(self.main_lbl_showstate, 2, 2, 1, 1)
        self.main_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn_exit.setGeometry(QtCore.QRect(720, 640, 71, 61))
        self.main_btn_exit.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.main_btn_exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/melike/Documents/GitHub/Weather_App/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_btn_exit.setIcon(icon)
        self.main_btn_exit.setIconSize(QtCore.QSize(50, 50))
        self.main_btn_exit.setFlat(True)
        self.main_btn_exit.setObjectName("main_btn_exit")
        self.main_tbl_cities = QtWidgets.QTableWidget(self.centralwidget)
        self.main_tbl_cities.setGeometry(QtCore.QRect(40, 170, 411, 511))
        self.main_tbl_cities.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.main_tbl_cities.setAutoFillBackground(False)
        self.main_tbl_cities.setStyleSheet("\n"
"background-color: rgba(255,255,255,0.5);\n"
"\n"
"selection-background-color: rgba(255,255,255,0.2);\n"
"\n"
"")
        self.main_tbl_cities.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.main_tbl_cities.setObjectName("main_tbl_cities")
        self.main_tbl_cities.setColumnCount(3)
        self.main_tbl_cities.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.main_tbl_cities.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.main_tbl_cities.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.main_tbl_cities.setHorizontalHeaderItem(2, item)
        self.main_tbl_cities.horizontalHeader().setVisible(True)
        self.main_tbl_cities.horizontalHeader().setCascadingSectionResizes(False)
        self.main_tbl_cities.horizontalHeader().setDefaultSectionSize(135)
        self.main_tbl_cities.horizontalHeader().setHighlightSections(True)
        self.main_tbl_cities.horizontalHeader().setMinimumSectionSize(27)
        self.main_tbl_cities.verticalHeader().setVisible(False)
        self.main_linedit_city = QtWidgets.QLineEdit(self.centralwidget)
        self.main_linedit_city.setGeometry(QtCore.QRect(570, 120, 231, 41))
        self.main_linedit_city.setStyleSheet("font: 18pt \"Times New Roman\";\n"
"  background-color: rgba(255,255,255,0.5);\n"
"")
        self.main_linedit_city.setObjectName("main_linedit_city")
        self.main_btn_usa = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn_usa.setGeometry(QtCore.QRect(310, 110, 81, 31))
        self.main_btn_usa.setStyleSheet("font: 75 18pt \"Times New Roman\";\n"
"\n"
"  background-color: rgba(255,255,255,0.7);\n"
"")
        self.main_btn_usa.setObjectName("main_btn_usa")
        self.main_btn_belgium = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn_belgium.setGeometry(QtCore.QRect(110, 110, 91, 31))
        self.main_btn_belgium.setStyleSheet("font: 75 18pt \"Times New Roman\";\n"
"\n"
"background-color: rgba(255,255,255,0.7);\n"
"")
        self.main_btn_belgium.setObjectName("main_btn_belgium")
        self.main_btn_germany = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn_germany.setGeometry(QtCore.QRect(210, 110, 91, 31))
        self.main_btn_germany.setStyleSheet("font: 75 18pt \"Times New Roman\";\n"
"\n"
"  background-color: rgba(255,255,255,0.7);\n"
"")
        self.main_btn_germany.setObjectName("main_btn_germany")
        self.main_lbl_showweathersituation = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_showweathersituation.setGeometry(QtCore.QRect(740, 370, 201, 61))
        self.main_lbl_showweathersituation.setStyleSheet("font: 75 28pt \"Times New Roman\";")
        self.main_lbl_showweathersituation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_lbl_showweathersituation.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_lbl_showweathersituation.setObjectName("main_lbl_showweathersituation")
        self.main_btn_info = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn_info.setEnabled(True)
        self.main_btn_info.setGeometry(QtCore.QRect(900, 20, 71, 61))
        self.main_btn_info.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_btn_info.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.main_btn_info.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/melike/Documents/GitHub/Weather_App/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_btn_info.setIcon(icon1)
        self.main_btn_info.setIconSize(QtCore.QSize(50, 50))
        self.main_btn_info.setFlat(True)
        self.main_btn_info.setObjectName("main_btn_info")
        self.main_lbl_searchwarning = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_searchwarning.setGeometry(QtCore.QRect(500, 180, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.main_lbl_searchwarning.setFont(font)
        self.main_lbl_searchwarning.setStyleSheet("color: rgb(227, 151, 67);")
        self.main_lbl_searchwarning.setText("")
        self.main_lbl_searchwarning.setAlignment(QtCore.Qt.AlignCenter)
        self.main_lbl_searchwarning.setObjectName("main_lbl_searchwarning")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App"))
        self.main_btn_search.setText(_translate("MainWindow", "Search City"))
        self.main_lbl_mainheading.setText(_translate("MainWindow", "Welcome to the Weather App"))
        self.main_lbl_headingcity.setText(_translate("MainWindow", "City :"))
        self.main_lbl_showcityname.setText(_translate("MainWindow", "City name"))
        self.main_lbl_showweathericon.setText(_translate("MainWindow", "icon"))
        self.main_lbl_showtemperature.setText(_translate("MainWindow", "Temp"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.main_lbl_headingpopulation.setText(_translate("MainWindow", "Population"))
        self.label.setText(_translate("MainWindow", ":"))
        self.main_lbl_headingstate.setText(_translate("MainWindow", "State / Region"))
        self.main_lbl_headingcountry.setText(_translate("MainWindow", "Country"))
        self.label_3.setText(_translate("MainWindow", ":"))
        item = self.main_tbl_cities.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "City"))
        item = self.main_tbl_cities.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Region/State"))
        item = self.main_tbl_cities.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Population"))
        self.main_btn_usa.setText(_translate("MainWindow", "USA"))
        self.main_btn_belgium.setText(_translate("MainWindow", "Belgium"))
        self.main_btn_germany.setText(_translate("MainWindow", "Germany"))
        self.main_lbl_showweathersituation.setText(_translate("MainWindow", "situation"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
