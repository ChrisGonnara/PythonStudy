def ex05():
    #contagem caracter
    texto =input('frase: ')
    caracter=input('Caracter : ')
    i=0

    for letra in texto:
        if letra == caracter:
            contador +=1

    print(f'Quantidade: {i}')


def ex06():
    #ler 5 numeros e dizer o maior:

    maior= None

    for i in range (5):
        n=int(input('Digite um numero: '))
        if maior == None or n>maior:
            maior=n

def ex07():
    #palindromo
    palavra=input('Palavra: ')
    eh_palindromo=True
    tamanho=len(palavra)

    for i in range (tamanho):
        if palavra[i] != palavra[tamanho-1-i]:
            eh_palindromo = False

    print(eh_palindromo)


def ex08():
    n=int(input('tamanho matriz: '))
    for linha in range(n):#horizontal
        for coluna in range(n):#coluna
            
            if linha == 0 or linha == n-1 or coluna ==0 or coluna==n-1:
                #se for borda
                print('1', end='')
            else:
                #se for recheio
                print('0',end='')
        print()   #passe a proxima linha

def ex09():
    #prefixo palindromo
    palavra=input('string: ')
    prefixo = ''
    tamanho = len(palavra)

    for i in range (tamanho):
        eh_palindromo = True
        prefixo +=palavra[i]

        for j in range (i+1):
            if palavra[j] != palavra[i-j]:
                eh_palindromo=False


        if eh_palindromo: 
            print(prefixo)


def ex10(): 
    senha=input('Senha: ')
    tamanho=len(senha)
    maiusculas, minusculas, numeros, especiais = 0,0,0,0


    for carac in senha:
        if "A" <= carac <= "Z":
            maiusculas +=1
        elif "a" <= carac <= "z":
            minusculas +=1
        elif "0" <= carac <= "9":
            numeros +=1
        else:
            especiais +=1


    print(f'Quantidade caracter: {tamanho} | maiusculas: {maiusculas} ')
    print(f'minusculas: {minusculas} | digitos: {numeros}')
    print(f'especiais: {especiais}')
          


    if  tamanho >= 8 and maiusculas >0 and minusculas >0 and numeros >0 and especiais >0:
        print('Senha forte: Sim')
    else:
        print('Senha forte: Não')

def ex11():
    texto=input('Digite um texto: ')
    total_palavras=0
    tamanho=len(texto)

    for i in range (tamanho):
        if texto[i] != " ":
            if i == 0 or texto [i -1] == " ":
                total_palavras +=1
    print('Quantidade de palavras: {total_palavras}')  


def ex12():
    valor_inicial, aporte, taxa, meses = 0,0,0,0
    simulacao_executada = False
    historico_saldos = []

    while True:
        print('menu: ')
        print('1- Configurar simulação | 2- Executar simulação')
        print('3- Mostrar relatório geral | 4- Mostrar evolução mes a mes')
        print('0 - Encerrar Sistema')

        opcao=int(input('Escolha op: '))
        if opcao== 1:
            valor_inicial = float(input('Valor inicial: '))
            aporte=float(input('Aporte mensal: '))
            taxa= float(input('taxa de juros mensal: '))



        

ex10()
