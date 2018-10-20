#! /usr/bin/env python3
#! /usr/bin/python3.6
# Form implementation generated from reading ui file 'untitled.ui'
# Created by: PyQt5 UI code generator 5.10.1

import vlc, sqlite3, _thread, time
from PyQt5 import QtCore, QtGui, QtWidgets
from DB import Database
from Miner import Miner
from create_person_dialog import Ui_create_pers
from create_group_dialog import Ui_create_group_dialog
from link_dialog import Ui_Dialog
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

        self.pb = QtWidgets.QProgressBar(self.centralwidget)
        self.pb.setProperty("value", 0)
        self.pb.setObjectName("pb")
        self.horizontalLayout.addWidget(self.pb)

        self.rolas_table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.start_min_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_min_btn.setObjectName("start_min_btn")
        self.horizontalLayout.addWidget(self.start_min_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Estos son mis escuchas/observadores

        # Muestra las canciones cuando hacen click al boton show Songs
        self.start_min_btn.clicked.connect(self.showSongs)
        # Conecta el presionar el boton de return con un click al boton de buscar
        self.search_box.returnPressed.connect(self.search_btn.click)
        # Conecta el boton search con la funcion que busca en la base de datos
        self.search_btn.clicked.connect(self.search)
        # Conecta el boton de reproduccion con el metodo que reproduce la musica
        self.play_mus_btn.clicked.connect(self.play)
        #Conecta el boton stop con el metodo que para la musica
        self.stop_btn.clicked.connect(self.stop)
        #Conecta el boton de crear grupo con la funcion create group
        self.create_grp_btn.clicked.connect(self.createGroup)
        # Conecta la funcion de create person con su boton correspondiente
        self.create_per_btn.clicked.connect(self.createPerson)
        # Conecta la funcion de ligar personas con grupos y viceversa
        self.update_btn.clicked.connect(self.link)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MP3 Player"))
        self.create_per_btn.setText(_translate("MainWindow", "Create Person"))
        self.create_grp_btn.setText(_translate("MainWindow", "Create Group"))
        self.update_btn.setText(_translate("MainWindow", "Link Persons and Groups"))
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
        """
        Actualiza la tabla de canciones
        :param guitab: objeto que contiene los resultados de una consulta a la base de datos
        :return:
        """
        self.rolas_table.setRowCount(0)
        for row_number, row_data in enumerate(guitab):
            self.rolas_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.rolas_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def play(self):
        """
        Metodo que reproduce una cancion
        """
        try:
            song_ind = self.rolas_table.selectionModel().selectedRows(0)
            row = song_ind[0].row()+1
            song = self.rolas_table.item(row-1, 0).text()
            filepath = db.cursor.execute("select path from rolas where id_rola = " + str(song)).fetchall()
            if not self.playing:
                self.player = vlc.MediaPlayer(filepath[0][0])
                self.player.play()
                self.playing = True
                _thread.start_new_thread(self.progress,())
            elif self.playing:
                self.player.pause()
        except IndexError as i:
            print(i)

    def stop(self):
        """
        Metodo que para la reproduccion de musica
        """
        if self.playing:
            self.player.stop()
            self.playing = False
            self.pb.setValue(0)

    def search(self):
        """
        Metodo para que el usuario pueda buscar en la base de datos
        """
        sQuery = self.search_box.text()
        if sQuery is '':
            self.updateTable(db.executeGUITable())
        else:
            self.search_box.clear()
            guitab = db.queryManager(str(sQuery))
            self.updateTable(guitab)

    def showSongs(self):
        """
        Metodo para mostrar todas las cacnioens de la clase de datos, si aun no existe la base de datos la crea
        """
        try:
            self.updateTable(db.executeGUITable())
        except sqlite3.OperationalError:
            db.setUpDB(miner)
            self.updateTable(db.executeGUITable())


    def createGroup(self):
        """
        Metodo para crear un grupo
        """
        create_group_dialog = QtWidgets.QDialog()
        ui = Ui_create_group_dialog()
        ui.populateComboBox()
        ui.setupUi(create_group_dialog)
        create_group_dialog.exec()
        create_group_dialog.show()
        group = ui.retrieveData()
        db.populateGroupsTable(group[0], group[1], group[2])

    def createPerson(self):
        """
        Metodo que crea una persona
        """
        create_pers = QtWidgets.QDialog()
        ui = Ui_create_pers()
        ui.setupUi(create_pers)
        create_pers.exec_()
        create_pers.show()
        person = ui.retrieveData()
        db.populatePersonsTable(person[0], person[1], person[2], person[3])

    def progress(self):
        """"
        Actualiza la posicion de la barra de progreso de la cancion cada 1.5 segundos
        """
        while self.player.get_position() < 1:
            time.sleep(1.5)
            self.pb.setValue(self.player.get_position()*100)

    def link(self):
        """Liga personas con grupos y viceversa"""
        link = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(link)
        link.exec_()
        link.show()
        info = ui.retrieveData()
        try:
            insert = db.cursor.execute("select persons.id_person, groups.id_group from persons inner join groups where persons.stage_name = ? AND groups.name = ?", info).fetchall()
            db.cursor.execute("insert into in_group values(?,?)", insert[0])
            db.dbc.commit()
        except:
            pass


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