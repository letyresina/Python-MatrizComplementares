'''
    Exercício 2:
    Preencha uma matriz 5x5 e informe se essa matriz é ou não simétrica. Uma matriz é considerada simétrica 
    quando ela é igual a sua transposta.
'''
# Importações

from moduloMatriz import exibeMatriz

# Código geral

matriz = []

for linha in range(5):
    lista = []
    for coluna in range(5):
        num = int(input("Digite um número inteiro: "))
        lista.append(num)
    matriz.append(lista)

exibeMatriz(matriz)

matrizTransposta = []

for i in range(len(matriz[0])):
    linhaTransposta = []
    for j in range(len(matriz[0])):
        linhaTransposta.append(matriz[j][i])
    matrizTransposta.append(linhaTransposta)

print("Matriz Transposta")
exibeMatriz(matrizTransposta)

if matriz == matrizTransposta:
    print("A matriz é simétrica")
else:
    print("A matriz nao é simétrica")