'''Condiçoes aninhadas''' #uma coisa dentro da outra, ninho
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

ex38()