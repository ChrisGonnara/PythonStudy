def dobro(numero):
    if numero >0:
        return numero*2
    else:
        return numero 
    
def main():
    numero=int(input('numero: '))
    print(dobro(numero))
main()