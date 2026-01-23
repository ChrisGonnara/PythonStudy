'''Condiçoes aninhadas''' #uma coisa dentro da outra, ninho
from datetime import date


def pratica():
    nome=str(input('Qual seu nome? '))
    if nome == 'Christiano':
        print('Que nome bonito!')
    elif nome =='Pedro' or nome == 'Maria' or nome=='Paulo':
        print('Seu nome é bem popular!') 
        
    elif nome in 'Ana Cláudia Jéssica Juliana':
        print('Belo nome feminino.')
    else:
        print('Seu nome é bem normal.')
    print(f'Tenha um bom dia, {nome}!')


def ex36():
    valor=float(input('Qual valor da casa? R$ '))
    sal=float(input('Qual salario do comprador? R$ '))
    anos=int(input('Em quantos anos vai pagar? '))
    meses= anos * 12
    prestacao= valor / meses
    limite30= sal*0.30
    print(f'Casa de R${valor:.2f} em {anos} anos')
    print(f'O seu limite de 30% é de R$ {limite30:.2f}')
    print(f'A prestacao sera de R$ {prestacao:.2f}')

    if prestacao<=limite30:
        print('empréstimo pode ser CONCEDIDO')
    else:
        print('emprestimo NEGADO!')

def ex37():
    n=int(input('Digite um numero: '))
    print('''Escolha uma das bases de conversão:
        [1] Converter para binário
        [2]Converter para octal
        [3]Converter para hexadecimal''')
    opcao=int(input('Sua opcao: '))
    if opcao == 1:
        print(f'{n} -> para binario = {bin(n)[2:]}')
    elif opcao ==2:
        print(f'{n} -> para octal= {oct(n)[2:]}')
    elif opcao ==3:
        print(f'{n} -> para hexadecimal = {hex(n)[2:]}')
    else:
        print(f'Opcao invalida.Tente novamente')
          
    
def ex38():
    n1=int(input('Digite o 1 numero: '))
    n2=int(input('Digite o 2 numero: '))

    if n1 > n2:
        print(f'O primeiro valor{n1} é maior que {n2}')
    elif n1 < n2:
        print(f'O Segundo valor {n2} é maior que {n1}')
    else:
        print(f'Nao existe valor maior, os 2 sao iguais, {n1}')

def ex39():
    atual=date.today().year

    nasc=int(input('Ano de nascimento: '))
    idade=atual-nasc
    if idade == 18:
        print('Voce tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo=18-idade
        print(f'Ainda faltam {saldo} anos para o alistamento')
        ano=atual+saldo
        print(f'Seu alistamento será em {ano}')
    else:
        saldo = idade -18
        saldo= idade-18
        print(f'Ja passou {saldo} anos do seu alistamento.')

def ex40():
    n1=float(input('NOTA 1: '))
    n2=float(input('NOTA 2: '))
    m=(n1+n2)/2
    if m <5.0:
        print(f'REPROVADO! {m}')
    elif m >=5.0 and m <=6.9:
        print(f'RECUPERAÇÃO! {m}')
    else:
        print(f'PARABÉNS! APROVADO! {m}')

def ex41():
    atual=date.today().year
    nasc=int(input('Ano de nascimento: '))
    idade=atual-nasc
    if idade <=9:
        print(f'{idade} anos, Categoria MIRIM')
    elif idade <=14:
        print(f'{idade} anos, Categoria INFANTIL')
    elif idade <=19:
        print(f'{idade} anos, Categoria JUNIOR')
    elif idade<=25:
        print(f'{idade} anos, categoria SENIOR')
    else:
        print(f'{idade} anos, Categoria MASTER')

def ex42():
    a=int(input('Lado A: '))
    b=int(input('Lado B: '))
    c=int(input('Lado C: '))

    if a < b+c and b < a+c and c <a+b:
        print('Forma um triangulo ', end='')
        if a == b == c: #LADOS IGUAIS
            print('EQUILÁTERO.')
        elif a!=b!=c!=a: #LADOS DIFERENTES
            print('ESCALENO.')    
        else: #2 LADOS IGUAIS, 1 DIFERENTE
            print('ISÓSCELES.')

def ex43():
    peso=float(input('Digite seu peso: '))
    altura=float(input('Digite sua altura: '))
    imc= peso / (altura ** 2) #altura ao quadrado

    if imc <=18.5:
        print(f'{imc:.1f}, ABAIXO DO PESO')
    elif imc <= 25:
        print(f'{imc:.1f}, PESO IDEAL')
    elif imc <= 30:
        print(f'{imc:.1f}, SOBREPESO')
    elif imc <= 40:
        print(f'{imc:.1f} OBESIDADE')
    else:
        print(f'{imc:.1f}OBESIDADE MÓRBIDA')
ex43()