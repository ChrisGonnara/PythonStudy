def calcular_reajuste(salario):
    reajuste=0
    if salario < 2000: reajuste =  salario * 0.2
    elif salario < 5000: reajuste = salario * 0.1
    else: reajuste = salario * 0.05
    salario_total = salario+reajuste
    return salario_total

def main():
    salario=float(input('salario: '))
    resultado = calcular_reajuste(salario)
    print(resultado)
main()



