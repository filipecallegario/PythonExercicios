import requests

def verificarsite(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(f'O site {url} está online')
        else:
            print(f'O site {url} respondeu com código de status: {resposta.status_code}')
    except requests.exceptions.RequestException as erro:
        print(f'Erro ao tentar acessar o site {url}: {erro}')

url = str(input('Digite o site que quer verificar: '))
verificarsite(url)