# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MP3 Library")
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
        self.search_box = QtWidgets.QTextEdit(self.centralwidget)
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
        self.rolas_table.setMinimumSize(QtCore.QSize(21, 440))
        self.rolas_table.setRowCount(1)
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
        self.verticalLayout.addWidget(self.rolas_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_mus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_mus_btn.setObjectName("play_mus_btn")
        self.horizontalLayout.addWidget(self.play_mus_btn)
        self.start_min_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_min_btn.setObjectName("start_min_btn")
        self.horizontalLayout.addWidget(self.start_min_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_per_btn.setText(_translate("MainWindow", "Create Person"))
        self.create_grp_btn.setText(_translate("MainWindow", "Create Group"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        item = self.rolas_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Song ID"))
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
        self.play_mus_btn.setText(_translate("MainWindow", "Play"))
        self.start_min_btn.setText(_translate("MainWindow", "Start Mining"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

