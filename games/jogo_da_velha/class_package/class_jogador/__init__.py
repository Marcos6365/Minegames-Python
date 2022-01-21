# Módulo para a Classe Jogador

class Jogador:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__contador = list()
        self.__vez = None
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self.__nome = str(novo_nome)
        
    
    @property
    def vez(self) -> bool:
        return self.__vez
    
    @vez.setter
    def vez(self, novo_valor: bool) -> None:
        if isinstance(novo_valor, bool):
            self.__vez = novo_valor
    
   
    def jogada(self, alternativas: list) -> int:
        if len(alternativas) == 9:
            caso = 'Primeira jogada!'
        else:
            caso = 'Próxima jogada!'
        while True:
            try:
                num = int(input(f'{caso} jogador: {self.__nome}\nresp: '))
            except:
                print(f'Digite um valor válido!')
                continue
            if num in list(range(1, 10)):
                if num not in alternativas:
                    print('Está posição já está ocupada!')
                else:
                    self.__contador.append(num)
                    return num
            else:
                print('Digite apenas as posições disponíveis!')
    
    
    def analise(self) -> bool:
        t = self.__contador
        if 1 in t and 2 in t and 3 in t:
            return True
        elif 1 in t and 4 in t and 7 in t:
            return True
        elif 7 in t and 8 in t and 9 in t:
            return True
        elif 3 in t and 6 in t and 9 in t:
            return True
        elif 1 in t and 5 in t and 9 in t:
            return True
        elif 3 in t and 5 in t and 7 in t:
            return True
        elif 2 in t and 5 in t and 8 in t:
            return True
        elif 4 in t and 5 in t and 6 in t:
            return True
        else:
            return False        
    
    
    def limpar(self):
        self.__contador = list()
        
        
    @classmethod
    def cadastro(cls, n: int) -> str:
        while True:
            try:
                nome = input(f'{n}º Jogador:  ')
                if nome == '':
                    print('inserir o nome por favor!')
                    continue
            except:
                print('Ocorreu algum erro! Digite seu nome denovo...')
            else:
                return cls(nome)
