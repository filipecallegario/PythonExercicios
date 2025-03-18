matriz = [[], [], []]

# Preenchendo a matriz
for l in range(3):  # Agora só precisa de um loop para as 3 linhas
    for c in range(3):  # Para as 3 colunas
        valor = int(input(f'Digite o valor [{l + 1}, {c + 1}] '))  # Indices ajustados para o padrão de 1 a 3
        matriz[l].append(valor)


# Exibindo a matriz
for linha in matriz:
    print(f'[{linha[0]:^5}] [{linha[1]:^5}] [{linha[2]:^5}]')