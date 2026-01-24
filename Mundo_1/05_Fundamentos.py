# --- RESUMO TEORIA: FUNDAMENTOS ---

# O comando print() exibe dados na tela.
# O comando input() recebe dados do usuário (sempre como string por padrão).
# f-strings (f'{}') facilitam a exibição de variáveis dentro de frases.

def resumo_teoria():
    """Conceitos iniciais de saida e entrada"""
    print('Ola, Mundo!') # A forma mais simples de exibir texto
    
    nome = 'Christiano'
    print(f'Variavel nome contem: {nome}')

# --- EXERCICIOS PRATICOS ---

def ex01():
    """O classico Ola Mundo usando variavel"""
    msg = 'Olá, mundo!'
    print(msg)

def ex02():
    """Interacao com o usuario (Boas-vindas)"""
    nome = input('Digite seu nome: ')
    print(f'É um prazer te conhecer, {nome}!')

# Chamada para teste
ex02()