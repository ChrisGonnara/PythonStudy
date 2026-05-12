def maior_menor_posicao():
    numeros=[]
    for i in range (7):
        n=int(input('numero: '))
        numeros.append(n)

    maior=numeros[0]
    menor=numeros[0]
    posicao_maior=0
    posicao_menor=0

    for i in  range (0,len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
            posicao_maior=i
        if numeros[i] <menor:
            menor=numeros[i]
            posicao_menor=i
    
    print(f'maior: {maior} posicao: {posicao_maior}')
    print(f'menor: {menor} posicao: {posicao_menor}')

maior_menor_posicao()