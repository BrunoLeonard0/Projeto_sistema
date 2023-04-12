from time import sleep


def cabecalho(txt:str):
    print('---'*10)
    print(txt.center(30))
    print('---'*10)

file = 'arq.txt'
def criar_arq():
    try:
        with open(file, "r"):
           pass
    except:
        print('Arquivo \'arq.txt\' criado com sucesso!')
        with open(file, 'w'):
            pass
    else:
        print('Arquivo \'arq.txt\' ja existe!')


def escrever_arq():
    with open(file, 'a') as arquivo:
        arquivo.write(input('Nome: '))
        arquivo.write('\t\t')
        arquivo.write(input('CPF: '))
        arquivo.write('\n')


def ler_arq():
    with open(file, 'r') as arquivo:
        return arquivo.read()
    

def menu(lista:list):
    while True:
        cabecalho('Menu')
        for i, c in enumerate(lista):
            print(f'\033[34m{i+1}\033[m - {c}')
        print()
        opcao = int(input('\033[33mSua opção: \033[m'))
        if opcao == 1 or 2 or 3:    
            while True:
                if opcao == 1:
                    cabecalho('Abrir cadastro')
                    escrever_arq()
                    sleep(1)
                    break
                elif opcao == 2:
                    cabecalho('Visualizar cadastros')
                    print('NOME\t\tCPF')
                    print(ler_arq())
                    sleep(1)
                    break
                elif opcao == 3:
                    cabecalho('Desligando sistema...')
                    sleep(1)
                    print('Obrigado por acessar nosso programa...')
                    break
        else:
            print('\033[32mOpção inválida\033[m')
            continue      
        if opcao == 3:
            break

