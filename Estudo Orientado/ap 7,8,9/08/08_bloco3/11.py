def calcular_inscricao(valor_base, taxa=10):
    return valor_base + (valor_base * taxa / 100)

def main():
    valor_base = int(input('Valor base: '))

    print(calcular_inscricao(valor_base))
    print(calcular_inscricao(valor_base, 5))
main()