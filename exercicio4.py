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
   maiorNumero = None  # Definir maiorNumero para None a cada nova linha
   for coluna in range(6):
       num = randint(1, 50)
       lista.append(num)
       if maiorNumero is None or num > maiorNumero:
           maiorNumero = num
   matriz.append(lista)