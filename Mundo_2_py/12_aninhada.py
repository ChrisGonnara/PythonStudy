'''
CONDIÇÕES ANINHADAS (MUNDO 2)
=============================
RESUMO DA AULA: 
- Estrutura: if (se), elif (senão se), else (senão).
- Lógica: Escada de decisões onde apenas um bloco é executado.
- Ferramentas: Operadores lógicos (and, or, in), Formatação (:.2f),
  Bibliotecas (datetime para o ano atual, random para sorteios).
- Engenharia: Foco em evitar repetição (DRY) e validar entradas do usuário.
'''

from datetime import date
from random import randint
from time import sleep

# TEORIA EXEMPLO: PRÁTICA DE NOMES
def pratica():
    nome = str(input('Qual seu nome? ')).strip()
    
    if nome == 'Christiano':
        print('Que nome bonito!')
    elif nome in 'Pedro Maria Paulo':
        print('Seu nome é bem popular!') 
    elif nome in 'Ana Cláudia Jéssica Juliana':
        print('Belo nome feminino.')
    else:
        print('Seu nome é bem normal.')
    print(f'Tenha um bom dia, {nome}!')



# EXERCÍCIO 36: APROVANDO EMPRÉSTIMO
def ex36():
    valor = float(input('Valor da casa: R$ '))
    sal = float(input('Salário: R$ '))
    anos = int(input('Anos para pagar: '))
    
    meses = anos * 12
    prestacao = valor / meses
    limite = sal * 0.30
    
    print(f'Prestação: R${prestacao:.2f} | Limite: R${limite:.2f}')
    if prestacao <= limite:
        print('\033[32mAPROVADO\033[m')
    else:
        print('\033[31mNEGADO\033[m')

# EXERCÍCIO 37: CONVERSOR DE BASES
def ex37():
    n = int(input('Número inteiro: '))
    print('[1] Binário\n[2] Octal\n[3] Hexadecimal')
    opcao = int(input('Sua opção: '))
    
    if opcao == 1:
        print(f'Binário: {bin(n)[2:]}')
    elif opcao == 2:
        print(f'Octal: {oct(n)[2:]}')
    elif opcao == 3:
        print(f'Hexadecimal: {hex(n)[2:]}')
    else:
        print('Opção inválida!')

# EXERCÍCIO 40: MÉDIA DO ALUNO
def ex40():
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    
    print(f'Média: {m:.1f}')
    if m < 5.0:
        print('REPROVADO')
    elif 5.0 <= m < 7.0:
        print('RECUPERAÇÃO')
    else:
        print('APROVADO')

# EXERCÍCIO 43: CALCULADORA DE IMC
def ex43():
    peso = float(input('Peso (kg): '))
    altura = float(input('Altura (m): '))
    imc = peso / (altura ** 2)
    
    print(f'IMC: {imc:.1f} -> ', end='')
    if imc < 18.5:
        print('Abaixo do Peso')
    elif imc < 25:
        print('Peso Ideal')
    elif imc < 30:
        print('Sobrepeso')
    elif imc < 40:
        print('Obesidade')
    else:
        print('Obesidade Mórbida')

# EXERCÍCIO 44: PAGAMENTOS
def ex44():
    preco = float(input('Preço: R$'))
    print('[1] À vista\n[2] Cartão\n[3] 2x Cartão\n[4] 3x+ Cartão')
    op = int(input('Opção: '))
    
    if op == 1:
        pago = preco * 0.9
    elif op == 2:
        pago = preco * 0.95
    elif op == 3:
        pago = preco
        print(f'2x de R${pago/2:.2f}')
    elif op == 4:
        pago = preco * 1.2
        parc = int(input('Parcelas? '))
        print(f'{parc}x de R${pago/parc:.2f}')
    else:
        pago = preco
        print('Opção inválida!')
    print(f'Total: R${pago:.2f}')

# EXERCÍCIO 45: JOKENPÔ
def ex45():
    itens = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    
    print('[0] Pedra\n[1] Papel\n[2] Tesoura')
    user = int(input('Sua jogada: '))
    
    if user not in (0, 1, 2):
        print('Inválido!')
        return
    
    print('JO...'), sleep(0.5)
    print('KEN...'), sleep(0.5)
    print('PÔ!!!')
    
    print(f'PC: {itens[pc]} | VOCÊ: {itens[user]}')
    if pc == user:
        res = 'EMPATE'
    elif (user == 0 and pc == 2) or (user == 1 and pc == 0) or (user == 2 and pc == 1):
        res = 'VOCÊ VENCEU'
    else:
        res = 'PC VENCEU'
    print(res)

#CHAMADA DE FUNÇÃO
ex45()