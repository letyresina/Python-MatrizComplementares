'''
    Exercício 1:
    Preencha uma matriz 5x5 com números aleatórios (de 1 a 25), de forma que nenhum número se repita na 
    matriz, ou seja, caso o número sorteado já esteja contido na matriz, outro número deve ser sorteado
'''

# Importações do código

from moduloMatriz import exibeMatriz

from random import randint

# Criando matriz 

matriz = []

sorteados = []

# Preenchendo a matriz

for linha in range(5):
    lista = []
    for coluna in range(5):
        num = randint(1,25)
        while num in sorteados:
            num = randint(1,25)
        lista.append(num)
        sorteados.append(num)
    matriz.append(lista)

exibeMatriz(matriz)