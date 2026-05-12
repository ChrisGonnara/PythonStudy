def soma_intervalo(n1,n2):
    soma=0
    for numeros in range (n1,n2+1):
        soma +=numeros
    return soma

def main():
    n1=int(input('numero 1: '))
    n2=int(input('numero 2: '))

    print(soma_intervalo(n1,n2))
main()