def ex01():
    n1= int(input("Digite o 1 n: "))
    n2= int(input("Digite o 2 n: "))
    soma = n1 + n2
    soma_str = str(soma)
    print(f"A soma dos valores é: { soma_str}")

def ex02():
    n1=float(input("Valor da hora: "))
    n2=float(input("Qtd hrs trabalhadas por dia: "))
    salario= n1*n2
    print(f"O salário final é {salario}")

def ex03():
    num=int(input("Digite um numero pra ver se é par ou impar"))
    paridade=num % 2
    eh_par = paridade == 0
    if (paridade==0):
        print("é Par")
    elif (paridade ==1):
        print("é impar")

def ex04():
    cor1=input("Digite uma cor: ")
    cor2=input("Digite uma cor: ")
ex01()  