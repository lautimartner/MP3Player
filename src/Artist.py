from Song import Song

class Interpreter:
    """Clase que representa un objeto interprete y sus atributos"""
    def __init__(self, id_per, song):
        self.id_per = id_per
        self.id_type = None
        self.name = song.interpreter


if __name__ == '__main__':
    print('Todo bien')