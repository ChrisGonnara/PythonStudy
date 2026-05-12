def ler_numeros():
    lista = []
    for cada in range (5):
        numero= int(input('numero: '))
        lista.append(numero)
    return lista


def exibir_invertido(lista):
    posicao=len(lista)-1
    while posicao >=0:
        print (lista[posicao])
        posicao -=1

numeros=ler_numeros()
exibir_invertido(numeros)