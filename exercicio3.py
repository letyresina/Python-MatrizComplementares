'''
    Exercício 3:
    Faça um programa que preenche uma matriz 7x7 com números aleatórios e gere uma lista de 7 elementos 
    que contenha o maior elemento de cada uma das linhas da matriz.
'''

# Importações

from moduloMatriz import exibeMatriz

from random import randint

# Criando matriz
matriz = []

# Lista de maiores números
maioresNumeros = []

for linha in range(7):
   lista = []
   maiorNumero = None  # Definir maiorNumero para None a cada nova linha
   for coluna in range(7):
       num = randint(1, 50)
       lista.append(num)
       if maiorNumero is None or num > maiorNumero:
           maiorNumero = num
   maioresNumeros.append(maiorNumero)  # Adicionar o maior número da linha à lista
   matriz.append(lista)
        


exibeMatriz(matriz)

print(maioresNumeros)