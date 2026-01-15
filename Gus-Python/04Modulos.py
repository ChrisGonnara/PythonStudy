def exemplo01():
    from math import sqrt, floor
    #floor arredondar pra baixo
    #ceil arredondar pra cima
    num = int(input('Digite um numero: '))
    raiz = sqrt(num)
    print(f'raiz de {num} = {floor(raiz):.2f}')

def exemplo02():
    import random
    num = random.randint(1,10)
    print (num)


def ex16():
    import math
    #leia um numero real qualquer
    #mostre a sua porcao inteira
    n1=float(input('Digite um numero: '))
    int= math.trunc(n1)
    print(f'numero: {n1}, parte inteira: {int}')

def ex17():
    #leia comp cat opost e cat adj de um tring retang
    #calcule e mostre o comprimento da hipotenusa
    import math
    co=float(input('Cateto oposto: '))
    ca=float(input('Cateto adjascente: '))
    #hi=(co**2 + ca ** 2) ** (1/2)
    hip=math.hypot(co, ca)
    print(f'a hip de catop:{co} e catad{ca} = {hip:.2f}')

def ex18():
    import math
    ang=float(input('Digite o angulo que deseja: '))
    rad= math.radians(ang)

    seno=math.sin(rad)
    print(f'angulo = {ang}, sen = {seno:.2f}')
    
    coss=math.cos(rad)
    print(f'angulo = {ang}, coss = {coss:.2f}')
    tan = math.tan(rad)
    print(f'angulo = {ang}, tang = {tan:.2f}')

def ex19():
    #quer sortear 1 dos 4
    #leia os nomes, escreva nome escolhido
    from random import choice
    n1=input('Digite o 1 nome:')
    n2=input('Digite o 2 nome:')
    n3=input('Digite o 3 nome:')
    n4= input('Digite o 4 nome:')

    lista=[n1,n2,n3,n4] #matriz
    sort= choice(lista) #sorteia 1 da lista
    print(f'o sorteado foi {sort}')

def ex20():
    #ordem apresentacao, 4 nomes e sorteia ordem
    from random import shuffle
    n1=input('Digite o 1 nome: ')
    n2=input('Digite o 2 nome: ')
    n3=input('Digite o 3 nome: ')
    n4=input('Digite o 4 nome: ')

    lista=[n1,n2,n3,n4]
    shuffle(lista) #embaralha
    print('A ordem de apresentacao sera: ')
    print(lista)

ex20()