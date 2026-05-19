def processar_pedidos(estoque_inicial):
    peso=int(input('peso desejado: '))
    i=0
    estoque=estoque_inicial

    while peso >0 and estoque!=0:
        if peso <=estoque:
            estoque -=peso
            i+=1
        else:
            print('pedido negado')

        peso=int(input('peso desejado: '))
    print(f'total agricultores: {i} | sobra no silo = {estoque}')


def main():
    estoque=int(input('estoque inicial: '))
    processar_pedidos(estoque)
main()

        

