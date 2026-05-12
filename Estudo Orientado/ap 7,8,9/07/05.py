# input qtd_mesas
# cada mesa -- input qtd_pedidos
# cada pedido -- input (1-Ham  RS18,2 -Refri RS18,2, sOBREMESA RS 9) e quantidade
# mostre total de cada mesa
#mostrar faturamento total do dia
faturamento_total=0
qtd_mesas = int(input('quantidade mesas: '))

for mesa in range (1,qtd_mesas+1):
    total_mesa=0
    qtd_pedido=int(input('quantidade de pedidos: '))
    
    for pedido in range (1,qtd_pedido+1):
        print('Hamburguer, Refri, Sobremesa')
        escolha=int(input('1- R$ 18, 2- 6,0 3- 9,0: '))
        qtd=int(input('quantidade: '))

        if escolha ==1:
            total_mesa += 18 * qtd
        elif escolha == 2:
            total_mesa += 6 * qtd
        else:
            total_mesa += 9 * qtd

    print(f'total mesa {mesa}: {total_mesa}')
    faturamento_total += total_mesa
print(f'faturamento total= {faturamento_total}')

