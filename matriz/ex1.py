def soma_matriz(linha: int, coluna: int) -> int:
    '''
    Recebe uma matriz 4x3 e retorna a soma dos elementos dessa matriz.
    Exemplos.
    soma_matriz(4, 3)
    '''
    matriz = []
    for j in range(linha):
        linhaa = []
        for i in range(coluna):
            linhaa.append(int(input('insira o valor: ')))
            matriz.append(linhaa)

    for j in range(coluna):
        print('Elemento [0,",j,"]: ', matriz[0][j])

    soma = matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[2][0] + matriz[2][1] + matriz[2][2] + matriz[3][0] + matriz[3][1] + matriz[3][2]
    print(soma)
    return soma

soma_matriz(4,3)

# def soma_matriz() -> list:
#     matriz = [[1, 2, 3],
#               [4, 5 ,6],
#               [7, 8 ,9],
#               [10, 11, 12]]
#     # soma = matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[2][0] + matriz[2][1] + matriz[2][2] + matriz[3][0] + matriz[3][1] + matriz[3][2]
#     print("A soma dos elementos dessa matriz é igual a", matriz[2][3])

#     return matriz
    