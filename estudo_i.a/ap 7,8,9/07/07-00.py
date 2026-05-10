qtd_times= int(input('qtd times campeonato: '))
campeao=''
melhor_saldo_time = ""
saldo_maior=0
maior_pontos=0

for time in range(1,qtd_times+1):

    pontos=0
    saldo_total= 0
    nome=input('nome time: ')
    qtd_jogos = int(input('quantidade de jogos: '))

    for jogo in range(1,qtd_jogos+1):
        marcados = int(input('gols marcados: '))
        sofridos = int(input('gols sofridos: '))
        saldo = marcados-sofridos
        saldo_total +=saldo

        if saldo >0:
            pontos +=3
        elif saldo==0:
            pontos +=1

    print(f'saldo de gols: {saldo_total} | pontos: {pontos}')

    if pontos > maior_pontos:
        campeao = nome

    if saldo_total > saldo_maior:
        saldo_maior = saldo_total
        melhor_saldo_time = nome
    
print(f'campeao { campeao} | maior saldo: {melhor_saldo_time} com {saldo_maior}')



    