import sqlite3
from Miner import Miner
from Song import Song
class Database:

    def __init__(self):
        self.miner = Miner()
        self.miner.startMining()
        self.created = False
        self.types = None
        self.prfrms = None
        self.prsns = None
        self.grps = None
        self.albms = None
        self.song = None
        self.ingrp = None
        self.dbc = sqlite3.connect('/home/lautimartner/Documents/Modelado/MP3Player/database.sqlite')
        self.cursor = self.dbc.cursor()

    def createDB(self):
        if not self.created:
            self.cursor.executescript("""
                CREATE TABLE types (
                id_type INTEGER PRIMARY KEY ,
                description TEXT
                );
                
                INSERT INTO types VALUES (0 , 'Person');
                INSERT INTO types VALUES (1 , 'Group');
                INSERT INTO types VALUES (2 , 'Unknown');
                
                CREATE TABLE performers (
                id_performer INTEGER PRIMARY KEY ,
                id_type INTEGER ,
                name TEXT ,
                FOREIGN KEY ( id_type ) REFERENCES types ( id_type )
                );
                CREATE TABLE persons (
                id_person INTEGER PRIMARY KEY ,
                stage_name TEXT ,
                real_name TEXT ,
                birth_date TEXT ,
                death_date TEXT
                );
                CREATE TABLE groups (
                id_group INTEGER PRIMARY KEY ,
                name TEXT ,
                start_date TEXT ,
                end_date TEXT
                );
                CREATE TABLE albums (
                id_album INTEGER PRIMARY KEY ,
                path TEXT ,
                name TEXT ,
                year INTEGER
                );
                CREATE TABLE rolas (
                id_rola INTEGER PRIMARY KEY ,
                id_performer INTEGER ,
                id_album INTEGER ,
                path TEXT ,
                title TEXT ,           
                track INTEGER ,
                year INTEGER ,
                genre TEXT ,
                FOREIGN KEY ( id_performer )
                REFERENCES performers ( id_performer ) ,
                FOREIGN KEY ( id_album )
                REFERENCES albums ( id_album )
                );
                CREATE TABLE in_group (
                id_person INTEGER ,
                id_group INTEGER ,
                PRIMARY KEY ( id_person , id_group ) ,
                FOREIGN KEY ( id_person ) REFERENCES persons ( id_person ) ,
                FOREIGN KEY ( id_group ) REFERENCES groups ( id_group )
                );
            """)
            self.dbc.commit()

            self.created = True
        else:
            pass

    def populateSongsTable(self):
        i = 0
        for songs in self.miner.minedSongs:
            self.cursor.execute("insert into rolas values(?,?,?,?,?,?,?,?)", (i, 0 , 0, songs.filepath, songs.songtitle, songs.trackNo, songs.rectime, songs.genre))
            i+=1
        self.dbc.commit()

    def populateAlbumsTable(self):
        i=0
        pass
        """for album in miner.minedAlbums:
            self.cursor.execute("insert into ")
        """
    def populatePerformersTable(self):
        pass

    def populatePersonsTable(self):
        pass

if __name__ == '__main__':
    db=Database()
    db.createDB()
    db.populateSongsTable()
    db.dbc.close()
    print ('Too bien')