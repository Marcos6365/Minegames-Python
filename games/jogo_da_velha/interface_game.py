# Módulo de Interface

def titulo(txt: str) -> None:
    print('='* 30)
    print(txt.center(30))
    print('='* 30)
    

def linha() -> None:
    print('='* 30)
    

def menu(txt: str) -> int:
    print(txt)
    linha()
    while True:
        try:
            opç = int(input('opç: '))
        except:
            print('opção inválida!')
        else:
            return opç
    

def teste_de_decisao() -> str:
    while True:
        resp = str(input('Jogar novamente?: [s, n]')).upper().strip()
        if resp in ['S', 'N']:
            return resp
        else:
            print('Opção inválida!')