def comparando_elementos_vizinhos():
    temperaturas=[]
    aumentou,diminuiu,permaneceu=0,0,0

    for i in range(10):
        t=float(input('temperatura: '))
        temperaturas.append(t)

    for i in range (1,len(temperaturas)):
        if temperaturas[i] < temperaturas[i-1]:
            diminuiu+=1
        elif temperaturas[i] == temperaturas[i-1]:
            permaneceu +=1
        else:
            aumentou +=1

    print(temperaturas)
    print(f'qtd de vezes que aumentou: {aumentou}')
    print(f'qtd vezes manteve: {permaneceu}')
    print(f'qtd vezes diminuiu: {diminuiu}')

comparando_elementos_vizinhos()
