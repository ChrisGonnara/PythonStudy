# 1 a 10
def ex01():
    i=1
    while i <=10:
        print(i)
        i+=1

#10 a 1
def ex02():
    i=10
    while i >=1:
        print(i)
        i-=1

#soma de 1 ate n
def ex03():
    n=int(input('numero: '))
    i=1
    soma=0
    while i <=n:
        soma+=i
        i+=1
    print(f' soma de 1 ate {n} = {soma}')

# tabuada de um numero
def ex04():
    n=int(input('numeroo: '))
    i=1
    while i<=10:
        print(f'{n} X {i} = {n * i}')
        i+=1


#media 5 notas
def ex05():
    soma = 0
    i=1
    
    while i <=5:
        nota=float(input(f'{i} nota:'))
        soma+=nota
        i+=1
    
    media = soma/5
    print(f'media das 5 notas: {media:.2f}')


#contador pares e impar
def ex06():
    i=1
    n=''
    par = 0
    impar = 0

    while i <=10:
        n=int(input(f'{i} numero: '))

        if n % 2 == 0:
            par +=1
        else:
            impar +=1
        i+=1

    print(f'{par} pares')
    print(f'{impar} impares')
          

#menor e maior valor informado  | ler 8 inteiros
def ex07():
    n=int(input('1 numero: '))
    maior=n
    menor=n
    i=2

    while i <=8:
        n=int(input(f'{i} numero: '))

        if n > maior:
            maior = n
        if n < menor:
            menor = n
        i+=1

    print(f'maior: {maior}')
    print(f'menor {menor}')


#soma ate valor de parada
def ex08():
    n=''
    soma=0
    while n != 0:
        n=int(input('numero: '))
        soma +=n
    print(f'Soma: {soma}')


def ex09():
    valor=''
    i=0
    soma=0

    while valor !=0:
        valor=float(input('Valor da venda: '))
        soma +=valor
        i +=1
    media = soma / i

    print(f'Valor vendido no dia: {soma}')
    print(f'numero vendas: {i}')
    print(f'valor medio: {media:.2f}')


def ex10():
    temperatura = int(input('Temperatura: '))

    if temperatura == -1:
        print('nenhuma temperatura registrtada.')
        return

    i=1  #qtd temperaturas
    j=0 #qtd acima de 80
    maior = temperatura
    menor = temperatura
    soma = 0
    media=0

    while temperatura != -1:
        i+=1
        soma += temperatura

        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura

        if temperatura > 80:
            j+=1

        temperatura =float(input(' [-1 sair] Temperatura: '))


    media = soma / i

    print(f'temperaturas registradas : {i}')
    print(f'menor : {menor}')
    print(f'maior: {maior}')
    print (f'media: {media}')
    print(f'acima de 80: {j}')



#tabuada 1 a 9 

def ex11():
    for i in range (1,11):
        print(f'Tabuada do {i}')

        for j in range (1,10):
            print(f'{i} x {j} = {i * j}')
        print('-'*10)


#retangulo de simbolos
def ex12():
    linhas=int(input('linhas: '))
    colunas=int(input('colunas'))

    for l in range (linhas):
        print ('*' * colunas)


def ex13():
    #triangulo de numeros
    n=int(input('numero: '))

    for l in range (1,n+1):
        linha=''

        for c in range (1,l+1):
           linha += str(c)

        print (linha)

ex04()