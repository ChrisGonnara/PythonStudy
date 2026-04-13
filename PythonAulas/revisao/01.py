#primo
def ex01():
    #primo
    EhPrimo=True
    n=int(input('Numero: '))
    contador = 0

    if n <2:
        EhPrimo = False
    else:    
        for i in range (2,n+1):
            if n % i == 0:
                contador +=1

    if contador != 2:
        EhPrimo = False

    print(EhPrimo)



def ex02():
    #fibonacci
    n=int(input('numero: '))
    a=0
    b=1

    for i in range (1,n+1):
        print(a)
        proximo = a+b
        a=b
        b=proximo

def ex03():
    #fatorial
    n=int(input('numero: '))
    fatorial=1
    for i in range (1,n+1):
        fatorial *=i

    print(fatorial)


def ex04():
    #triangulo
    n=int(input('Altura: '))
    for i in range (n):
        for j in range (i+1):
            print('*', end='')
        print()


def ex05():
    #palindromo
    palavra=input('Texto: ')
    tamanho=len(palavra)
    eh_palindromo=True

    for i in range(tamanho):
        if palavra[i] != palavra[tamanho-1-i]:
            eh_palindromo=False
        if eh_palindromo:
            print('é palindromo')
        else:
            print('nao é palindromo')

def ex06():
    #prefixo palindromo
    palavra=input('Texto: ')
    tamanho=len(palavra)
    prefixo=''

    for i in range (tamanho):
        eh_palindromo=True
        prefixo+=palavra[i]

        for j in range (i+1):
            if palavra[j] != palavra[i-j]:
                eh_palindromo=False

        if eh_palindromo:
            print(prefixo)
ex06()
