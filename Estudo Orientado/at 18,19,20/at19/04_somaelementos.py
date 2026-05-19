matriz = [
    [10,20,30],
    [40,50,60],
    [15,15,15]
]
soma=0
for i in range (len(matriz)):
    for j in range(len(matriz[i])):
        soma+=matriz[i][j]
print(soma)
