def calcular_salario(salario_base,horas_extra):
    #extra=horas_extra * 50
    #salario_final = salario + extra
    return salario_base + (horas_extra * 50)

def main():
    qtd_funcionario = int(input('qtd funcionarios: '))
    for funcionario in range(1,qtd_funcionario+1):
        nome = input('nome: ')
        salario_base= float(input('salario: base'))
        horas_extra=int(input('horas extra feita: '))
        salario_final = calcular_salario(salario_base, horas_extra)

        print(f'{funcionario} nome: {nome} | salario_final: {salario_final}')


