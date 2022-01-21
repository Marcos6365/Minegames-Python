# Módulo para a Classe Torneio
from typing import Type

class Jogador:
    pass

class Torneio:
    
    def __init__(self) -> None:
        self.__alternativas = list(range(1, 10))
        self.__tabuleiro = [list(range(7, 10)), list(range(4, 7)), list(range(1, 4))]
        
        
    def apresentar_tabuleiro(self) -> None:
        
        for linha in self.__tabuleiro:
            for elemento in range(0, 3):
                print(f'[{linha[elemento]:2}]', end = '')
            print()
        print()
    
    
    def __reorganizar_tabuleiro(self, simbolo: str, num: int) -> any:
        for linha in self.__tabuleiro:
            for elemento in linha:
                if elemento == num:
                    self.__tabuleiro[self.__tabuleiro.index(linha)][linha.index(elemento)] = simbolo
                    self.__alternativas.remove(num)
                    return
    
    
    def recomecar_partida(self) -> None:
        self.__alternativas = list(range(1, 10))
        self.__tabuleiro = [list(range(7, 10)), list(range(4, 7)), list(range(1, 4))]
    
    
    def round(self, j1: Type[Jogador], j2: Type[Jogador]) -> bool:
        if len(self.__alternativas) == 0:
            print('Deu velha!')
            return True
        
        if j1.vez:
            posicao = j1.jogada(self.__alternativas)
            simbolo = 'X'
            self.__reorganizar_tabuleiro(simbolo, posicao)
            if j1.analise():
                self.apresentar_tabuleiro()
                print(f'{j1.nome} é o CAMPEÃO!')
                return True               
            j1.vez = False
            j2.vez = True
        
        elif j2.vez:
            posicao = j2.jogada(self.__alternativas)
            simbolo = 'O'
            self.__reorganizar_tabuleiro(simbolo, posicao)
            if j2.analise():
                self.apresentar_tabuleiro()
                print(f'{j2.nome} é o CAMPEÃO!')
                return True           
            j1.vez = True
            j2.vez = False
                
        if not j1.analise() and not j2.analise():
            return False
            