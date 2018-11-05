#coding:UTF-8

import os
import sys
import time

win = False
winner = ""
player = ""
i = 1
cod_input = ""
cod_translated = ""
log = open("logpartida.txt","w")

table = {'top_l': ' ',
        'top_m' : ' ',
        'top_r' : ' ',
        'mid_l' : ' ',
        'mid_m' : ' ',
        'mid_r' : ' ',
        'bot_l' : ' ',
        'bot_m' : ' ',
        'bot_r' : ' '}

cod = {'11':'top_l',
        '12':'top_m',
        '13': 'top_r',
        '21': 'mid_l',
        '22': 'mid_m',
        '23': 'mid_r',
        '31': 'bot_l',
        '32': 'bot_m',
        '33': 'bot_r'}

while not win:

    if (i % 2 == 0):
        player = "Jogador X"
        i -= 1
    else:
        i += 1
        player = "Jogador O"

    time.sleep(1/24)

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n{}|{}|{}\n- - -\n{}|{}|{}\n- - -\n{}|{}|{}\n".format(table['top_l'],
                                                                        table['top_m'],
                                                                        table['top_r'],
                                                                        table['mid_l'],
                                                                        table['mid_m'],
                                                                        table['mid_r'],
                                                                        table['bot_l'],
                                                                        table['bot_m'],
                                                                        table['bot_r']))

    print("%s, por favor digite o código correspondente à posição no qual deseja, conforme o código abaixo:\n" % (player))
    print("\n11|12|13\n--------\n21|22|23\n--------\n31|32|33\n")
    cod_input = input()

    while (cod_input != '11' and cod_input != '12' and cod_input != '13' and
           cod_input != '21' and cod_input != '22' and cod_input != '23' and
           cod_input != '31' and cod_input != '32' and cod_input != '33'):

        time.sleep(1 / 24)

        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n{}|{}|{}\n- - -\n{}|{}|{}\n- - -\n{}|{}|{}\n".format(table['top_l'],
                                                                      table['top_m'],
                                                                      table['top_r'],
                                                                      table['mid_l'],
                                                                      table['mid_m'],
                                                                      table['mid_r'],
                                                                      table['bot_l'],
                                                                      table['bot_m'],
                                                                      table['bot_r']))

        print("%s, valor inserido é inválido, digitar outro:\n" % (
            player))
        print("\n11|12|13\n--------\n21|22|23\n--------\n31|32|33\n")
        cod_input = input()

    cod_translated = cod[cod_input]

    while (table[cod_translated] == 'x' or table[cod_translated] == 'o'):

        time.sleep(1 / 24)

        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n{}|{}|{}\n- - -\n{}|{}|{}\n- - -\n{}|{}|{}\n".format(table['top_l'],
                                                                      table['top_m'],
                                                                      table['top_r'],
                                                                      table['mid_l'],
                                                                      table['mid_m'],
                                                                      table['mid_r'],
                                                                      table['bot_l'],
                                                                      table['bot_m'],
                                                                      table['bot_r']))

        print("%s, a célula informada já está preenchida, favor informar outra:\n" % (
            player))
        print("\n11|12|13\n--------\n21|22|23\n--------\n31|32|33\n")
        cod_input = input()

        while (cod_input != '11' and cod_input != '12' and cod_input != '13' and
               cod_input != '21' and cod_input != '22' and cod_input != '23' and
               cod_input != '31' and cod_input != '32' and cod_input != '33'):
            time.sleep(1 / 24)

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n{}|{}|{}\n- - -\n{}|{}|{}\n- - -\n{}|{}|{}\n".format(table['top_l'],
                                                                          table['top_m'],
                                                                          table['top_r'],
                                                                          table['mid_l'],
                                                                          table['mid_m'],
                                                                          table['mid_r'],
                                                                          table['bot_l'],
                                                                          table['bot_m'],
                                                                          table['bot_r']))

            print("%s, valor inserido é inválido, digitar outro:\n" % (
                player))
            print("\n11|12|13\n--------\n21|22|23\n--------\n31|32|33\n")
            cod_input = input()

        cod_translated = cod[cod_input]

    while (cod_input != '11' and cod_input != '12' and cod_input != '13' and
           cod_input != '21' and cod_input != '22' and cod_input != '23' and
           cod_input != '31' and cod_input != '32' and cod_input != '33'):

        time.sleep(1 / 24)

        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n{}|{}|{}\n- - -\n{}|{}|{}\n- - -\n{}|{}|{}\n".format(table['top_l'],
                                                                      table['top_m'],
                                                                      table['top_r'],
                                                                      table['mid_l'],
                                                                      table['mid_m'],
                                                                      table['mid_r'],
                                                                      table['bot_l'],
                                                                      table['bot_m'],
                                                                      table['bot_r']))

        print("%s, valor inserido é inválido, digitar outro:\n" % (
            player))
        print("\n11|12|13\n--------\n21|22|23\n--------\n31|32|33\n")
        cod_input = input()
        cod_translated = cod[cod_input]

    if (player == "Jogador X"):
        table[cod_translated] = 'x'
    else:
        table[cod_translated] = 'o'

    if((table['top_r'] == 'x' and table['top_m'] == 'x' and table['top_l'] == 'x') or
        (table['mid_r'] == 'x' and table['mid_m'] == 'x' and table['mid_l'] == 'x') or
        (table['bot_r'] == 'x' and table['bot_m'] == 'x' and table['bot_l'] == 'x') or
        (table['top_l'] == 'x' and table['mid_l'] == 'x' and table['bot_l'] == 'x') or
        (table['top_m'] == 'x' and table['mid_m'] == 'x' and table['bot_m'] == 'x') or
        (table['top_r'] == 'x' and table['mid_r'] == 'x' and table['bot_r'] == 'x') or
        (table['top_l'] == 'x' and table['mid_m'] == 'x' and table['bot_r'] == 'x') or
        (table['top_r'] == 'x' and table['mid_m'] == 'x' and table['bot_l'] == 'x')):

        win = True

        winner = "x"

    elif((table['top_r'] == 'o' and table['top_m'] == 'o' and table['top_l'] == 'o') or
        (table['mid_r'] == 'o' and table['mid_m'] == 'o' and table['mid_l'] == 'o') or
        (table['bot_r'] == 'o' and table['bot_m'] == 'o' and table['bot_l'] == 'o') or
        (table['top_l'] == 'o' and table['mid_l'] == 'o' and table['bot_l'] == 'o') or
        (table['top_m'] == 'o' and table['mid_m'] == 'o' and table['bot_m'] == 'o') or
        (table['top_r'] == 'o' and table['mid_r'] == 'o' and table['bot_r'] == 'o') or
        (table['top_l'] == 'o' and table['mid_m'] == 'o' and table['bot_r'] == 'o') or
        (table['top_r'] == 'o' and table['mid_m'] == 'o' and table['bot_l'] == 'o')):

        win = True

        winner = "o"

    elif(table['top_r'] != ' ' and table['top_m'] != ' ' and table['top_l'] != ' ' and
        table['mid_r'] != ' ' and table['mid_m'] != ' ' and table['mid_l'] != ' ' and
        table['bot_r'] != ' ' and table['bot_m'] != ' ' and table['bot_l'] != ' '):

        win = True

        winner = "Houve um empate"

    else:

        continue

time.sleep(1 / 24)

os.system('cls' if os.name == 'nt' else 'clear')

print("\n{}|{}|{}\n- - -\n{}|{}|{}\n- - -\n{}|{}|{}\n".format(table['top_l'],
                                                              table['top_m'],
                                                              table['top_r'],
                                                              table['mid_l'],
                                                              table['mid_m'],
                                                              table['mid_r'],
                                                              table['bot_l'],
                                                              table['bot_m'],
                                                              table['bot_r']))

if (winner == "o" or winner == "x"):
    print("\nO vencedor foi:", winner)
else:
    print("\n")
    print(winner)


text = "\n{}|{}|{}\n- - -\n{}|{}|{}\n- - -\n{}|{}|{}\n".format(table['top_l'],
                                                                        table['top_m'],
                                                                        table['top_r'],
                                                                        table['mid_l'],
                                                                        table['mid_m'],
                                                                        table['mid_r'],
                                                                        table['bot_l'],
                                                                        table['bot_m'],
                                                                        table['bot_r'])

log.write(text)

if (winner == "o" or winner == "x"):
    log.write("O vencedor foi: %s" % (winner))
else:
    log.write(winner)

print("\nEsta partida está salva no arquivo 'logpartida'\nObrigado por jogar!")

log.close()