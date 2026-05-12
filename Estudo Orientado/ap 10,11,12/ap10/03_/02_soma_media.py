def soma_media():
    numeros = []
    for i in range (6):
        n=float(input('numero: '))
        numeros.append(n)
    
    soma=0
    for i in range(len(numeros)):
        soma += numeros[i]

    media =  soma / len(numeros)

    print(f'soma: {soma:.1f}')
    print(f'media: {media}')
soma_media()