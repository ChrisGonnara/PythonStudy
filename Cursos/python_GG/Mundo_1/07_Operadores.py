# --- FUNDAMENTOS: OPERACOES ARITMETICAS (AULA 07) ---

# Ordem de Precedencia:
# 1) () | 2) ** | 3) *, /, //, % | 4) +, -

def resumo_teoria():
    """Exemplos de operadores e precedencia"""
    # Exemplo 01: Operadores basicos com valores fixos
    n1, n2 = 5, 2
    print(f'Soma: {n1+n2} | Sub: {n1-n2} | Mult: {n1*n2}')
    print(f'Div: {n1/n2} | Pot: {n1**n2} | DivInt: {n1//n2} | Resto: {n1%n2}')

    # Exemplos de Precedencia (X, Y, Z)
    y = (5 + 3 * 2)
    x = 3 * 5 + 4 ** 2
    z = 3 * (5 + 4) ** 2
    print(f'\nPrecedencia: y={y}, x={x}, z={z}')

    # Testes de Raiz e Formatacao (Exemplo 02 e 03)
    raiz = 81**(1/2)
    print(f'\nRaiz de 81 = {raiz}')
    
    nome = "Python"
    # ^ centraliza | < esquerda | > direita
    print(f'Prazer em te conhecer {nome:=^20}!') 

def ex01_pratico():
    """Entrada de dados e formatacao de casas decimais"""
    n1 = int(input('Um valor: '))
    n2 = int(input('Outro valor: '))
    s, m, d = n1 + n2, n1 * n2, n1 / n2
    
    # end=' ' evita que o proximo print pule linha
    print(f'Soma: {s}, Divisao: {d:.3f}', end=' ')
    print(f'Div. Inteira: {n1//n2}, Potencia: {n1**n2}')

# --- EXERCICIOS ---

def ex05():
    """Antecessor e Sucessor"""
    n = int(input('Digite um numero: '))
    print(f'Analisando {n}: Antecessor {n-1} e Sucessor {n+1}')

def ex09():
    """Tabuada com alinhamento"""
    n = int(input('Digite um numero: '))
    print('-' * 15)
    # :2 serve para alinhar o 1 com o 10
    print(f'{n} x {1:2} = {n*1}')
    print(f'{n} x {10:2} = {n*10}')
    print('-' * 15)

def ex12():
    """Desconto de 5%"""
    p = float(input('Preco do produto: '))
    print(f'Preco: R${p:.2f} | Com 5% de desconto: R${p * 0.95:.2f}')

def ex13():
    """Aumento de 15%"""
    s = float(input('Salario atual: '))
    print(f'Antigo: R${s:.2f} | Com 15% de aumento: R${s * 1.15:.2f}')

def ex15():
    """Aluguel de Carros"""
    km = float(input('Km percorridos: '))
    dias = int(input('Dias alugados: '))
    total = (dias * 60) + (km * 0.15)
    print(f'Total a pagar: R${total:.2f}')

# Teste chamando a função desejada:
resumo_teoria()