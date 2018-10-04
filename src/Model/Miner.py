import sqlite3
import os
from Song import Song
from mutagen.id3 import *
from mutagen.id3._util import *
class Miner:
    def __init__(self):
        self.minedSongs = []


    def startMining(self):
        for dirpath, dirs, files in os.walk('/home/lautimartner/Music', topdown=True):
            for file in files:
                filepath = dirpath + os.sep + file
                if filepath.endswith(".mp3"):
                    try:
                        id3song = ID3(filepath)
                        newsong = self.createSong(id3song)
                        self.minedSongs.append(newsong)
                    except ID3NoHeaderError as e:
                        continue
                    except Exception as e:
                        print(e)
                else:
                    continue



    def createSong(self, id3obj):
        song = Song(id3obj)
        return song

if __name__ == '__main__':
    miner = Miner()
    miner.startMining()
