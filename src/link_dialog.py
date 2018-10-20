# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/link_pers_group.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        """Clase que sirve para representar el dialogo que liga personas con grupos y viceversa"""
        self.db = sqlite3.connect("/home/lautimartner/Documents/Modelado/MP3Player/database.sqlite")
        self.cur = self.db.cursor()
        Dialog.setObjectName("Dialog")
        Dialog.resize(306, 115)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.exist_pers = QtWidgets.QComboBox(Dialog)
        self.exist_pers.setObjectName("exist_pers")
        self.gridLayout.addWidget(self.exist_pers, 0, 1, 1, 1)
        self.ex_groups = QtWidgets.QComboBox(Dialog)
        self.ex_groups.setObjectName("ex_groups")
        self.gridLayout.addWidget(self.ex_groups, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.buttonBox.accepted.connect(self.retrieveData)

        self.exist_pers.addItems(self.populatePersonsBox())
        self.ex_groups.addItems(self.populateGroupsBox())

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Link"))
        self.label.setText(_translate("Dialog", "Existing Persons"))
        self.label_2.setText(_translate("Dialog", "Existing Groups"))

    def populatePersonsBox(self):
        """Agrega las personas de la base de datos al combo box personas"""
        persons = self.cur.execute("select stage_name from persons").fetchall()
        self.db.commit()
        person_list = []
        for person in persons:
            person_list.append(person[0])
        return person_list

    def populateGroupsBox(self):
        """Agrega los grupos de la base de datos al combo box personas"""

        groups = self.cur.execute("select name from groups").fetchall()
        self.db.commit()
        group_list = []
        for group in groups:
            group_list.append(group[0])
        return group_list

    def retrieveData(self):
        """Recupera los datos indicados en los combo boxes"""
        group = str(self.ex_groups.currentText())
        person = str(self.exist_pers.currentText())
        return (person, group)
