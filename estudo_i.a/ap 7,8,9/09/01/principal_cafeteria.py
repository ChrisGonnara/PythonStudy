from funcoes_cafeteria import *

def main():
    nome_cafe=input('nome: ')
    preco_base = float(input('preco base cafe: '))
    acrescimo=float(input('acrescimo'))

    nome_acomp=input('nome: ')
    acompanhamento=float(input('preco acompanhamento: '))
    desconto=int(input('desconto %: '))

    preco_cafe= calcular_preco_cafe(preco_base, acrescimo)
    preco_acomp=calcular_acompanhamento(acompanhamento,desconto)

    nome_cafe, valor_cafe = resumo_item(nome_cafe,preco_cafe)
    nome_acomp, valor_acomp= resumo_item(nome_acomp, preco_acomp)

    subtotal,taxa,total=calcular_totais(preco_cafe,preco_acomp)

    print(f'nome cafe: {nome_cafe}, valor:  {valor_cafe}')
    print(f'nome acomp: {nome_acomp}, valor:  {valor_acomp}')
    print(f'preco: {subtotal}')
    print(f'taxa: {taxa} | total: {total}')
main()
