from time import sleep


def cabecalho(txt:str):
    print('---'*10)
    print(txt.center(30))
    print('---'*10)


def criar_arq():
    file = 'arq.txt'
    try:
        with open(file, "r"):
           pass
    except:
        print('Arquivo \'arq.txt\' criado com sucesso!')
        with open(file, 'w'):
            pass
    else:
        print('Arquivo \'arq.txt\' ja existe!')



def menu(lista:list):
    cabecalho('Menu')
    for i, c in enumerate(lista):
        print(f'\033[34m{i+1}\033[m - {c}')
    print()
    opcao = int(input('\033[33mSua opção: \033[m'))
    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        cabecalho('Desligando sistema...')
        sleep(1)
        print('Obrigado por acessar nosso programa...')

