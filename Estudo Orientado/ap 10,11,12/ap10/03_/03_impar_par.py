def impar_par():
    numeros=[]
    pares=[]
    impares=[]

    for i in range (10):
        n=int(input('numero: '))
        numeros.append(n)

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print(f'qtd pares: {len(pares)}')
    print(f'qtd impares: {len(impares)}')
    print(f'pares: {pares}')
    print(f'impares: {impares}')

impar_par()