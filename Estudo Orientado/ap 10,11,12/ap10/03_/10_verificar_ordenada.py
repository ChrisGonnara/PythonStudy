def verificar_ordenada():
    numeros=[]
    crescente=True
    for i in range(8):
        n=int(input('numero: '))
        numeros.append(n)

    for i in range (1,len(numeros)):
        if numeros[i] < numeros[i-1]:
            crescente=False

    if crescente:
        print('A lista esta em ordem crescente')
    else:
        print('A lista nao esta em ordem crescente')
verificar_ordenada()