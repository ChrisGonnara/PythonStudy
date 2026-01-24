from time import sleep
def exemplo01():
    for c in range(1,6, 2): #0 a 7 de 2 em 2
        print(c)
    print('FIM\n')

    for c in range(4,0,-1): #contar pra tras -1
        print(c)
    print('Fim')

def exemplo02():
    i=int(input('Inicio: '))
    f=int(input('Fim: '))
    p=int(input('Passo: '))
    for c in range(i,f+1,p):
        print(c)
    print('Fim')

def exemplo03():
    s=0
    for c in range(0,3):
        n=int(input('Digite um valor: '))
        s += n
    print(f'O somatório de todos valore = {s}')



def ex46():
    print('Contagem regressiva: ')
    for s in range (5,-1,-1):
        print(f'{s}...'), sleep(0.5)
    print('POOW! BUUM!')

def ex47():
    for n in range (2,51,2):
            print(n, end=' ')
    print('\nacabou!')

def ex48():
    soma=0
    cont=0
    for n in range (3,501,3):
        if n % 2 != 0:
            soma += n
            cont += 1

    print('os numeros impar de 1 a 500, mult de 3')
    print(f'Soma desses {cont} numeros = {soma}')

def ex49():
    n=int(input('Digite um numero pra tabuada: '))
    for c in range (1,11):
        print(f'{n} x {c:2} = {n*c}')

def ex50():
    soma=0
    cont = 0
    for c in range (1,7):
        n=int(input(f'Digite o {c} numero: '))
        if n % 2 == 0:
            soma += n
            cont +=1
    print(f'teve {cont} PARES')
    print(f'e a soma foi {soma}')

def ex51():
    pi=int(input('1 termo: '))
    razao=int(input('Razão: '))
    total=int(input('Quantos termos voce quer? '))

    pf = pi + (total-1) * razao

    for c in range (pi,pf+razao,razao):
        print(f'{c}', end= ' -> ')

    print('Acabou!')

def ex52():
    num=int(input('Digite um numero: '))
    cont=0
    for c in range (1,num+1):
        num % c == 0
        cont+=1
    print(f'O {num} foi disivel {cont} vezes')
    if cont == 2:
        print(f'{num}, é primo')
    else:
        print(f'Não é primo')

def ex53():
    frase=str(input('Digite uma frase: ')).strip().upper()
    palavras=frase.split()
    junto= ''.join(palavras)
    # Ele inicializa a variável vazia para receber as letras
    inverso=''
    
    # O FOR invertido: começa na última letra,
    # vai até a primeira, voltando de 1 em 1
    for letra in range (len(junto)-1,-1,-1):
        inverso+=junto[letra]

    print(f'O inverso de {junto} é {inverso}')
    if inverso == junto:
        print('Temos um PALÍNDROMO!')
    else:
        print('A frase digitada não é um palíndromo')
ex53()