#coding: UTF-8

import os
import shutil
import pathlib

print("Insira o caminho no qual estão os arquivos a serem renomeados")
source = input()
list = os.listdir(source)

def main ():

    for filename in list:

        i = 0

        file_path = source + "/" + filename
        file_extension = pathlib.Path(file_path).suffix
        destiny = source + "/" + str(i + 1) + file_extension

        while os.path.exists(destiny):
            i += 1
            destiny = source + "/" + str(i + 1) + file_extension

        os.rename(file_path, destiny)
        i += 1

    print("Os arquivos foram renomeados")

if __name__ == '__main__':
    main()