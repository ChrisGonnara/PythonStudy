#TC1: 50,30,120,0 > 200, GRATIS        #TC2: 40,25,60,0, > 125, PAGO

def ex01():
    produto = float (input('Digite preço produto: '))
    total = produto

    while produto != 0:
        produto=float(input('Digite preço produto: '))
        total = total + produto

    print(f'Total a pagar: {total:.2f}')
    if total >= 200:
        print('Frete gratis')
    else:
        print('Frete pago')


def ex02():
    #TC1: 3 > 6
    n=int(input('numero positivo: '))
    contador = 0
    soma=0
    while contador < n:
        contador+=1
        soma = soma + contador
    print(f'Somatório: {soma}')

ex02()