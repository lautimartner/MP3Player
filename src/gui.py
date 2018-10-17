# -*- coding: utf-8 -*-
#! /usr/bin/env python
#! /usr/bin/python3.6
# Form implementation generated from reading ui file 'untitled.ui'
# Created by: PyQt5 UI code generator 5.10.1

import vlc, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from DB import Database
from Miner import Miner
from create_person_dialog import Ui_create_pers
from create_group_dialog import Ui_create_group_dialog
global miner, db
miner = Miner(None)
db = Database()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.playing = False
        self.player = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_per_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_per_btn.setObjectName("create_per_btn")
        self.horizontalLayout_2.addWidget(self.create_per_btn)
        self.create_grp_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_grp_btn.setObjectName("create_grp_btn")
        self.horizontalLayout_2.addWidget(self.create_grp_btn)
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout_2.addWidget(self.update_btn)
        self.search_box = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy)
        self.search_box.setObjectName("search_box")
        self.horizontalLayout_2.addWidget(self.search_box)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_2.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.rolas_table = QtWidgets.QTableWidget(self.centralwidget)
        self.rolas_table.verticalHeader().setVisible(False)
        self.rolas_table.setMinimumSize(QtCore.QSize(21, 10))
        self.rolas_table.setRowCount(0)
        self.rolas_table.setColumnCount(6)
        self.rolas_table.setObjectName("rolas_table")
        item = QtWidgets.QTableWidgetItem()
        self.rolas_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rolas_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rolas_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.rolas_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.rolas_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.rolas_table.setHorizontalHeaderItem(5, item)
        header = self.rolas_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.verticalLayout.addWidget(self.rolas_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_mus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_mus_btn.setObjectName("play_mus_btn")
        self.horizontalLayout.addWidget(self.play_mus_btn)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout.addWidget(self.stop_btn)
        self.start_min_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_min_btn.setObjectName("start_min_btn")
        self.horizontalLayout.addWidget(self.start_min_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Estos son mis escuchas/observadores
        self.start_min_btn.clicked.connect(self.showSongs)
        self.search_box.returnPressed.connect(self.search_btn.click)
        self.search_btn.clicked.connect(self.search)
        self.rolas_table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.play_mus_btn.clicked.connect(self.play)
        self.stop_btn.clicked.connect(self.stop)
        self.create_grp_btn.clicked.connect(self.createGroup)
        self.create_per_btn.clicked.connect(self.createPerson)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MP3 Player"))
        self.create_per_btn.setText(_translate("MainWindow", "Create Person"))
        self.create_grp_btn.setText(_translate("MainWindow", "Create Group"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        item = self.rolas_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.rolas_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Album"))
        item = self.rolas_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Artist"))
        item = self.rolas_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Genre"))
        item = self.rolas_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Year"))
        item = self.rolas_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        self.play_mus_btn.setText(_translate("MainWindow", "Play/Pause"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.start_min_btn.setText(_translate("MainWindow", "Show Songs"))


    def updateTable(self, guitab):
        self.rolas_table.setRowCount(0)
        for row_number, row_data in enumerate(guitab):
            self.rolas_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.rolas_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def play(self):
        song_ind = self.rolas_table.selectionModel().selectedRows(0)
        row = song_ind[0].row()+1
        song = self.rolas_table.item(row-1, 0).text()
        filepath = db.cursor.execute("select path from rolas where id_rola = " + str(song)).fetchall()
        if not self.playing:
            self.player = vlc.MediaPlayer(filepath[0][0])
            self.player.play()
            self.playing = True
        elif self.playing:
            self.player.pause()

    def stop(self):
        if self.playing:
            self.player.stop()
            self.playing = False

    def search(self):
        sQuery = self.search_box.text()
        if sQuery is '':
            self.updateTable(db.executeGUITable())
        else:
            self.search_box.clear()
            guitab = db.queryManager(str(sQuery))
            self.updateTable(guitab)

    def showSongs(self):
        try:
            self.updateTable(db.executeGUITable())
        except sqlite3.OperationalError:
            db.setUpDB(miner)


    def createGroup(self):
        create_group_dialog = QtWidgets.QDialog()
        ui = Ui_create_group_dialog()
        ui.populateComboBox()
        ui.setupUi(create_group_dialog)
        create_group_dialog.exec()
        create_group_dialog.show()
        group = ui.retrieveData()
        db.populateGroupsTable(group[0], group[1], group[2])

    def createPerson(self):
        create_pers = QtWidgets.QDialog()
        ui = Ui_create_pers()
        ui.setupUi(create_pers)
        create_pers.exec_()
        create_pers.show()
        person = ui.retrieveData()
        db.populatePersonsTable(person[0], person[1], person[2], person[3])

if __name__ == "__main__":
    #try:
    import sys, os
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    #except Exception as e:
     #   print(e.__doc__)

