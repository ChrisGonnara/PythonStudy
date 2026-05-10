def calcular_valor_final(valor_produto,desconto):
    valor_desconto = valor_produto / 100 * desconto
    return valor_produto -valor_desconto

def main():
    valor_produto = float(input('Valor produto: '))
    desconto= float(input('Desconto %:'))
    valor_final = calcular_valor_final(valor_produto,desconto)

    print(f'valor final: {valor_final}')
main()