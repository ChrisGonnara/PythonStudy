from funcoes_treino import *

def main():
    calorias_base = int(input('Calorias: '))
    bonus=int(input('Bonus: '))

    tempo_principal=int(input('Tempo principal: '))
    aquecimento=int(input('Tempo aquecimento: '))

    meta=int(input('Meta Calorica: '))


    #processamento
    calorias = calcular_calorias(calorias_base,bonus)
    tempo_treino=calcular_tempo_treino(tempo_principal,aquecimento)
    horas,minutos=analisar_desempenho(tempo_treino)
    diferenca,atingiu,mensagem=consolidar_treino(calorias,tempo_treino,meta)

    print(f'Calorias totais: {calorias}')
    print(f'Tempo total: {tempo_treino}')
    print(f'tempo em horas e minutos: {horas}h {minutos}m')
    print(f'Diferenca pra meta: {diferenca}')
    print(f'Meta batida: {atingiu}')
    print(f'Mensagem final: {mensagem}')

    main()
