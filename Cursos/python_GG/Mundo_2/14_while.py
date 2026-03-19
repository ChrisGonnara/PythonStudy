def ex01():
    for c in range (1,10):
        print(c)

    c = 1
    while c <10:
        print(c)
        c +=1

def ex02():
    for c in range (1,3):
        n=int(input('valor: '))
    print(f'Fim')



    r='S'
    while r =='S':
        n=int(input('valor: '))
        r=str(input('Quuer continuar? [S/N]')).upper()
    print('Fim')


def ex03():
    n=1
    par = impar = 0
    while n!=0:
        n=int(input('Valor: '))
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    print(f'Voce digitou {impar} impar e {par} par')
    print('Acabou')
ex03()