# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Documents/GitHub/Weather_App/weather_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 750))
        MainWindow.setStyleSheet("background-color: rgb(162, 109, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_combo_city = QtWidgets.QComboBox(self.centralwidget)
        self.main_combo_city.setGeometry(QtCore.QRect(700, 40, 201, 22))
        self.main_combo_city.setObjectName("main_combo_city")
        self.main_combo_city.addItem("")
        self.main_combo_city.addItem("")
        self.main_combo_city.addItem("")
        self.main_combo_city.addItem("")
        self.main_combo_city.addItem("")
        self.main_combo_country = QtWidgets.QComboBox(self.centralwidget)
        self.main_combo_country.setGeometry(QtCore.QRect(170, 110, 201, 22))
        self.main_combo_country.setObjectName("main_combo_country")
        self.main_combo_country.addItem("")
        self.main_combo_country.addItem("")
        self.main_combo_country.addItem("")
        self.main_combo_country.addItem("")
        self.main_btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn_search.setGeometry(QtCore.QRect(810, 90, 111, 26))
        self.main_btn_search.setObjectName("main_btn_search")
        self.main_lbl_headingcountrytop = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_headingcountrytop.setGeometry(QtCore.QRect(60, 110, 111, 21))
        self.main_lbl_headingcountrytop.setObjectName("main_lbl_headingcountrytop")
        self.main_lbl_mainheading = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_mainheading.setGeometry(QtCore.QRect(170, 20, 311, 51))
        self.main_lbl_mainheading.setObjectName("main_lbl_mainheading")
        self.main_lbl_headingcity = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_headingcity.setGeometry(QtCore.QRect(510, 90, 111, 21))
        self.main_lbl_headingcity.setObjectName("main_lbl_headingcity")
        self.main_lbl_showcityname = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_showcityname.setGeometry(QtCore.QRect(610, 220, 201, 71))
        self.main_lbl_showcityname.setFrameShape(QtWidgets.QFrame.Box)
        self.main_lbl_showcityname.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_lbl_showcityname.setObjectName("main_lbl_showcityname")
        self.main_lbl_showweathericon = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_showweathericon.setGeometry(QtCore.QRect(520, 320, 171, 121))
        self.main_lbl_showweathericon.setFrameShape(QtWidgets.QFrame.Box)
        self.main_lbl_showweathericon.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_lbl_showweathericon.setObjectName("main_lbl_showweathericon")
        self.main_lbl_showtemperature = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl_showtemperature.setGeometry(QtCore.QRect(730, 320, 181, 121))
        self.main_lbl_showtemperature.setFrameShape(QtWidgets.QFrame.Box)
        self.main_lbl_showtemperature.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_lbl_showtemperature.setObjectName("main_lbl_showtemperature")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(550, 480, 341, 84))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.main_lbl_headingpopulation = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_headingpopulation.setObjectName("main_lbl_headingpopulation")
        self.gridLayout.addWidget(self.main_lbl_headingpopulation, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.main_lbl_headingstate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_headingstate.setObjectName("main_lbl_headingstate")
        self.gridLayout.addWidget(self.main_lbl_headingstate, 2, 0, 1, 1)
        self.main_lbl_showpopulation = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_showpopulation.setObjectName("main_lbl_showpopulation")
        self.gridLayout.addWidget(self.main_lbl_showpopulation, 1, 2, 1, 1)
        self.main_lbl_headingcountry = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_headingcountry.setObjectName("main_lbl_headingcountry")
        self.gridLayout.addWidget(self.main_lbl_headingcountry, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.main_lbl_showcountry = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_showcountry.setObjectName("main_lbl_showcountry")
        self.gridLayout.addWidget(self.main_lbl_showcountry, 0, 2, 1, 1)
        self.main_lbl_showstate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_lbl_showstate.setObjectName("main_lbl_showstate")
        self.gridLayout.addWidget(self.main_lbl_showstate, 2, 2, 1, 1)
        self.main_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.main_btn_exit.setGeometry(QtCore.QRect(680, 660, 81, 26))
        self.main_btn_exit.setObjectName("main_btn_exit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 170, 321, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 90, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App"))
        self.main_combo_city.setItemText(0, _translate("MainWindow", "- City -"))
        self.main_combo_city.setItemText(1, _translate("MainWindow", "Berlin"))
        self.main_combo_city.setItemText(2, _translate("MainWindow", "Brussels"))
        self.main_combo_city.setItemText(3, _translate("MainWindow", "Ankara"))
        self.main_combo_city.setItemText(4, _translate("MainWindow", "Istanbul"))
        self.main_combo_country.setItemText(0, _translate("MainWindow", "- Country -"))
        self.main_combo_country.setItemText(1, _translate("MainWindow", "Belgium"))
        self.main_combo_country.setItemText(2, _translate("MainWindow", "Germany"))
        self.main_combo_country.setItemText(3, _translate("MainWindow", "United States of America"))
        self.main_btn_search.setText(_translate("MainWindow", "Search City"))
        self.main_lbl_headingcountrytop.setText(_translate("MainWindow", "Country :"))
        self.main_lbl_mainheading.setText(_translate("MainWindow", "Welcome!"))
        self.main_lbl_headingcity.setText(_translate("MainWindow", "City:"))
        self.main_lbl_showcityname.setText(_translate("MainWindow", "City name"))
        self.main_lbl_showweathericon.setText(_translate("MainWindow", "Weather icon"))
        self.main_lbl_showtemperature.setText(_translate("MainWindow", "Temperature"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.main_lbl_headingpopulation.setText(_translate("MainWindow", "Population"))
        self.label.setText(_translate("MainWindow", ":"))
        self.main_lbl_headingstate.setText(_translate("MainWindow", "State / Region"))
        self.main_lbl_showpopulation.setText(_translate("MainWindow", "900.000"))
        self.main_lbl_headingcountry.setText(_translate("MainWindow", "Country"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.main_lbl_showcountry.setText(_translate("MainWindow", "USA"))
        self.main_lbl_showstate.setText(_translate("MainWindow", "Arkansas"))
        self.main_btn_exit.setText(_translate("MainWindow", "Exit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Region/State"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
