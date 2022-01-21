# Módulo de interface

def titulo(txt):
    print('=' * 40)
    print(txt.center(40))
    print('=' * 40)
    

def linha():
    print('=' * 40)


def menu(txt):
    print(txt)
    linha()
    return leia_int('opç: ')


def leia_int(txt):
    while True:    
        try:
            num = int(input(txt))
        except:
            print('Valor inválido!')
        else:
            return num

def leia_sn(txt):
    while True:
        resp = input(txt).strip().upper()
        if resp in ['S', 'N']:
            return resp
        else:
            print('Opção inválida!')
          