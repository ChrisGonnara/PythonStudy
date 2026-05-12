def segundo_maior_valor():
    numeros=[]
    for i in range(10):
        n=int(input('numero: '))
        numeros.append(n)

    if numeros[0] > numeros[1]:
        maior=numeros[0]
        segundo_maior=numeros[1]
    else:
        maior=numeros[1]
        segundo_maior=numeros[0]

    for i in range(len(numeros)):
        if numeros[i] > maior:
            segundo_maior=maior
            maior= numeros[i]
        elif numeros[i] > segundo_maior and numeros[i] !=maior:
            segundo_maior=numeros[i]

    if maior==segundo_maior:
        print('nao existe segundo maior valor distinto')
    else:
    
        print(f'maior: {maior}' )
        print(f'segundo maior: {segundo_maior} ')

segundo_maior_valor()
