#TC1 = -50, 120 > SEM MEDALHA
#TC2 = 70,120 > PRATA
#TC90,120 > OURO, DESTAQUE

pontos=int(input('pontuacao obtida: '))
tempo=int(input('Tempo: (min)'))

if pontos >= 90:
    print('Classificação Ouro')
    if tempo <=120:
        print('Participante destaque da competicao')

elif pontos >= 70:
    print('Prata')
elif pontos >=50:
    print('Bronze')
else:
    print('Sem medalha')