import math
import random

# --- NOTAS DE ESTUDO (AULA 08) ---

def resumo_teoria():
    """Arredondamentos e Raiz Quadrada"""
    num = int(input('Digite um numero: '))
    raiz = math.sqrt(num)
    
    # floor: baixo | ceil: cima | trunc: corta a virgula
    print(f'A raiz de {num} e {raiz:.2f}')
    print(f'Arredondado para baixo: {math.floor(raiz)}')
    print(f'Arredondado para cima: {math.ceil(raiz)}')

# --- EXERCICIOS PRATICOS ---

def ex16():
    """Mostra a porcao inteira de um numero"""
    n1 = float(input('Digite un numero: '))
    inteiro = math.trunc(n1)
    print(f'O numero e {n1} e a sua parte inteira e {inteiro}')

def ex17():
    """Calculo da Hipotenusa"""
    co = float(input('Cateto oposto: '))
    ca = float(input('Cateto adjacente: '))
    hip = math.hypot(co, ca)
    print(f'A hipotenusa mede {hip:.2f}')

def ex18():
    """Seno, Cosseno e Tangente"""
    ang = float(input('Digite o angulo: '))
    rad = math.radians(ang) # O Python precisa converter para radiano
    
    print(f'Angulo {ang}:')
    print(f'Seno: {math.sin(rad):.2f}')
    print(f'Cosseno: {math.cos(rad):.2f}')
    print(f'Tangente: {math.tan(rad):.2f}')

def ex19():
    """Sorteia um nome da lista"""
    n1 = input('Nome 1: ')
    n2 = input('Nome 2: ')
    n3 = input('Nome 3: ')
    n4 = input('Nome 4: ')
    
    lista = [n1, n2, n3, n4]
    sorteado = random.choice(lista)
    print(f'O sorteado foi {sorteado}')

def ex20():
    """Embaralha a ordem da lista"""
    n1 = input('Nome 1: ')
    n2 = input('Nome 2: ')
    n3 = input('Nome 3: ')
    n4 = input('Nome 4: ')
    
    lista = [n1, n2, n3, n4]
    random.shuffle(lista) # Embaralha a lista original
    print(f'A ordem de apresentacao sera: {lista}')

# Para rodar, basta chamar a funcao aqui
ex20()