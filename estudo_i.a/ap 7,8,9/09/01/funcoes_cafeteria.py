def calcular_preco_cafe(preco_base,acrescimo=0):
    return preco_base + acrescimo

def calcular_acompanhamento(preco,desconto=0):
    valor_desconto = preco * desconto /100
    return preco - valor_desconto

def resumo_item(nome,valor):
    return nome, f'R$ {valor:.2f}'

def calcular_totais(valor1,valor2, taxa_servico=10):
    subtotal= valor1+valor2
    taxa= subtotal* taxa_servico /100
    total_final = subtotal+taxa

    return subtotal,taxa,total_final