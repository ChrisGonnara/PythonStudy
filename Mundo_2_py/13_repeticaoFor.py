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
ex48()