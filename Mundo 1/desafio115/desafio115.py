from uteis import cores, interface
from time import sleep

while True:
    interface.cab('MENU PRINCIPAL')
    print(f'{cores.yellow("1 -")} {cores.blue("Ver pessoas cadastradas")} \n{cores.yellow("2 -")} {cores.blue("Cadastrar novas pessoas")} \n{cores.yellow("3 -")} {cores.blue("Sair do sistema")}')
    interface.linha()
    while True:
        try:
            res = int(input('Escolha uma opção: '))
        except (TypeError, ValueError):
            print(cores.red('Erro!! Digite um número inteiro entre 1 e 3!'))
        else:
            if 1 <= res <= 3:
                break
            else:
                print(f'{cores.red("Erro!! Digite um valor entre 1 e 3!")}')
    if res == 1:
        arquivo = open('Mundo 1\desafio115\pessoas.txt', 'r')
        print(arquivo.read())
        sleep(2)
    elif res == 2:
        nome = str(input('Digite o nome da pessoa: ')).capitalize()
        while True:
            idade = int(input('Digite a idade: '))
            try:
                idade = int(idade)
            except (ValueError, TypeError):
                print(cores.red('Erro!! Digite um valor inteiro!'))
            except:
                print(cores.red('Erro!! Tente novamente!'))
            else:
                break
        arquivo = open('Mundo 1\desafio115\pessoas.txt', 'a')
        arquivo.write('\n')
        arquivo.write(f'{nome:<25}')
        arquivo.write(f'{idade} anos')
        arquivo.close()
        print(f'{nome} foi adicionado com sucesso!')
        sleep(2)
    else:
        interface.cab('Saindo do Sistema... Volte Sempre!!')
        break