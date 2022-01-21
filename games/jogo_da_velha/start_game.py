# Módulo da função Start_game
from games.jogo_da_velha.class_package.class_torneio import Torneio
from games.jogo_da_velha.class_package.class_jogador import Jogador
from games.jogo_da_velha.interface_game import *

def start_game() -> None:
    j1 = Jogador.cadastro(1)
    j2 = Jogador.cadastro(2)
    torneio = Torneio()
    j1.vez = inicio_j1 = True
    j2.vez = inicio_j2 = False
    while True:       
        titulo(f'{j1.nome} X {j2.nome}')
        torneio.apresentar_tabuleiro()
        fim = torneio.round(j1, j2)
        if fim:
            opç = teste_de_decisao()
            if opç == 'N':
                break
            else:
                titulo('Agora é o segundo jogador que começa!')
                j1.limpar()
                j2.limpar()
                torneio.recomecar_partida()
                if inicio_j1:
                    j1.vez = False
                else:
                    j1.vez = True
                
                if inicio_j2:
                    j2.vez = False
                else:
                    j2.vez = True
                                                