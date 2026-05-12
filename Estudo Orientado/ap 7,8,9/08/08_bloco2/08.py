def calcular_situacao(nota):
    if nota >=70:
        return 'Aprovado'
    elif nota >=50:
        return 'Recuperaçao'
    else:
        return 'Reprovado'
    
def main():
    nota=int(input('nota: '))

    if 0 <= nota <= 100:
        print(calcular_situacao(nota))
    