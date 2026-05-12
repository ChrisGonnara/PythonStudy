def maior_sequencia_crescimento():
    numeros=[]
    sequencia_atual=1
    maior_sequencia=1

    for i in range (12):
        n=int(input('numero: '))
        numeros.append(n)

    for i in range(1,len(numeros)):
        if numeros[i] > numeros[i-1]:
            sequencia_atual +=1

            if sequencia_atual > maior_sequencia:
                maior_sequencia= sequencia_atual
        else:
            sequencia_atual=1


    print(f'maior tamanho sequencia: {maior_sequencia}')

maior_sequencia_crescimento()