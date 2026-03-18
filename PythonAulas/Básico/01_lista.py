#entradas
#calculo
#saida

def ex01():
    peso = float (input('Digite seu peso: '))
    altura = float (input("Digite sua altura: "))
    imc = peso / (altura * altura)
    print(f'{imc:.2f}')

def ex02():
    n1=float(input('nota1: '))
    n2=float(input('nota2: '))
    n3=float(input('nota 3: '))
    m= (n1+n2+n3)/3
    print(f'media = {m}')

def ex03():
    b=float('base do triangulo: ')
    al=float('altura do triangulo: ')
    area= b*al
    print(f'area = {area}')

def ex04():
    bas=float('base do triangulo: ')
    alt=float('altura do triangulo: ')
    area= (bas*alt)/2
    print(f'area = {area}')

def ex05():
    comp=float(input('comprimento: '))
    larg=float(input('Largura: '))
    alt=float(input('altura: '))
    vol= comp * larg * alt
    print(f'Volume = {vol}')

def ex06():
    cel=float(input('Celsius: '))
    fah= (cel * 1.8) + 32
    print(f'celsius = {cel:.2f}, Fahreinheit= {fah:.2f}')

def ex07():
    saa= float (input('salario atual: '))
    aum= float(input('aumento porcentagem: '))
    novo= saa * (1 + aum/100)
    print(f'novo salario = {novo:.2f}')

def ex08():
    vap= float(input('Valor produto: '))
    des= float(input('percentual desconto: '))
    final= vap * (1 - des/100)
    print(f'Valor com desconto = {final}')

def ex09():
    dis=float (input('Distancia: '))
    gas=float (input('litros gasto: '))
    cons= dis/gas
    print(f'consumo medio = {cons}')

def ex10():
    hora= float(input('horas: '))
    minut = hora * 60
    segun = minut * 60
    print(f'Horas em minutos: {minut:.0f}')
    print(f'Minutos em segundos: {segun:.0f}')

def ex11():
    cap=float(input('capital: '))
    jur=float(input('taxa de juros: ')) / 100
    tempo=float(input('Tempo: '))
    valfin= cap * (1 + jur * tempo)

    print(f'valor final = {valfin}')
ex11()