'''
 AULA 13: ESTRUTURAS DE REPETIÇÃO (FOR)
================================================================================
- range(i, f, p): Início, Fim (exclusivo) e Passo.
- Acumuladores/Contadores: soma += n | cont += 1.
- Slicing [[::-1]]: Inverte strings (Dica de Performance).
- Extremos: Usar 'if c == 1' para inicializar Maior/Menor.
================================================================================
'''

from time import sleep
from datetime import date

# --- EXEMPLOS DA AULA (TEORIA) ---

def exemplo01():
    print('\n--- EXEMPLO 01 ---')
    for c in range(1, 6, 2): # Início, Fim, Passo
        print(c)
    print('FIM\n')
    for c in range(4, 0, -1): # Contagem regressiva
        print(c)
    print('FIM')
exemplo01()

def exemplo02():
    print('\n--- EXEMPLO 02 ---')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    for c in range(i, f + 1, p):
        print(c)
    print('FIM')
exemplo02()

def exemplo03():
    print('\n--- EXEMPLO 03 ---')
    s = 0
    for c in range(0, 3):
        n = int(input('Digite um valor: '))
        s += n
    print(f'O somatório de todos valores = {s}')
exemplo03()

# --- EXERCÍCIOS RESOLVIDOS ---
# --- EXERCÍCIO 46: CONTAGEM REGRESSIVA ---
def ex46():
    print('\n--- EX 46: CONTAGEM REGRESSIVA ---')
    for s in range(5, -1, -1):
        print(f'{s}...')
        sleep(0.5)
    print('FIM DA CONTAGEM!')
ex46()

# --- EXERCÍCIO 47: NÚMEROS PARES ---
def ex47():
    print('\n--- EX 47: PARES DE 1 A 50 ---')
    for n in range(2, 51, 2):
        print(n, end=' ')
    print('\nACABOU!')
ex47()

# --- EXERCÍCIO 48: SOMA ÍMPARES MÚLTIPLOS DE 3 ---
def ex48():
    print('\n--- EX 48: SOMA ÍMPARES MÚLTIPLOS DE 3 ---')
    soma = 0
    cont = 0
    for n in range(3, 501, 3):
        if n % 2 != 0:
            soma += n
            cont += 1
    print(f'Soma dos {cont} valores: {soma}')
ex48()

# --- EXERCÍCIO 49: TABUADA V2.0 ---
def ex49():
    print('\n--- EX 49: TABUADA V2.0 ---')
    n = int(input('Tabuada do número: '))
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
ex49()

# --- EXERCÍCIO 50: SOMA DOS PARES ---
def ex50():
    print('\n--- EX 50: SOMA DOS PARES ---')
    soma = 0
    cont = 0
    for c in range(1, 7):
        num = int(input(f'Digite o {c}º valor: '))
        if num % 2 == 0:
            soma += num
            cont += 1
    print(f'Você digitou {cont} números PARES e a soma foi {soma}')
ex50()

# --- EXERCÍCIO 51: PROGRESSÃO ARITMÉTICA ---
def ex51():
    print('\n--- EX 51: PROGRESSÃO ARITMÉTICA ---')
    pi = int(input('1º termo: '))
    razao = int(input('Razão: '))
    total = int(input('Quantos termos? '))
    pf = pi + (total-1) * razao
    for c in range(pi, pf + razao, razao):
        print(f'{c}', end=' -> ')
    print('Acabou!')
ex51()

# --- EXERCÍCIO 52: NÚMEROS PRIMOS ---
def ex52():
    print('\n--- EX 52: NÚMEROS PRIMOS ---')
    num = int(input('Digite um número: '))
    tot_div = 0
    for c in range(1, num + 1):
        if num % c == 0:
            tot_div += 1
    print(f'O número {num} foi divisível {tot_div} vezes')
    if tot_div == 2:
        print('Ele É PRIMO!')
    else:
        print('Ele NÃO É PRIMO!')
ex52()

# --- EXERCÍCIO 53: DETECTOR DE PALÍNDROMO ---
def ex53():
    print('\n--- EX 53: DETECTOR DE PALÍNDROMO ---')
    frase = str(input('Digite uma frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    
    # FORMA (Slicing): Inverte a string inteira de uma vez
    inverso = junto[::-1]
        
    print(f'O inverso de {junto} é {inverso}')
    if inverso == junto:
        print('Temos um PALÍNDROMO!')
    else:
        print('Não é um palíndromo.')
ex53()

# --- EXERCÍCIO 54: GRUPO DA MAIORIDADE ---
def ex54():
    print('\n--- EX 54: GRUPO DA MAIORIDADE ---')
    atual = date.today().year
    maiores = 0
    menores = 0
    for c in range(1, 8):
        nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
        if atual - nasc >= 21:
            maiores += 1
        else:
            menores += 1
    print(f'Total: {maiores} maiores e {menores} menores.')
ex54()

# --- EXERCÍCIO 55: MAIOR E MENOR PESO ---
def ex55():
    print('\n--- EX 55: MAIOR E MENOR PESO ---')
    pesomaior = 0
    pesomenor = 0
    for c in range(1, 6):
        peso = float(input(f'Peso da {c}ª pessoa: '))
        if c == 1:
            pesomaior = peso
            pesomenor = peso
        else:
            if peso > pesomaior: pesomaior = peso
            if peso < pesomenor: pesomenor = peso
    print(f'Maior peso: {pesomaior}kg | Menor peso: {pesomenor}kg')
ex55()

# --- EXERCÍCIO 56: ANALISADOR COMPLETO ---
def ex56():
    print('\n--- EX 56: ANALISADOR COMPLETO ---')
    soma_idade = 0
    homem_velho_idade = 0
    homem_velho_nome = ''
    mulheres_novas = 0
    for c in range(1, 5):
        print(f'--- {c}ª PESSOA ---')
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        soma_idade += idade
        if sexo == 'M' and (c == 1 or idade > homem_velho_idade):
            homem_velho_idade = idade
            homem_velho_nome = nome
        if sexo == 'F' and idade < 20:
            mulheres_novas += 1
    print(f'\nMédia de idade: {soma_idade/4} anos.')
    print(f'Homem mais velho: {homem_velho_nome} ({homem_velho_idade} anos).')
    print(f'Mulheres < 20 anos: {mulheres_novas}.')

#CHAMADA DE FUNÇÃO
ex56()