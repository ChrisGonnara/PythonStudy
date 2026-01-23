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

ex36()