# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog - untitled'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_create_group_dialog(object):
    def setupUi(self, create_group_dialog):
        create_group_dialog.setObjectName("create_group_dialog")
        create_group_dialog.resize(249, 190)
        self.gridLayout_2 = QtWidgets.QGridLayout(create_group_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(create_group_dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.group_name = QtWidgets.QLineEdit(create_group_dialog)
        self.group_name.setMaximumSize(QtCore.QSize(100, 16777215))
        self.group_name.setObjectName("group_name")
        self.horizontalLayout.addWidget(self.group_name)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(create_group_dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.start_date = QtWidgets.QComboBox(create_group_dialog)
        self.start_date.setMaximumSize(QtCore.QSize(100, 16777215))
        self.start_date.setObjectName("start_date")
        self.horizontalLayout_2.addWidget(self.start_date)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(create_group_dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.end_date = QtWidgets.QComboBox(create_group_dialog)
        self.end_date.setMaximumSize(QtCore.QSize(100, 16777215))
        self.end_date.setEditable(False)
        self.end_date.setObjectName("end_date")
        self.horizontalLayout_3.addWidget(self.end_date)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(create_group_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(create_group_dialog)
        self.buttonBox.rejected.connect(create_group_dialog.reject)
        self.buttonBox.accepted.connect(create_group_dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(create_group_dialog)

    def retranslateUi(self, create_group_dialog):
        _translate = QtCore.QCoreApplication.translate
        create_group_dialog.setWindowTitle(_translate("create_group_dialog", "Create Group"))
        self.label.setText(_translate("create_group_dialog", "Name"))
        self.label_2.setText(_translate("create_group_dialog", "Start Date"))
        self.label_3.setText(_translate("create_group_dialog", "End Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_group_dialog = QtWidgets.QDialog()
    ui = Ui_create_group_dialog()
    ui.setupUi(create_group_dialog)
    create_group_dialog.show()
    sys.exit(app.exec_())

