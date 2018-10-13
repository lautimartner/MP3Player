import os
from src.Model.Song import Song
from mutagen.id3 import *
from mutagen.id3._util import *
from src.Model.Album import Album
from src.Model.Artist import Interpreter
from src.Model.DB import Database
class Miner:
    def __init__(self, path):
        if path is None:
            self.path='/home/lautimartner/Music'
        else:
            self.path = path

    def startMining(self, dao):
        albID = 0
        interID = 0
        for dirpath, dirs, files in os.walk(self.path, topdown=True):
            for file in files:
                filepath = dirpath + os.sep + file
                if filepath.endswith(".mp3"):
                    try:
                        id3song = ID3(filepath)
                        newSong = self.createSong(id3song, filepath)
                        dao.songList.append(newSong)

                        if newSong.album not in dao.albumDic:
                            newAlbum = self.createAlbum(newSong, albID, dirpath)
                            dao.albumDic[newSong.album] = newAlbum
                            albID += 1
                        if newSong.interpreter not in dao.interDic:
                            newArtist = self.createArtist(interID, newSong)
                            dao.interDic[newSong.interpreter]=newArtist
                            interID += 1
                    except ID3NoHeaderError as e:
                        continue
                    except Exception as e:
                        print(e)
                else:
                    continue



    def createSong(self, id3obj, filepath):
        song = Song(id3obj, filepath)
        return song

    def createAlbum(self, song, id, dirpath):
        album = Album(song, id, dirpath)
        return album

    def createArtist(self, id_art, song ):
        artist = Interpreter(id_art, song)
        return artist

if __name__ == '__main__':
    try:
        os.remove('/home/lautimartner/Documents/Modelado/MP3Player/database.db')
    except:
        pass
    miner = Miner(None)
    db = Database()
    miner.startMining(db)
    db.createDB()
    db.populatePerformersTable()
    db.populateAlbumsTable()
    db.populateSongsTable()


    print ('Todo bien')
