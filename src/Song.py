import sqlite3
from mutagen.id3 import *
from mutagen.id3._util import *

class Song:
    """
    Clase que representa una cancion junto a todos sus atributos.
    Esta cancion sera una entrada en la tabla principal de la base de datos.
    """
    def __init__(self, id3obj, filepath):
        self.id3obj = id3obj
        self.filepath = filepath
        try:
            self.songtitle = id3obj['TIT2'].text[0]
        except:
            self.songtitle = 'Unknown'
        try:
            self.interpreter = id3obj['TPE1'].text[0]
        except:
            self.interpreter = 'Unknown'
        try:
            self.album=id3obj['TALB'].text[0]
        except:
            self.album = 'Unknown'
        try:
            self.rectime = int(id3obj['TDRC'].text[0])
        except:
            self.rectime = 2018
        try:
            self.genre = id3obj['TCON'].text[0]
        except:
            self.genre = 'Unknown'
        try:
            self.trackNo = int(id3obj['TRCK'].text[0])
        except:
            self.trackNo = 0

