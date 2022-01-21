# Classe Generos

class Generos:
    
    def __init__(self) -> None:
        self.__generos = dict()
        
        self.__generos['animais'] = ['gato', 'cachorro', 'canguru', 'serpente', 
                                     'morcego', 'cavalo', 'urubu', 'girafa', 
                                     'zebra', 'coelho', 'tigre', 'leão', 'hipopótamo',
                                     'macaco', 'javali', 'gavião', 'gorila', 'gírafa',
                                     'tamanduá']

        self.__generos['frutas'] = ['abacaxi', 'maça', 'pessêgo', 'manga', 'banana', 
                                   'uva', 'morango', 'cocô', 'franboesa', 'cereja',
                                   'goiaba', 'maracujá', 'carambola', 'tomate']
        
        self.__generos['escola'] = ['lápis', 'borracha', 'caderno', 'quadro-negro',
                                   'professor', 'aluno', 'diretoria', 'biblioteca']
                                        
    @property
    def generos(self) -> None:
        return self.__generos
 
