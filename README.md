# MP3Player
Proyecto para clase de Modelado y Programacion de Ciencias de la Computacion, Facultad de Ciencias, UNAM
### Bibliotecas usadas
* Python 3
* Python bindings for VLC
* Mutagen
* SQLite 3
* PyQt5
### Descargar
git clone https://github.com/lautimartner/MP3Player.git
### Como ejecutar
Dentro de MP3Player/src ejecutar: `python3 gui.py` . Tambien pueden crear una ejecutable con bash.
### Guia rapida de uso
Una vez abierto el programa, picar el boton de Show Songs para que empiece a minar canciones de la carpeta `$/home/USER/Music` o solo haga una consulta a la base de datos si ya existe. Para reproducir hay que seleccionar una cancion y poner el boton Play/Pause, para hacer pausa el mismo boton es usado, para reproducir otra cancion hay que hacer click en el boton Stop primero. Para crear una persona y grupo el procedimiento es obvio y ligar personas a grupos y viceversa igual. 

Para hacer busquedas se utiliza el siguiente lenguaje:
* `[consulta]` Busca consulta en todos los campos
* `a: [album name]`
* `p: [performer name]`
* `s: [song name]`
* `y: [year]`
* `g: [genre name]`
* Para buscar varios campos a la vez con una conjuncion se utiliza `|`entre cada busqueda (notese la ironia), sin espacios antes de cada `|`. Por ejemplo `a: The Beatles| p: Help| s: Help`.
