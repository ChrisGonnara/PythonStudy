def classificar_desempenho(nota):
    if nota >=90:
        return  'Excelente'
    elif nota >=70:
        return 'Bom'
    elif nota >= 60:
        return 'Regular'
    else:
        return 'Insuficiente'
    
def main():
    nota=int(input('nota: '))
    if 0 <= nota <= 100:
        classificacao = classificar_desempenho(nota)
        print(f'nota: {nota}, classificaçao: {classificacao}')
main()