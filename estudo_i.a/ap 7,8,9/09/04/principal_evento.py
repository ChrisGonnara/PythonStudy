from funcoes_evento import *

for i in range (1,3+1):
    nome=input('nome: ')
    tipo_ingresso = input('Tipos. regular,vip,estudante: ')
    qtd_oficinas_extras = int(input('oficinas extra qtd: '))
    material_extra = input('MATERIAL EXTRA: s/n')
    material_extra = material_extra == 's' 
    valor_padrao=120
    cupom=int(input('Cupom desconto: '))

    valor_base, valor_oficinas, valor_material,desconto,taxa,valor_final,classificacao=\
    gerar_relatorio_participante(nome,tipo_ingresso,valor_padrao,qtd_oficinas_extras,material_extra,cupom)

    print(f'nome: {nome}, tipo: {tipo_ingresso}')
    print(f'valor base: {valor_base}')
    print(f'valor oficinas: {valor_oficinas}')
    print(f'Valor material: {valor_material}')
    print(f'Valor do desconto: {desconto}')
    print(f'valor da taxa: {taxa}')
    print(f'valor final: {valor_final}')
    print(f'Classificação: {classificacao}')