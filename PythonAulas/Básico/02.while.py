def ex01():
    idade = 18
    if idade >=18:
        print('Maior de idade')

def ex02():
    idioma='pt'
    if idioma =='pt':
        print('Iidioma portugues')
    else:
        print('idioma ingles')

def ex03():
    idioma = input('Escolha o programa pt/en: ')
    if idioma =='pt':
        print('Idioma configurado para portugues.')
    else:
        print('Idioma confugrado para ingles')

#tc abc> errada #tc2 123 > errada   tc3 '' > errada
#tc4 Python123 > errada     #tc5 python123 > liberada
def ex04():
    senha= str(input('senha: '))
    if senha == 'python123':
        print('Acesso liberado')
    else:
        print('Senha incorreta')

def ex05():
    numero=int(input('Digite um numero positivo: '))
    while numero <0:
        print('Valor negativo')
        numero = int(input('Digite um numero positivo: '))
    print(f'o numero digitado é {numero}')


def ex06():
    #tc1 abc > erro,  TC2 123 > ERRO,  TC3 PYTHON123 > ERRO, python123 > libera
    senha=str(input('SENHA: '))
    while senha != 'python123':
        print('Senha invalida')
        senha=str(input('Senha: '))
    print('Acesso liberado')

def ex07():
    senha=''
    while senha != 'python123':
        senha=str(input('Senha: '))
    print('Acesso liberado')

def ex08():
    senha=''
    contador=0

    while senha !='python123' and contador < 3:
        senha=str(input('Senha: '))
        contador += 1

    if senha == 'python123':
        print ('Acesso liberado')
    else:
        print('Senha invalida')

def ex09():
    i=0
    while i<10:
        print (i)
        i=i+1 

def ex10():
    senha= str(input('senha: '))

    while senha != 'python123' and senha !='fim':
        print('Senha incorreta')
        senha = str(input('senha: '))



ex09()