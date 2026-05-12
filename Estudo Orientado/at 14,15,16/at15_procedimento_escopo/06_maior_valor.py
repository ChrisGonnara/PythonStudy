def maior_valor(sequencia):
    lista = sequencia.split()
    maior=int(lista[0])
    for numero in range (len(lista)):
        lista[numero] = int(lista[numero])
        if lista[numero] >= maior:
            maior = lista[numero]
    return maior

def main():
    sequencia=input('sequencia de numero, com espaco')
    print(maior_valor(sequencia))
main()
