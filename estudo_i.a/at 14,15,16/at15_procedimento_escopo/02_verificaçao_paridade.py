def verificar_paridade(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

def main():
    numero=int(input('numero: '))

    print(verificar_paridade(numero))
main()