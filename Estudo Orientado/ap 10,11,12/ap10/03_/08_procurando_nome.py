def procurando_nomes():
    nomes=[]
    encontrado=False
    contador=0

    for i in range(8):
        n=input('nome: ')
        nomes.append(n)

    procurado=input('procurando nome: ')

    for nome in nomes:
        if nome == procurado:
            encontrado=True
            contador+=1

    print(f'procurado: {procurado} ')
    if encontrado:
        print(f'encontrado | quantas vezes: {contador} ')
    else:
        print('nao encontrado')
procurando_nomes()
