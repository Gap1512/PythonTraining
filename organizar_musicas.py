#coding : UTF-8
import eyed3
import os
import pathlib

print("Insira o diretório no qual estão os arquivos .mp3 que serão renomeados")
src = input()
list = os.listdir(src)

class Music:
    __name = ""
    __artist = ""
    __album = ""
    __number = ""

    def __init__(self, name="", artist="", album="", number=""):
        self.__name = name
        self.__artist = artist
        self.__album = album
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_artist(self, artist):
        self.__artist = artist

    def set_album(self, album):
        self.__album = album

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_artist(self):
        return self.__artist

    def get_genre(self):
        return self.__genre

    def get_album(self):
        return self.__album

    def get_number(self):
        return self.__number

def rename(Music):

    new_name = (Music.get_number() \
               + " - " \
               + Music.get_name() \
               + " [" \
               + Music.get_artist() \
               + "]")
    return new_name

def main ():

    i = 0
    k = 0

    for filename in list:

        j = 0

        file_path = src + "/" + filename
        file_extension = pathlib.Path(file_path).suffix

        if file_extension != '.mp3':
            k += 1
            print("Arquivo '%s' não foi renomeado, visto que não possui extensão '.mp3'" % (filename))

        else:
            audio_file = eyed3.load(file_path)

            if audio_file.tag is None:
                title = filename
                title = title.replace('.mp3',"")
                artist = "Desconhecido"
                album = "Desconhecido"
            else:
                title = audio_file.tag.title
                artist = audio_file.tag.artist
                album = audio_file.tag.album

            music_file = Music(title,
                               artist,
                               album,
                               str(i + 1))
            new_name = rename(music_file)

            for ch in [':', '<', '>', '/', '|', '?', '*', "\"", "\\"]:
                if ch in new_name:
                    new_name = new_name.replace(ch, "-")

            dst = src + "/" + new_name + ".mp3"

            while os.path.exists(dst) and file_path != dst:

                dst = src + "/" + new_name + "(" + str(j+1) + ")" + ".mp3"
                j += 1

            os.rename(file_path, dst)
            i += 1
    if k != list:
        print("Os arquivos foram renomeados")

if __name__ == '__main__':
    main()