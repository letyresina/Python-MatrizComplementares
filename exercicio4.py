'''
    Exercício 4:
    Preencha uma matriz 6x6 com números aleatórios e multiplique cada elemento da matriz pelo maior 
    elemento de sua linha. Escrever a matriz original e a modificada.
'''

# Importações

from moduloMatriz import exibeMatriz

from random import randint

# Criando matriz
matriz = []

for linha in range(6):
   lista = []
   for coluna in range(6):
       num = randint(1, 50)
       lista.append(num)
   matriz.append(lista)

exibeMatriz(matriz)

maiores = []

for i in range(len(matriz)):
    maiorNumero = None
    for j in range(len(matriz[0])):
        if maiorNumero is None or matriz[i][j] > maiorNumero:
            maiorNumero = matriz[i][j]

    for j in range(len(matriz[0])):
        matriz[i][j] *= maiorNumero

print("Matriz modificada")
exibeMatriz(matriz)