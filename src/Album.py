
from Song import Song
class Album:
    """Clase que representa un objeto album y sus atributos"""
    def __init__(self, song, id, dirpath):
        self.id_album = id
        self.path = dirpath
        try:
            self.name = song.album
        except:
            self.name = "Unknown"
        self.year = song.rectime