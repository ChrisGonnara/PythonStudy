#operaçoes aritmeticas

# Adiçao(+)   Subtração(-)
#Multipl(*)   Potencia(**)
#Divisão(/)   Divisao inteira(//)
#RestoDiv(%)

#ordem de precedencia 
#1) () 
#2) ** 
#3) *, /, //, %,
#4) +, -,


def ex01():
    n1 = int(5);     n2 = int(2)

    soma = n1+n2;    sub = n1-n2
    mult = n1 * n2;  div = n1 / n2
    pot = n1 ** n2;  divint = n1 //n2
    rest = n1 % n2

    print(f' soma:{soma}\n sub:{sub}\n mult:{mult}') 
    print(f' div:{div}\n pot:{pot}\n divint:{divint}')
    print(f' resto:{rest}\n')

 #exemplos de precedencia
    y = (5+3*2)
    print(f'exemplo precedencia: {y}')
    x = 3 * 5 + 4 ** 2
    print(f'exemplo precedencia: {x}')
    z = 3*(5+4) ** 2
    print(f'exemplo precedencia {z}')



def teste02():
    raiz= 81**(1/2)
    print(f'raiz de 81 = {raiz}')
    print('='* 20)

def teste03():
    #nome= input('Digite o nome: ')
    #print (f'Prazer em te conhecer {nome:=^12}!') 
    # escrever em ate x espaco(12) :12 e 
    # ^ centraliza < 12 a esquerda > 12 a direita

    n1= int(input('Um valor: '))
    n2= int(input('outro valor: '))
    s = n1+n2;    m= n1 * n2
    d= n1 / n2;   di = n1 //n2
    e = n1 ** n2
    print (f'soma = {s}, divisao = {d:.3f}, ', end =' ')
    print (f'div int = {di}, potencia = {e}')



def ex05():
    #leia um int e mostre sucessor e antecessor
    n1= int(input('Digite um numero: '))
    print(f'antecessor de {n1} = {n1 - 1}')
    print(f'Sucessor de {n1} = {n1+1}')

def ex06():
    #leia um numero e mostre seu 2x, 3x, e raiz qd
    n1= int (input('Digite um numero: '))
    print(f'dobro de {n1} = {n1 * 2}')
    print(f'triplo de {n1}={n1*3}')
    print(f'Raiz de {n1} = {n1 ** 0.5:.3f}') # 3 num depois da,

def ex07():
    #leia 2 notas de um aluno e mostre sua media
    n1= float(input('Digite a 1 nota:'))
    n2= float (input('Digite a 2 nota: '))
    media = (n1+n2)/2
    print(f'As notas foram {n1} , {n2}')
    print(f'A media das notas = {media:.1f}')

def ex08():
    #leia um valor em metros e converta em cm e mm
    m=float(input('Digite quantos metros: '))
    cm= m*100
    mm= m*1000
    print(f'metros:{m}m corrresponde a{cm}cm, {mm}mm')

def ex09():
    #leia um int e mostre sua tabuada
    n=int(input('Digite um numero: '))
    print(f'-'*15)
    print(f'{n} x {1:2} = {n*1}')
    print(f'{n} x {2:2} = {n*2}')
    print(f'{n} x {2:2} = {n*3}')
    print(f'{n} x {4:2} = {n*4}')
    print(f'{n} x {5:2} = {n*5}')
    print(f'{n} x {6:2} = {n*6}')
    print(f'{n} x {7:2} = {n*7}')
    print(f'{n} x {8:2} = {n*8}')
    print(f'{n} x {9:2} = {n*9}')
    print(f'{n} x {10:2} = {n*10}')
    print(f'-'*15)

def ex10():
    #leia quaanto tem na carteira e
    #mostre quantos dolar ela pode comprar
    #considere 1 dolar = rs 5.37

    r=float(input('Quantos reais na carteira?: '))
    d = r / 5.37
    print(f'{r:.2f} reais = {d:.2f} dolar')

def ex11():
    #leia a largura e a altura de uma parede (metros)
    #calcule sua area e a quantidade de tinta
    #cada litro de tinta pinta uma area 2m²
    #area = base * altura

    l=float(input('Qual a largura da parede?'))
    a=float(input('Qual a altura da parede?'))
    area= l*a
    tinta = area / 2

    print (f'Parede {l}X{a} = area de {area}m²')
    print(f'para a parede, voce precisa de {tinta:.1f}l de tinta')

def ex12():
    #ler preço de um produto, mostre preço com 5% de desconto

    p=float(input('Qual preço do produto?'))
    pn=p * 0.95
    print(f' preco = {p:.2f} reais\n com desconto vai pra {pn:.2f} reais')

def ex13():
    #leia salario, e mostre o novo com 15% de aumento
    s=float(input('Salario?'))
    sn=s * 1.15
    print(f'Salario antigo = {s:.2f}\n Salario novo= {s*1.15:.2f}')

def ex14():
    #converter temperatura de celsius para f
    c=float(input ('qual a temperatura em celsius?'))
    f=(c*1.8+32)

    print(f'A temperatura de {c}celsius = {f} em fahrenheint')


def ex15():
    #perguinte qtd de km carro alugado, qtd dias alugado
    #calcule o preco a pagar, sabendo que o dia 60 reais, e 0.15cents por km rodado

    km=float(input('Quantos km percorreu:'))
    dias=int(input('quantos dias alugados?'))
    diapago=dias* 60
    kmpago=km* 0.15
    ptotal= kmpago+diapago
    print(f'custo aluguel = R${diapago} custo km total = R${kmpago}')
    print(f'Total pago= {ptotal}')

ex15()