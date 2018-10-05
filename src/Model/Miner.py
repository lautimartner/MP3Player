import sqlite3
import os
from Song import Song
from mutagen.id3 import *
from mutagen.id3._util import *
class Miner:
    def __init__(self):
        self.minedSongs = []
        self.minedAlbums = []

    def startMining(self):
        for dirpath, dirs, files in os.walk('/home/lautimartner/Music', topdown=True):
            for file in files:
                filepath = dirpath + os.sep + file
                if dirpath not in self.minedAlbums:
                    self.minedAlbums.append(dirpath)
                if filepath.endswith(".mp3"):
                    try:
                        id3song = ID3(filepath)
                        newsong = self.createSong(id3song, filepath)
                        self.minedSongs.append(newsong)
                    except ID3NoHeaderError as e:
                        continue
                    except Exception as e:
                        print(e)
                else:
                    continue



    def createSong(self, id3obj, filepath):
        song = Song(id3obj, filepath)
        return song

    def printMinedSongs(self):
      for song in self.minedSongs:
        print("Artist: %s \n Track: %s " %(song.interpreter, song.songtitle))

    def printMinedAlbums(self):
        for album in self.minedAlbums:
            print(str(album))

if __name__ == '__main__':
    miner = Miner()
    miner.startMining()
    miner.printMinedSongs()
    print ('Todo bien')
