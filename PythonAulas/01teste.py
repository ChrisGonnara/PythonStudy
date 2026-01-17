def   desafio_soma(): 
    n1 = input ('primeiro número: ')
    n2 = input ('segundo numero: ')
    soma = int(n1)+int(n2)

    #aqui vai dar 63 se voce digitar 6 e 3
    #pq sao strings
    print (f'A soma enter {n1} e {n2} é...{n1+n2}')

def desafio_data():
    dia = input ("dia: ")
    mes = input ("mes: ")
    ano = input ("ano: ")
    print(f"Data: {dia}/{mes}/{ano}")

def calcular_idade():
    anoatual = int (input ("ano atual: ")) #converte
    nascimento = int (input ('ano nascimento: ')) #converte
    calculo = anoatual - nascimento
    print (f'Voce tem ou fará {calculo} anos')

def lanchonete():
    hamburguer = float (input ("Hamburguer: "))
    batata = float (input ("batata: "))
    soma = hamburguer + batata
    print (f"total = {soma}")

def checkout ():
    nome = str(input('nome: '))
    quantidade = int(input ('quantidade: '))
    valor = float(input('valor hamburguer: '))
    total =  quantidade * valor

    print (f"ola {nome}, o total do seu pedido de {quantidade} hamburguer é {total:.2f} reais")


checkout ()