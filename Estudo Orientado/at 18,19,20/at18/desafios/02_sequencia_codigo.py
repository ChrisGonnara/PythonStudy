def ordem_crescente(lista):
    for i in range (1,len(lista)):
        if lista[i] <= lista[i-1]:
            return False
    return True

def main():
    lista=[]

    while len(lista) < 5:
        n=int(input('numero: '))
        lista.append(n)
    
    resultado = ordem_crescente(lista)
    print(resultado)
main()