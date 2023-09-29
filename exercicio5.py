'''
    Exercício 5:
    Uma matriz quadrada é chamada de "quadrado mágico" se a soma dos elementos de cada linha, cada coluna 
    e a soma dos elementos das diagonais principal e secundária são todos iguais. Escreva um programa que 
    preencha uma matriz 4x4 com valores informados pelo usuário e informe se ela é ou não um quadrado 
    mágico.
'''

# Importações

from moduloMatriz import exibeMatriz

# Criando matriz
matriz = []

for linha in range(4):
    lista = []
    for coluna in range(4):
        num = int(input("Digite um número inteiro: "))
        lista.append(num)
    matriz.append(lista)

# percorrer indices da matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if sum(matriz[i][j]) == matriz[i][j] * matriz[i][j]:
            print("TESTE")
           

exibeMatriz(matriz)