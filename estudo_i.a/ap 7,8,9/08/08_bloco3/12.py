def converter_tempo(tempo_segundos):
    horas = tempo_segundos //3600 
    sobra = tempo_segundos %3600
    minutos = sobra //60
    segundos = sobra % 60
    return horas,minutos,segundos

def main():
    tempo_segundos = int(input('tempo em segundos: '))

    horas,minutos,segundos = converter_tempo(tempo_segundos)

    print(f'{horas}h {minutos}m {segundos}s')
main()