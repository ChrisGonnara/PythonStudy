def soma_digitos(numero):
    string=str(numero)
    soma=0

    for c in string:
        soma += int(c)
    return soma

def main():
    numero=int(input('numero: '))
    print(soma_digitos(numero))
main()