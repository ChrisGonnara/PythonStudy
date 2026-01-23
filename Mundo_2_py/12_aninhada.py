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
    print(f' O IMC da pessoa é {imc:.1f}')

    if imc <=18.5:
        print(', ABAIXO DO PESO')
    elif imc <= 25:
        print(', PESO IDEAL')
    elif imc <= 30:
        print(', SOBREPESO')
    elif imc <= 40:
        print(' OBESIDADE')
    else:
        print('OBESIDADE MÓRBIDA')

def ex44():
    preco=float(input('preço do produto: '))
    print('''FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')
    tipo=int(input('Escolha como vai pagar: '))
    if tipo == 1:
        pago = preco * 0.90
    elif tipo == 2:
        pago = preco * 0.95
    elif tipo == 3:
        pago = preco
        parcela= pago /2
        print(f'parcelada em 2x de R${parcela:.2f} SEM JUROS')
    elif tipo == 4:
        pago= preco *1.2
        totparc=int(input('Quantas parcelas? '))
        parcela = pago / totparc
        print(f'parcelado em {totparc}x de R${parcela:.2f} COM JUROS')

    else:
        pago=preco
        print('opcao invalida,tente novamente!')
    print(f'Sua compra de R${preco} vai custar {pago:.2f} no final')



def ex45():
    from random import randint
    from time import sleep

    itens = ('Pedra', 'Papel', 'Tesoura')
    pc=randint(0,2)

    print('[0] Pedra\n[1] Papel\n[2] Tesoura')
    jogador = int(input('Sua jogada: '))

    if jogador not in (0, 1, 2):
        print('JOGADA INVÁLIDA!')
        return # Para a função aqui mesmo

    print('JO... KEN... PÔ!')
    sleep(1)

    print('-='*11)
    print(f'Computador jogou {itens[pc]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-='*11)

    if pc == jogador:
        res='EMPATE'
    elif ((jogador == 0 and pc == 2) or
        (jogador == 1 and pc == 0) or
        (jogador == 2 and pc == 1)):
        res='VOCE VENCEU!'
    else:
        res='Computador venceu!'

    print(f'Resultado: {res}\n')

        
ex45()