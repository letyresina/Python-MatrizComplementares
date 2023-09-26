def exibeMatriz(matriz: list) -> None: 
    '''
        Exbir matriz formatada
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()