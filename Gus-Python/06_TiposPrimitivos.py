#aula variaveis simples

#int 7, -4, 0, 9875
#float 4.5, 0.076, -15.223, 7.0
#bool True, False
#str 'Olá', '7.5', ' ' tudo dentro aspas

def exemplo01():
    n1 =int (input ('digite um numero:  '))
    n2= int ( input ('Digite mais um numero: '))
    s= n1 + n2
    print (f'A soma vale {s}' )

def exemplo02():
    n1= int (input ('Digite um valor: '))
    n2= int (input ('Digite outro: ')) 
    s=n1+n2

    #print('A soma entre', n1, 'e', n2,'vale',s)
    print((f'A soma entre {n1} e {n2} vale {s}'))


def exemplo03():
    n=float(input('Digite um valor: '))
    s=str(input('Digite um valor: '))
    t=bool(input('Digite um valor: '))
    print(n)
    print(type(s))
    print(t)
    print (n.isnumeric()) #se é numero
    print (n.isalpha()) #se é letra
    print(n.isalnum()) #alfa numerico
    print(n.isupper()) #se so tem maisucula



#leia 2 numeros e mostre a soma
#somando 2 numeros
def desafio03():
    n1=int (input ('Digite um valor: '))
    n2=int (input ('Digite outro valor: '))
    s= n1+n2

    print(f'A soma de {n1} + {n2} = {s}')



#Leia algo e mostre seu tipo e informacoes
#dissecando uma variavel
def desafio04():
    a1= input('Digite algo: ')
    print('O tipo primitivo é: ',type(a1))
    print('Só tem numero?', a1.isnumeric())
    print('só tem letras?', a1.isalpha())
    print('Letras e numeros?', a1.isalnum())
    print('só espaço?', a1.isspace())
    print('Esta em minusculo?', a1.islower())
    print('esta em maiusculo?', a1.isupper())
    print('Esta capitalizada?', a1.istitle()) #primeira letra maiuscula?

desafio04()


