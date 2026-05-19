matriz = [
    [10,20,30],
    [40,50,60],
    [15,15,15]
]

pares=0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            pares+=1

print(f'qtd pares: {pares}')