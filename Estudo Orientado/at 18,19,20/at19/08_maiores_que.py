matriz = [
    [10,20,30],
    [40,50,60],
    [15,15,15]
]

informado=int(input('informado: '))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > informado:
            print(matriz[i][j])