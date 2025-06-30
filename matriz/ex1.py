def soma_matriz(linha: int, coluna: int) -> int:
    matriz = []
    for j in range(linha):
        linhaa = []
        for i in range(coluna):
            linhaa.append(int(input('insira o valor: ')))
            matriz.append(linhaa)

    soma = matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[2][0] + matriz[2][1] + matriz[2][2] + matriz[3][0] + matriz[3][1] + matriz[3][2]
    print(soma)
    return soma

soma_matriz(4,3)
