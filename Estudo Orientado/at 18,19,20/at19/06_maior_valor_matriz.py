matriz = [
    [10,20,30],
    [40,50,60],
    [15,15,15]
]

maior = matriz[0][0]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior=matriz[i][j]
print(maior)