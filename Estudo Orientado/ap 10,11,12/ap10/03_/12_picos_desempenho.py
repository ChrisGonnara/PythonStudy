def picos_desempenho():
    pontuacoes=[]
    valores=[]
    posicoes=[]
    picos=0
    for i in range(10):
        n=int(input('pontuacao: '))
        pontuacoes.append(n)

    for i in range (1,len(pontuacoes)-1):
        if pontuacoes[i] > pontuacoes[i-1] and pontuacoes[i] > pontuacoes[i+1]:
            picos+=1
            valores.append(pontuacoes[i])
            posicoes.append(i)

    print(f'Quantidade de picos: {picos}')
    print(f'Posicoes: {posicoes}')
    print(f'Valores: {valores}')
picos_desempenho()