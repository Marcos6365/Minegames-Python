#classe para partida
from random import randint

class Partida:

    def __init__(self, lista_de_palavras: list) -> None:
        self.__lista_de_palavras = lista_de_palavras
        self.__palavra = str()
        self.__interface_palavra = list()
        self.__letras_certas = list()
        self.__letras_erradas = list()
        self.__tentativas = 0
        
    
    def definir_palavra(self) -> None:
        self.__palavra = self.__lista_de_palavras[randint(0, len(self.__lista_de_palavras) -1)]
        for indice in self.__palavra:
            if indice == '-':
                self.__interface_palavra.append(' ')
            else:
                self.__interface_palavra.append('_')
    
    
    def apresentar_palavra(self) -> None:
        palavra = '.'.join(self.__interface_palavra)
        if palavra[0].isalpha:
            print(palavra.title())
        else:
            print(palavra)
    
    
    def jogada(self, resposta: str) -> None:
        if resposta in self.__letras_certas or resposta in self.__letras_erradas:
            print(f'A letra {resposta.upper()} já foi imformada!')
        
        else: 
            test = False
            indice = -1
            for letra in self.__palavra:
                indice += 1
                if resposta == letra:
                    test = self.__acerto(indice, letra)
                elif resposta == 'c' and letra == 'ç':
                    test = self.__acerto(indice, letra)
                elif resposta == 'a' and letra in ['à', 'á', 'ã', 'â']:
                    test = self.__acerto(indice, letra)
                elif resposta == 'e' and letra in ['ê', 'é', 'è']:
                    test = self.__acerto(indice, letra)
                elif resposta == 'i' and letra in ['í', 'ì', 'î']:
                    test = self.__acerto(indice, letra)
                elif resposta == 'o' and letra in ['ò', 'ó', 'ô', 'õ']:
                    test = self.__acerto(indice, letra)
                elif resposta == 'u' and letra in ['ú', 'ù', 'û']:
                    test = self.__acerto(indice, letra)
            if not test:
                print(f'Não tem {resposta.upper()} na palavra!')   
                self.__tentativas += 1
                self.__letras_erradas.append(resposta)
                
                   
    def __acerto(self, indice: int, letra: str) -> bool:
        self.__interface_palavra[indice] = letra
        if letra not in self.__letras_certas:
            self.__letras_certas.append(letra)
        return True
    
    
    def analise(self) -> bool:
        if self.__interface_palavra.count('_') == 0 or self.__tentativas == 7:
            return False
        else:
            return True
    
    
    def finalizar(self) -> None:
        if '-' in self.__palavra:
            self.__palavra = self.__palavra.replace('-', ' ')
        if self.__tentativas == 7:
            print(f'VOCÊ PERDEU!\nA palavra certa é {self.__palavra.upper()}')
        else:
            print(f'VOCÊ GANHOU!\nA palavra é exatamente {self.__palavra.upper()}')        
    
    @staticmethod
    def leia_letra() -> str:
        while True:
            letra = str(input('Digite uma letra: ')).strip().lower()
            if letra.isalpha() and len(letra) == 1:
                return letra
            else:
                if letra.isalpha() and len(letra) > 1:
                    print('Digite apenas uma letra!')
                else:
                    print('Digite apenas letras alfabéticas!')
                
    
    def apresentar_estatisticas(self) -> None:
        print('Acertos: ', end = '')
        if len(self.__letras_certas) == 0:
           print('nenhum', end = '   ') 
        else:
           for indice, letra in enumerate(self.__letras_certas):
               if indice == 0:
                    print(f'{letra.upper()}', end = '')
               else:
                    print(f',{letra.upper()}', end = '')
           print(end = '   ') 
        print('Erros: ', end = '')
        if len(self.__letras_erradas) == 0:
            print('nenhum', end = '   ')
        else:
            for indice, letra in enumerate(self.__letras_erradas):
                if indice == 0:
                    print(f'{letra.upper()}', end = '')
                else:
                    print(f',{letra.upper()}', end = '')
            print(end = '   ')
        print()
        print('-'* 40)
            
    
    def apresentar_boneco(self) -> None:
        from games.jogo_da_forca.class_package.class_partida.boneco import apresentar_boneco_
        apresentar_boneco_(self.__tentativas)
 
