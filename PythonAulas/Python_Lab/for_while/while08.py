def ex01():
    #fatorial
    n=int(input('numero: '))
    i=1
    fat=1

    while i <=n:
        fat  *= i
        i+=1
    print(fat)


def ex02():
    n=int(input('qtd de termos: '))
    t1=0
    t2=1

    i=0

    while i < n:
        print(t1)
        proximo = t1+t2
        t1=t2
        t2=proximo

        i+=1


def ex03():
    soma=0
    n= int(input('Digite um numero: '))

    while n != 0:
        soma+=n
        n=int(input('Digite um numero: '))

    print(f'soma dos valores {soma}')
    

def ex04():
    #soma apenas dos pares
    soma =0
    n=int(input('Digite um numero: '))

    while n !=0:
        if n % 2 == 0:
            soma +=n
        n=int(input('Digite um numero: '))

    print(f'soma dos numeros pares: {soma} ')


def ex05():
    #quantidade pares,impar, positivo e negativo
    impar=0
    par=0
    positivo=0
    negativo=0

    n=int(input('Digite um numero: '))

    while n !=0:
        if n % 2 == 0:
            par +=1
        else:
            impar +=1

        if n >0:
            positivo +=1
        elif n <0:
            negativo +=1

        n=int(input('Digite um numero '))
            
    print(f'pares: {par}\t | impares: {impar}\t')
    print(f'positivos: {positivo}\t | negativos: {negativo}\t')


def ex06():
    media=0
    soma=0
    i=0

    n=int(input('Digite um numero: '))

    while n !=0:
        i+=1
        soma+=n

        n=int(input('Digite um numero: '))
    
    if i > 0:
        media = float (soma / i)
        print (f'media: {media:.1f}')
    else:
        print('nenhum valor valido informado')


def ex07():
    #maior e menor numero digitado
    n=int(input('numero: '))
    maior = n
    menor = n
    entrada = False

    while n != 0:
        entrada= True

        if n > maior:
            maior=n
        if n < menor:
            menor=n

        n=int(input('numero: '))

    if entrada == True:
        print(f"maior numero: {maior}")
        print(f'menor numero: {menor}')
    else:
        print('nenhum valor informado')


def ex08():
    n=float(input('Digite um numero: '))
    otimo=0
    bom=0
    regular=0
    ruim=0
    i=0

    while n >=0:
        i=1

        if n <5:
            ruim+=1
        elif n<7:
            regular+=1
        elif n<8:
            bom+=1
        elif n <=10:
            otimo+=1
        
        n = float(input('Digite uma nota: '))

    if i == 1:
        print(f'Otimo: {otimo:.0f}\t | Bom: {bom:.0f}\t')
        print(f'Regular: {regular:.0f}\t | Ruim: {ruim:.0f}\t')

    else:
        print('Nao colocou nenhuma nota valida')


def ex09():
    #comparacao entre numeros consecutivos
    n=int(input('Digite um numero: '))
    anterior=int(input('Digite um numero: '))
    igual,maior,menor = 0,0,0 #em relacao ao anterior
    i=0
    
    while n!= 0:
        i=1

        if n == anterior:
            igual +=1
        elif n > anterior:
            maior+=1
        elif n < anterior:
            menor +=1

        anterior = n
        n=int(input('Digite um numero: '))
        
    if i == 1:
        print(f'Iguais ao anterior: {igual}')
        print(f'Maiores que o anterior: {maior}')
        print(f'Menores que o anterior: {menor}')
    
    else:
        print('Ja comecou com 0')


def ex10():
    #relatorio com decisao final
    n=int(input('Nota: '))
    i=0
    abaixo,acima,soma = 0,0,0
    leitura =0

    while n >=0:
        leitura =1

        soma+=n
        i+=1
        if n >=60:
            acima+=1
        else:
            abaixo+=1
        n=int(input('nota: '))

    if leitura ==1: 
        media = soma / i
        print(f'notas lidas: {i}\t | media: {media:.1f} ')
        print(f'Notas acima 60: {acima}\t | abaixo: {abaixo}')

        if media >=70:
            print('Turma com desempenho satisfatorio')
        else:
            print('Turma precisa de reforço')

    elif leitura ==0:
        print('Nenhuma nota valida informada')



def ex11():
    #validacao com limite de tentativas
    senha=''
    i=0
    
    while senha != 'python123' and i<3:
        i+=1
        senha=input('Senha: ')

    if senha == 'python123':
        print('Acesso liberado')
    else:
        print('Acesso bloqueado')

    print(f'tentativas utilizadas: {i}')


def ex12():
    somar,parimpar,dobro,invalido = 0,0,0,0

    print('\n1- Somar 2 numeros | 2- Par/Impar | 3- Dobro | 4- Sair')
    op = int(input('Escolha opção: '))

    while op != 4:
        if op == 1:
            somar+=1

            n1=int(input('1 numero: '))
            n2=int(input('2 numero: '))
            print(f'Resultado da soma: {n1 + n2}')

        elif op== 2:
            parimpar +=1
            n=int(input('numero teste: '))
            if n % 2 == 0:
                print(f'{n} é par')
            else:
                print(f'{n} é impar')

        elif op== 3:
            dobro+=1

            n=int(input('Numero para dobrar: '))
            print(f'o dobro de {n} é {n*2}')
        else: 
            invalido+=1
            print('Opção invalida! Tente de 1 a 4')

        print('\n1- Somar 2 numeros | 2- Par/Impar | 3- Dobro | 4- Sair')
        op = int(input('Escolha opção: '))
    
    print(f'Opção 1 : {somar}\t  | Opção 2: {parimpar}')
    print(f'Opção 3: {dobro}\t  |Opção invalida: {invalido}')    

ex11()
