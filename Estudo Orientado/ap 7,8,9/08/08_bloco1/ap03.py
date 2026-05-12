def calcular_comissao(valor_venda):
    return valor_venda * 0.05

def main():
    valor_venda = float(input('Valor venda: '))
    comissao = calcular_comissao(valor_venda)
    print(f'{comissao:.2f}')