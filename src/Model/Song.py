import sqlite3
from mutagen.id3 import *
from mutagen.id3._util import *

class Song:
    """
    Clase que representa una cancion junto a todos sus atributos.
    Esta cancion sera una entrada en la tabla principal de la base de datos.
    """
    def __init__(self, id3obj):
        self.id3obj = id3obj
        self.setSongTitle(id3obj)
        self.setInterpreter(id3obj)
        self.setAlbum(id3obj)
        self.setRecTime(id3obj)
        self.setGenre(id3obj)
        self.setTrackNo(id3obj)

    def setSongTitle(self, id3obj):
        try:
            self.songtitle = id3obj['TIT2'].text[0]
        except:
            self.songtitle = 'Unknown'

    def setInterpreter(self, id3obj):
        try:
            self.interpreter = id3obj['TPE1'].text[0]
        except:
            self.interpreter = 'Unknown'

    def setAlbum(self, id3obj):
        try:
            self.album=id3obj['TALB'].text[0]
        except:
            self.album = 'Unkwnown'
    def setRecTime(self, id3obj):
        try:
            self.rectime = id3obj['TDRC'].text[0]
        except:
            self.rectime = '2018'

    def setGenre(self, id3obj):
        try:
            self.genre = id3obj['TCON'].text[0]
        except:
            self.genre = 'Unknown'

    def setTrackNo(self, id3obj):
        try:
            self.trackNo = id3obj['TRCK'].text[0]
        except:
            self.trackNo = '0'

if __name__ == '__main__':
    print('Todo bien')