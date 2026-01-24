# --- RESUMO TEORIA: TIPOS PRIMITIVOS ---

# int:   7, -4, 0 (Numeros inteiros)
# float: 4.5, 7.0, -15.2 (Numeros com virgula/ponto)
# bool:  True, False (Valores logicos)
# str:   'Ola', '7.5', ' ' (Texto entre aspas)

def resumo_teoria():
    """Exemplos de entrada e tipos de dados"""
    # Exemplo 01 e 02: Soma basica
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro: '))
    s = n1 + n2
    print(f'A soma entre {n1} e {n2} vale {s}')
    
    # Exemplo 03: Verificando tipos e metodos is...
    valor = input('Digite algo para teste: ')
    print(f'Tipo primitivo: {type(valor)}')
    print(f'E numerico? {valor.isnumeric()}')
    print(f'E alfabetico? {valor.isalpha()}')
    print(f'E maiusculo? {valor.isupper()}')

# --- EXERCICIOS PRATICOS ---

def ex03():
    """Leia 2 numeros e mostre a soma"""
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print(f'A soma de {n1} + {n2} = {n1 + n2}')

def ex04():
    """Leia algo e mostre seu tipo e informacoes (Dissecando a variavel)"""
    a = input('Digite algo: ')
    
    print(f'O tipo primitivo e: {type(a)}')
    print(f'So tem espaco? {a.isspace()}')
    print(f'E um numero? {a.isnumeric()}')
    print(f'E alfabetico? {a.isalpha()}')
    print(f'E alfanumerico? {a.isalnum()}')
    print(f'Esta em maiusculas? {a.isupper()}')
    print(f'Esta em minusculas? {a.islower()}')
    print(f'Esta capitalizada (Title)? {a.istitle()}')

# Chamada para teste
ex04()

