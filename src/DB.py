import sqlite3
import os, sys
class Database:

    def __init__(self):
        self.songList = []
        self.albumDic = {}
        self.interDic = {}
        self.path = '/home/lautimartner/Documents/Modelado/MP3Player/database.sqlite'
        self.dbc = sqlite3.connect(self.path)
        self.cursor = self.dbc.cursor()
        self.guiTable = "SELECT rolas.id_rola, rolas.title, albums.name, performers.name, " \
                        "rolas.genre, rolas.year FROM ((rolas INNER JOIN albums ON " \
                        "rolas.id_album = albums.id_album) INNER JOIN performers ON rolas.id_performer = performers.id_performer)"

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
            interInfo = (inter.id_per, 2, inter.name)
            self.cursor.execute("insert into performers values(?,?,?)", interInfo)
        self.dbc.commit()

    def populatePersonsTable(self, stage_nm, real_nm, birth_dt, death_dt):
        self.cursor.execute("INSERT INTO persons VALUES(?,?,?,?,?)", (None, stage_nm,real_nm, birth_dt, death_dt))
        self.dbc.commit()

    def populateGroupsTable(self, name, start_date, end_date):
        self.cursor.execute("INSERT INTO groups VALUES (?,?,?,?)", (None, name, start_date, end_date))
        self.dbc.commit()

    def queryManager(self, query):
        if type(query) is not str:
            raise ValueError
        else:
            cols = self.searchColumns(self.divideQueries(query))
            result = self.cursor.execute(self.guiTable + " WHERE " + cols)
            self.dbc.commit()
        return result

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
            try:
                searchi = query.index(":")
                searchW = query[searchi + 2:]
            except:
                pass
            if 'a:' in query:
                columns += ' AND albums.name LIKE ' + "'%" +searchW+"%'"
            elif 's:' in query:
                columns += ' AND rolas.title LIKE ' + "'%" + searchW + "%'"
            elif 'p:' in query:
                columns += ' AND performers.name LIKE '+ "'%" +searchW+"%'"
            elif 'y:' in query:
                columns += 'AND rolas.year LIKE ' + "'%" +searchW+"%'"
            elif 'g:' in query:
                columns += ' AND rolas.genre LIKE ' + "'%" +searchW+"%'"
            else:
                columns += " OR rolas.genre LIKE " + "'%" +query+"%'"+ " OR albums.name LIKE " + \
                "'%" +query+"%'" + " OR rolas.title LIKE " + "'%" + query + "%'" + ' OR performers.name LIKE '+ "'%" \
                +query+"%'" +" OR rolas.year LIKE " + "'%" +query+"%'" + " OR rolas.genre LIKE " + "'%" +query+"%'"
                break
        return columns[4:]

    def executeGUITable(self):
        guitab = self.cursor.execute(self.guiTable)
        self.dbc.commit()
        return guitab

    def setUpDB(self, miner):
        miner.startMining(self)
        self.createDB()
        self.populatePerformersTable()
        self.populateAlbumsTable()
        self.populateSongsTable()
