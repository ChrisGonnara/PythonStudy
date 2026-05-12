def nota_valida(nota):
    if  0 <= nota <= 100:
        return True
    else:
        return False
    

def classificar_desempenho(nota):
    if nota >=90:
        return  'Excelente'
    elif nota >=70:
        return 'Bom'
    elif nota >= 60:
        return 'Regular'
    else:
        return 'Insuficiente'
    
def calcular_situacao(nota):
    if nota >=70:
        return 'Aprovado'
    elif nota >=50:
        return 'Recuperaçao'
    else:
        return 'Reprovado'


def gerar_resumo_correcao(nota):
    classificacao = classificar_desempenho(nota)
    situacao = calcular_situacao(nota)
    return classificacao,situacao
    

def main():
    for i  in range (3):
        nome=input('nome: ')
        nota=int(input('nota: '))

        if nota_valida(nota):
            classificacao,situacao = gerar_resumo_correcao(nota)

            print(nome)
            print(f'nota: {nota}')
            print(f'classificacao: {classificacao}')
            print(f'situaçao: {situacao}')
        else:
            print('nota invalida')
main()
