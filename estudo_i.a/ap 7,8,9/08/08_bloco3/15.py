def calcular_inscricao(valor_base, taxa=10):
    return valor_base + (valor_base * taxa / 100)

def converter_tempo(tempo_segundos):
    horas = tempo_segundos //3600 
    sobra = tempo_segundos %3600
    minutos = sobra //60
    segundos = sobra % 60
    return horas,minutos,segundos

def gerar_resumo_tempo(nome,total_segundos):
    horas,minutos, segundos =converter_tempo(total_segundos)
    return f'{nome}: {horas}h  {minutos}m {segundos}s'

def eh_par(numero):
    if numero % 2 == 0: return True
    else: return False

def contar_pares_faixa(inicio,fim):
    contador=0
    for i in range (inicio, fim+1):
        if eh_par(i):
            contador+=1
    return contador


def main():
    n=int(input('quantidade de  participantes: '))

    for i in range(1,n+1):

        nome=input('nome participante')
        valor_base = int(input('Valor base: '))
        total_segundos=int(input('Segundos totais: '))
        inicio = int(input('inicio faixa: '))
        fim= int(input('final faixa: '))

        resumo = gerar_resumo_tempo(nome, total_segundos)
        contar_pares=contar_pares_faixa(inicio,fim)

        print(calcular_inscricao(valor_base))
        print(resumo)
        print(f'quantidade pares: {contar_pares}')
        
main()