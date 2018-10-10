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
                FOREIGN KEY ( id_performer ) REFERENCES performers ( id_performer ) ,
                FOREIGN KEY ( id_album ) REFERENCES albums ( id_album )
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
                print(e)
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

    def queryManager(self, query):
        cols = self.searchColumns(self.divideQueries(query))
        print("SELECT * FROM guiTable WHERE %s" % cols)
        self.cursor.execute("SELECT * FROM guiTable WHERE (?) ", (cols,))
        self.dbc.commit()

    def divideQueries(self, query):
        tokenList = []
        token = ''
        i = 0
        for char in query:
            if char == '|' or len(query)-1 == i:
                if len(query)-1 == i:
                    token+=char
                tokenList.append(token)
                token = ''
            else:
                token += char
            i+=1
        return tokenList

    def searchColumns(self, queryList):
        columns = ''
        for query in queryList:
            if len(queryList) == 1:
                columns += " OR genre LIKE " + "'%" +query+"%'"+ " OR alb_name LIKE " + \
                "'%" +query+"%'" + " OR song_name LIKE " + "'%" + query + "%'" + ' OR perf_name LIKE '+ "'%" \
                +query+"%'" +" OR year LIKE " + "'%" +query+"%'" + " OR genre LIKE " + "'%" +query+"%'"
                break
            searchi = query.index(":")
            searchW = query[searchi + 2:]
            if 'a:' in query:
                columns += 'AND alb_name LIKE ' + "'%" +searchW+"%'"
            elif 's:' in query:
                columns += 'AND song_name LIKE ' + "'%" + searchW + "%'"
            elif 'p:' in query:
                columns += 'AND perf_name LIKE '+ "'%" +searchW+"%'"
            elif 'y:' in query:
                columns += 'AND year LIKE ' + "'%" +searchW+"%'"
            elif 'g:' in query:
                columns += 'AND genre LIKE ' + "'%" +searchW+"%'"
        return columns[3:]

    def setGUITable(self):
        self.cursor.executescript("""
            CREATE TABLE guiTable(
                id_rola INTEGER,
                song_name TEXT,
                alb_name TEXT,
                perf_name TEXT,
                genre TEXT,
                year INTEGER,
                path TEXT,
                PRIMARY KEY(id_rola),
                FOREIGN KEY(id_rola, song_name, genre, year, path) REFERENCES rolas(id_rola, title, genre, year, path),
                FOREIGN KEY(alb_name) REFERENCES albums(name),
                FOREIGN KEY(perf_name) REFERENCES performers(name)
            );
            
            INSERT INTO guiTable(id_rola, song_name, genre, year, path) SELECT id_rola, title, genre, year, path FROM rolas;
            INSERT INTO guiTable(alb_name) SELECT name FROM albums;
            INSERT INTO guiTable(perf_name) SELECT name FROM performers;                
        """)
        self.dbc.commit()

if __name__ == '__main__':

    print ('Todo bien')