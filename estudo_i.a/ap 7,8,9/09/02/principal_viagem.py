from funcoes_viagem import *

def main():
    #passagem
    valor_base=float(input('valor base: '))
    bagagem=float(input('valor bagagem: '))

    #hospedagem
    valor_diaria= float(input('Valor diaria: '))
    dias= int(input('dias: '))
    taxa_extra = int(input('taxa extra (opcional): '))

    #duracao
    total_horas=int(input('total horas: '))

    #orcamento
    alimentacao=int(input('valor alimentacao: '))
    #--hospedagem
    #--passagem

    #processamento
    passagem=calcular_passagem(valor_base, bagagem)
    hospedagem= calcular_hospedagem(valor_diaria, dias,taxa_extra)
    dias_duracao, horas_duracao= converter_duracao(total_horas)
    custo_fixo, custo_extra, total = calcular_orcamento(passagem,hospedagem,alimentacao)

    #prints
    print(f'passagem: {passagem:.2f} ')
    print(f'hospedagem: {hospedagem:.2f}')
    print(f'duracao {dias_duracao} dia(s) e {horas_duracao} hora(s)')
    print(f'custo fixo: R$ {custo_fixo:.2f} ')
    print(f'custo extra; R$ {custo_extra:.2f}')
    print(f'total: R$ {total:.2f}')

main()
