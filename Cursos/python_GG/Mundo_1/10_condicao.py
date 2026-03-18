# CURSO EM VÍDEO - AULA 10 (CONDIÇÕES)
# ==========================================

from random import randint
from time import sleep

# --- EXEMPLOS PRÁTICOS DA AULA ---

def teoria():
    # Verifica se o carro é novo ou velho baseado no tempo
    tempo = int(input('Quantos anos tem seu carro?\n'))
    if tempo <= 3:
        print('Carro novo')
    else:
        print('Carro velho')
    print('--FIM--')

def pratico():
    # Condição simples para verificar o nome
    nome = str(input('Qual seu nome? ')).strip()
    if nome == 'Christiano':
        print(f'Que nome lindo você tem!')
    else:
        print('Seu nome é tão normal!')
    print(f'Bom dia, {nome}!')

def pratico2():
    # Cálculo de média simples com if/else
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    m = (n1 + n2) / 2
    print(f'A sua media foi: {m:.1f}')
    if m >= 6.0:
        print('A sua media foi boa, PARABÉNS! ')
    else:
        print('A sua media foi ruim! ESTUDE MAIS!')

# --- EXERCÍCIOS 28 AO 35 ---

def ex28():
    # Jogo da Adivinhação: Computador pensa em um número
    comp = randint(0, 5)
    print('-=-' * 20)
    print('Pensando em 1 numero de 0 a 5. tente adivinhar...')
    print('-=-' * 20)
    
    jogador = int(input('Em que numero pensei? '))
    print('processando... ')
    sleep(1.5)

    if jogador == comp:
        print('Parabéns! voce conseguiu me vencer!')
    else:
        print(f'GANHEI! Eu pensei no numero {comp} e nao no {jogador}!')

def ex29():
    # Radar eletrônico: Cálculo de multa acima de 80km/h
    vel = float(input('Digite a velocidade que estava: '))
    if vel > 80:
        print(f'Multado! {vel}km/h')
        calculo = vel - 80
        multa = calculo * 7.00
        print(f'Valor da multa: R$ {multa:.2f}')
    else:
        print(f'Certo! {vel}km/h')

def ex30():
    # Verificador de Par ou Ímpar usando o resto da divisão (%)
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é impar')

def ex31():
    # Custo da Viagem: Tarifas diferentes por distância
    dis = float(input('Qual a distância em km da viagem: '))
    if dis <= 200:
        valor = 0.50 * dis
    else:
        valor = 0.45 * dis
    print(f'Valor da viagem de {dis}km foi: R$ {valor:.2f}')

def ex32():
    # Ano Bissexto: Verificação simples de divisibilidade por 4
    ano = int(input('Ano pra ver se é bissexto: '))
    if ano % 4 == 0:
        print(f'O ano {ano}, é bissexto')
    else:
        print(f'o ano {ano}, não é bissexto')

def ex33():
    # Maior e Menor valores: Lógica de comparação entre 3 números
    a = int(input('Digite o 1 numero: '))
    b = int(input('Digite o 2 numero: '))
    c = int(input('Digite o 3 numero: '))

    maior = a
    if b > a and b > c: maior = b
    if c > a and c > b: maior = c

    menor = a
    if b < a and b < c: menor = b
    if c < a and c < b: menor = c
    
    print(f'O menor valor: {menor}')
    print(f'O maior valor: {maior}')

def ex34():
    # Aumentos múltiplos: Reajuste salarial baseado na faixa
    sal = float(input('Salario: '))
    if sal <= 1250.00:
        novo = sal * 1.15
    else:
        novo = sal * 1.10
    print(f'Salario aumentado para: R$ {novo:.2f}')

def ex35():
    # Analisando Triângulo: Condição de existência de um triângulo
    a = float(input('lado 1: '))
    b = float(input('Lado 2: '))
    c = float(input('Lado 3: '))

    if a < b+c and b < a+c and c < a+b:
        print('Forma um triangulo')
    else:
        print('Não forma um triangulo')

# CHAMADA DA FUNÇÃO
ex35()