def converter_tempo(tempo_segundos):
    horas = tempo_segundos //3600 
    sobra = tempo_segundos %3600
    minutos = sobra //60
    segundos = sobra % 60
    return horas,minutos,segundos

def gerar_resumo_tempo(nome,total_segundos):
    horas,minutos, segundos =converter_tempo(total_segundos)
    return f'{nome}: {horas}h  {minutos}m {segundos}s'

def main():
    nome = input('nome: ')
    total_segundos=int(input('Segundos totais: '))

    resumo = gerar_resumo_tempo(nome, total_segundos)

    print(resumo)
main()