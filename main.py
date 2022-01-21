#MENU DO FLIPERAMA

from games.jogo_da_velha.main_game import jogo_da_velha
from games.jogo_da_forca.main_game import jogo_da_forca
from time import sleep

lista_games = ['[1] - JOGO DA VELHA', '[2] - JOGO DA FORCA', '[0] - Sair']
while True:
    print('='* 35)
    print('FLIPERAMA'.center(35))
    print('='* 35)
    for jogo in lista_games:
        print(jogo)
    print('='* 35)
    while True:
        try:
            opç = int(input('opç: '))
        except:
            print('opção inválida!')
        else:
            break
    if opç == 1:
        print('Acessando jogo da velha...')
        sleep(1.5)
        jogo_da_velha()
    if opç == 2:
        print('Acessando jogo da forca...')
        sleep(1.5)
        jogo_da_forca()
    elif opç == 0:
        break
    else:
        print('opção inválida!')
        
