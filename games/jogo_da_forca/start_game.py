#Módulo para start_game
def start_game() -> None:    
    from games.jogo_da_forca.interface_game import menu, linha, leia_sn 
    from games.jogo_da_forca.class_package.class_partida import Partida
    from games.jogo_da_forca.class_package.class_generos import Generos
    
    while True:
        while True:
            opç = menu('GENÈROS: \n[1] - ANIMAIS\n[2] - FRUTAS\n[3] - ESCOLA\n[0] - REUTURN TO MENU')
            if opç == 0:
                return
            elif opç == 1:
                genero_escolhido = Generos()
                jogo = Partida(genero_escolhido.generos['animais'])
                break
            elif opç == 2:
                genero_escolhido = Generos()
                jogo = Partida(genero_escolhido.generos['frutas'])
                break
            elif opç == 3:
                genero_escolhido = Generos()
                jogo = Partida(genero_escolhido.generos['escola'])
                break
            else:
                print('Opção inválida! Digite apenas as opções informadas...')
        
        jogo.definir_palavra()
        while jogo.analise():
            linha()
            jogo.apresentar_estatisticas()
            jogo.apresentar_boneco()
            jogo.apresentar_palavra()
            jogo.jogada(jogo.leia_letra())
        jogo.apresentar_estatisticas()
        jogo.apresentar_boneco()
        jogo.apresentar_palavra()
        jogo.finalizar()    
        resp = leia_sn('Deseja jogar novamente?[S/ N]: ')
        if resp == 'S':
            continue
        else:
            return
            