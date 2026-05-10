#declarar faturamento total,maior_venda,melhor_vendedor

#ler qtd_vendores
#cada vendedor -- 
    #declarar valor_mes
    #ler nome e qtd_venda_mes
    #cada venda --
        #leia valor
        #valor_mes+=valor
    #faturamento_total+= valor_mes
    #mostre o total e comissao vendedor
    #se maior_venda= valor_mes:
        #maior_venda=valor_mes
        #melhor_vendedor = nome

#ao final mostrar melhor_vendedor + vendeu e faturamento total

faturamento_total = maior_venda = 0
melhor_vendedor = ''

qtd_vendedores = int(input('quantidade vendedores: '))
for vendedor in range (1,qtd_vendedores+1):
    valor_mes=0
    nome=input(f'{vendedor} nome vendedor: ')
    qtd_venda_mes= int(input('quantidade vendas mes: '))

    for venda in range(1,qtd_venda_mes+1):
        valor=float(input(f'{venda} Valor venda: '))
        valor_mes +=valor
    faturamento_total +=valor_mes
    comissao = valor_mes * 0.10
    print(f'Valor venda funcionario: {valor_mes}|comissao: {comissao}')

    if valor_mes > maior_venda:
        maior_venda=valor_mes
        melhor_vendedor = nome

print(f'melhor vendedor: {melhor_vendedor} | faturamento total: {faturamento_total}')