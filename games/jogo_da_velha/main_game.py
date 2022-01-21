 
def jogo_da_velha() -> None: 
    from time import sleep
    from games.jogo_da_velha.start_game import start_game
    from games.jogo_da_velha.interface_game import titulo, menu

    while True:
        titulo('JOGO DA VELHA')
        opç = menu('[1] - START GAME\n[2] - SOBRE O GAME\n[3] - EXIT')
        if opç == 1:
            start_game()
        elif opç == 2:        
            print('Jogo criado por Vinicius...')
            sleep(2)
        elif opç == 3:
            print('saindo do jogo...')
            sleep(1.5)
            break
        