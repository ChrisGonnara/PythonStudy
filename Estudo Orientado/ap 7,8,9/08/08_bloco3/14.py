def eh_par(numero):
    if numero % 2 == 0: return True
    else: return False

def contar_pares_faixa(inicio,fim):
    contador=0
    for i in range (inicio, fim+1):
        if eh_par(i):
            contador+=1
    return contador

def main():
    inicio = int(input('inicio faixa: '))
    fim= int(input('final faixa: '))

    contar_pares=contar_pares_faixa(inicio,fim)

    print(f'quantidade pares: {contar_pares}')
main()