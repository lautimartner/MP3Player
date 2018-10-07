import sqlite3
from Song import Song
from Album import Album
from Artist import Interpreter
class Database:

    def __init__(self):
        self.songList = []
        self.albumDic = {}
        self.interDic = {}
        self.path = '/home/lautimartner/Documents/Modelado/MP3Player/database.db'
        self.dbc = sqlite3.connect(self.path)
        self.cursor = self.dbc.cursor()

    def createDB(self):
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

    def populateSongsTable(self):
        for songs in self.songList:
            try:
                songInfo = (None,self.interDic[songs.interpreter].id_per, self.albumDic[songs.album].id_album, songs.filepath, songs.songtitle, songs.trackNo, songs.rectime, songs.genre)
                self.cursor.execute("insert into rolas values(?,?,?,?,?,?,?,?)", songInfo)

            except Exception as e:
                #print(e)
                pass
        self.dbc.commit()

    def populateAlbumsTable(self):
        try:
            for album in self.albumDic:
                alb = self.albumDic[album]
                albumInfo = (alb.id_album, alb.path, alb.name, alb.year)
                self.cursor.execute("insert into albums values(?,?,?,?)", albumInfo)
            self.dbc.commit()
        except Exception as e:
            print (e)

    def populatePerformersTable(self):
        for interpreter in self.interDic:
            inter = self.interDic[interpreter]
            interInfo = (inter.id_per, 0, inter.name)
            self.cursor.execute("insert into performers values(?,?,?)", interInfo)
        self.dbc.commit()

    def populatePersonsTable(self):
        pass

if __name__ == '__main__':


    print ('Todo bien')