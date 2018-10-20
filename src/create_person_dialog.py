# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_person_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_create_pers(object):
    """Clase que representa el dialogo para crear personas en gui"""
    def setupUi(self, create_pers):
        create_pers.setObjectName("create_pers")
        create_pers.resize(300, 207)
        self.gridLayout_2 = QtWidgets.QGridLayout(create_pers)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(create_pers)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_4 = QtWidgets.QLineEdit(create_pers)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(175, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(create_pers)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(create_pers)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(175, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(create_pers)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(create_pers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(175, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(create_pers)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(create_pers)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(175, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.add_person = QtWidgets.QDialogButtonBox(create_pers)
        self.add_person.setOrientation(QtCore.Qt.Horizontal)
        self.add_person.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.add_person.setObjectName("add_person")
        self.gridLayout.addWidget(self.add_person, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(create_pers)
        self.add_person.accepted.connect(create_pers.accept)
        self.add_person.rejected.connect(create_pers.reject)
        QtCore.QMetaObject.connectSlotsByName(create_pers)
        self.add_person.accepted.connect(self.retrieveData)

    def retranslateUi(self, create_pers):
        _translate = QtCore.QCoreApplication.translate
        create_pers.setWindowTitle(_translate("create_pers", "Create Person"))
        self.label.setText(_translate("create_pers", "Stage Name"))
        self.label_2.setText(_translate("create_pers", "Real Name"))
        self.label_3.setText(_translate("create_pers", "Birth Date"))
        self.label_4.setText(_translate("create_pers", "Death Date"))

    def retrieveData(self):
        """Recupera los datos de entrada que puso el usuario"""
        stagename = self.lineEdit_4.text()
        realname = self.lineEdit_3.text()
        birthdate = self.lineEdit.text()
        deathdate = self.lineEdit_2.text()
        return (stagename, realname, birthdate, deathdate)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_pers = QtWidgets.QDialog()
    ui = Ui_create_pers()
    ui.setupUi(create_pers)
    create_pers.show()
    sys.exit(app.exec_())

