def teoria():
    tempo = int(input('Quantos anos tem seu carro?\n'))
    #print('Carro novo' if tempo<=3 else 'Carro velho')
    if tempo<=3:
        print('Carro novo')
    else:
        print('Carro velho')
    print('--FIM--')

def pratico():
    nome=str(input('Qual seu nome? '))
    if nome == 'Christiano':
        print(f'Que nome lindo você tem!')
    else:
        print('Seu nome é tão normal!')
    print(f'Bom dia, {nome}!')

def pratico2():
    n1=float(input('Digite a primeira nota: '))
    n2=float(input('Digite a segunda nota: '))
    m=(n1+n2)/2
    print(f'A sua media foi: {m:.1f}')
    if m>=6.0:
        print('A sua media foi boa, PARABÉNS! ')
    else:
        print('A sua media foi ruim! ESTUDE MAIS!')

def ex28():
    import random 
    lista= [0,1,2,3,4,5]
    pensado= random.choice(lista)
    n=int(input('tente 1 numero de 0 a 5: '))
    if n == pensado:
        print(f'Venceu!, acertou o numero {n}!')
    else:
        print(f'ERROU! tentativa: {n}, era: {pensado}')

def ex29():
    vel=int(input('Digite a velocidade que estava: '))
    if vel > 80:
        print(f'Multado! {vel}km/h')
        calculo=vel-80
        multa = calculo *7.00
        print(f'Valor da multa: R$ {multa:.2f}')
    else:
        print(f'Certo! {vel}km/h')

def ex30():
    n=int(input('Digite um número: '))
    if n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é impar')

def ex31():
    dis=int(input('Qual a distância em km da viagem: '))
    if dis <=200:
        valor=0.50*dis
    else:
        valor=0.45*dis
    print(f'Valor da viagem de {dis}km foi: {valor}')

def ex32():
    ano=int(input('Ano pra ver se é bissexto: '))
    if ano % 4 == 0:
        print(f'O ano {ano}, é bissexto')
    else:
        print(f'o ano {ano}, não é bissexto')

def ex33():
    a=int(input('Digite o 1 numero: '))
    b=int(input('Digite o 2 numero: '))
    c=int(input('Digite o 3 numero: '))

    maior=a
    if b>a and b>c:
        maior=b
    if c>a and c>b:
        maior=c

    menor=a
    if b<a and b<c:
        menor=b
    if c<a and c<b:
        menor=c
    
    print(f'O menor valor: {menor}')
    print(f'O maior valor: {maior}')

def ex34():
    sal=float(input('Salario: '))
    if sal <= 1250.00:
        novo= sal*1.15
    else:
        novo=sal*1.10
    print(f'salario aumentado pra: {novo:.2f}')

def ex35():
    a=int(input('lado 1: '))
    b=int(input('Lado 2: '))
    c=int(input('Lado 3: '))

    if a < b+c and b < a+c and c < a+b:
        print('Forma um triangulo')
    else:
        print('não forma um triangulo')
ex35()