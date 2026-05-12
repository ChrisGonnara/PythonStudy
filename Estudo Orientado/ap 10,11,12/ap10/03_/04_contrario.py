def contrario():
    palavras=[]
    for i in range(8):
        p=input('palavra: ')
        palavras.append(p)


    posicao= len(palavras)-1
    while posicao >= 0:
        print(palavras[posicao])
        posicao-=1
contrario()
