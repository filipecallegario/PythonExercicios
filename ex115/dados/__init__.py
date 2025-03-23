from time import sleep

dados = []

def cadastrar():
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    dados.append([nome, idade])
    with open('arquivo.txt', 'a') as arquivo:
        arquivo.write(f'{nome:<35} {idade} anos\n')
    print(f'Novo registro de {nome} adicionado.')

def verpessoas():
    print(f'~' * 45)
    print(f'{"PESSOAS CADASTRADAS":^45}')
    print(f'~' * 45)
    with open('arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
        for linha in conteudo:
            print(linha.strip())
    sleep(3)

def apagar():
    with open("arquivo.txt", "w") as arquivo:
        pass
    print("Todos os registros foram apagados.")

