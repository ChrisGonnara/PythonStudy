matriz = [
    [10,20,30],
    [40,50,60],
    [15,15,15]
]

for i in range(len(matriz)):
    soma=0
    for elemento in range(len(matriz[i])):
        soma+= matriz[i][j]
    media = soma/len(matriz[i])
    print(f'media jogador {i}: {media}')