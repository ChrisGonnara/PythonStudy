#leia qtd_times_camp
#cada time -- leia nome_time e qtd_jogos
#cada jogoo -- leia resultado: 'v' vitoria 'e' empate 'd' derrota
#mostre total de pontos cada time  (v3p E1p D0p)
#nome do time com mais ponto no final

qtd_times = int(input('qtd times: '))
maior_pontos= 0
melhor_time = ''

for time in range (1,qtd_times +1):
    pontos=0
    nome=input('nome time: ')
    qtd_jogos = int(input('qtd jogos: '))

    for jogo in range(1,qtd_jogos+1):
        resultado=input('Resultado[v/e/d]: ').lower()
        if resultado == 'v': pontos +=3
        if resultado == 'e': pontos +=1

    print (f'total pontos do {nome}: {pontos}')
    if pontos > maior_pontos:
        maior_pontos=pontos
        melhor_time= nome
print(f'melhor time: {melhor_time} | maior pontos: {maior_pontos}')