def exibir_cabecalho():
    print(f'loja X')
    print(f'Sistema de atendimento')

def exibir_cliente(nome):
    print(f'Cliente: {nome}')

def calcular_comissao(valor_venda):
    return valor_venda * 0.05

def calcular_valor_final(valor_produto,desconto):
    valor_desconto = valor_produto / 100 * desconto
    return valor_produto -valor_desconto



def main():
    exibir_cabecalho()

    nome = input('nome cliente: ')
    exibir_cliente(nome)

    valor_produto = float(input('valor produto: '))
    desconto = float(input('desconto %: '))
    valor_final = calcular_valor_final(valor_produto, desconto)
    comissao = calcular_comissao(valor_final)  
    
    print(f'valor original: R$ {valor_produto:.2f}')
    print(f'valor final: R$ {valor_final:.2f}')
    print(f'comissão: R$ {comissao:.2f}')

main()


