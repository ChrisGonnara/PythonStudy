def ex01():
    #tabuada
    n=int(input('numero: '))
    for i in range (1,11):
        print(f'{n} * {i} = {n*i}')


def ex02():
    #fatorial
    n=int(input('numero: '))
    fatorial=1
    for i in range (1,n+1):
        fatorial *=i
    print(f'fatorial: {fatorial}')

def ex03():
    #fibonacci
    n=int(input('termos: '))
    t1=0
    t2=1
    print (f'os {n} primeiros termos sao: ')

    for i in range(n):
        print(t1)
        t3=  t1+t2

        t1=t2
        t2=t3


def ex04():
    #soma dos divisores de um numero

    n=int(input('Digite um numero: '))
    soma=0

    for i in range (1,n+1):
        if n % i == 0:
            soma +=i
    
    print(f'soma dos divisiores: {soma}')


def ex05():
    #verificacao de numero primo
    n=int(input('numero: '))
    contador = 0
    for i in range (1,n+1):
        if n % i == 0:
            contador +=1

    if contador == 2:
        print('O numero é primo')

    else:
        print('O numero nao é primo')


def ex06():
    #palavra invertida
    palavra=input('palavra: ')
    invertido= ''

    for letra in (palavra):
        invertido = letra + invertido

    print(invertido)


def ex07():
    #palindromo, igual de tras pra frente

    palavra=input('palavra: ')
    invertido=''

    for letra in (palavra):
        invertido = letra+invertido
    if invertido ==palavra:
        print('a palavra é um palindromo')
    else:
        print('a palavra nao é um palindromo')

def ex08():
    #ler numero string e somar os digitos

    n=str (input("numero: "))
    soma=0

    for i in (n):
        soma += int (i)
    print(soma)


def ex09():
    #numero perfeito
    #somar os divisiveis do numero, menor que ele
    n=int(input('numero: '))
    soma=0
    for i in range (1,n):
        if n % i == 0:
            soma+=i
        
    if soma == n:
        print(f'{soma}, numero perfeito')
    else:
        print(f'{soma}, numero nao perfeito')



def ex10():
    #primos em um intervalo, 
    inicio=int(input('inicio numero: '))
    fim=int(input('final numero: '))

    for numero_atual in range (inicio,fim+1):
        total_divisores=0

        for divisor in range (1,numero_atual+1):
            if numero_atual % divisor == 0:
                total_divisores  +=1

        if total_divisores  == 2:
            print(f'o numero {numero_atual} é primo')

ex10()