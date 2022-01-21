#script principal do jogo da forca
from time import sleep

def jogo_da_forca(): 
    from games.jogo_da_forca.interface_game import titulo, menu
    from time import sleep
    from games.jogo_da_forca.start_game import start_game

    while True:
        titulo('JOGO DA FORCA')
        opç = menu('[1] - START GAME\n[2] - ABOUT GAME\n[3] - EXIT')
        if opç == 1:
            start_game()
        elif opç == 2:
            print('Jogo criado por Marcos Vinícius...')
            sleep(2)
        elif opç == 3:
            print('Saindo...')
            sleep(1.5)
            break
        else:
            print('Opção inválida!')
 
