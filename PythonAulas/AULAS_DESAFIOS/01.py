#informar usuario o nivel de risco associado ao indice uv observado em determinado momento
#sistema deve classificar o indice uv em 4 categorias de risco, baixo, moderado, alto, muito alto
#de acordo com o indice informado. a partir dessa classificacao o aplcaitivo podera exibir
#uma indicacao clara do nivel de exposicao ao qual ele esta sujeito
#escreva um programa deverra armazenar o valor do indic e em uma variavel e classificar o risco
#baixo,moderado,alto,muito alto

#tc1: 0 -> baixo 
#tc2 -50 -> baixo
#tc4 8 -> muitoo altoo
def ex00():
    indice = int (input('INDICE UV: '))
    risco = ''
    if indice >=8:
        risco = 'Muito alto'
    elif indice >=5:
        risco = 'Alto'
    elif indice>=3:
        risco = 'Moderado'
    else:
        risco='Baixo'
    print(f'risco: {risco}')


def ex01():
#tc1: 10 -> alto
#tc2: 0 -> baixo
#tc3 2 -> moderado
    consumo = int (input('Litros consumido no dia: '))
    classe = ''
    if consumo < 1:
        classe='baixo'
    elif consumo <=2:
        classe='moderado'
    else:
        classe = 'alto'
    print(f'classe: {classe}')

def ex02(): 
    #limite 60 km/h
    # < limite ok
    # 20 km > limite excesso
    # > 20 km > acima excesso grave de velocidade
    radar = float(input('Velocidade registrada: '))
    registro = ''
    if radar <= 60:
        registro = 'permitido'
    elif radar <= 80:
        registro = 'Excesso de velocidade'
    else:
        registro = 'excesso grave de velocidade'
    print(f'velocidade: {radar}km/h \n registro: {registro}')

def ex03():
    #<50 boa    ||  50 < 100 moderada   || > 100 qualidade ruim
    #de o valor de indice de qualidade do ar e determine qual classificacao

    indice = int (input('valor qualidade do ar: '))
    classe = ''
    if indice < 50:
        classe = 'boa'
    elif indice <=100:
        classe = 'moderada'
    else:
        classe = 'ruim'
    print (f'qualidade: {classe}')

def ex04():
    # temp < 15 fria    || 15 - 25 amenas   || > 25 quentes
    # dado valor da temperatura, determine qual classificacao deve ser exibida

    temp=float(input('Temperatura: '))
    classe = ''

    if temp < 15:
        classe = 'Fria'
    elif temp <=25:
        classe = 'Amena'
    else:
        classe = 'Quente'

    print (f'classificação: {classe}')

def ex05():
    #matriculado no evento  &  idade >= 18  || veja se pode participar
    evento=int (input('matriculado? [1]Sim [0]Não'))
    idade= int (input('Idade: '))

    if evento == 1 & idade >=18:
        print('Pode participar da atividade')
    else:
        print('Não pode participar')

def ex06():
    # gratuito >=65 or deficiencia  ||indicar que tem direito a gratuito ou nao
    idade = int(input('Idade: '))
    deficiencia = str(input('Possui deficiencia? [s // n]'))
    if idade >=65 or deficiencia == 's':
        print('Tem direito a transporte gratuito')
    else:
        print('Não tem direito a transporte gratuito')

def ex07():
    #alerta vel > 60 'AND' chuva >50mm  indicar alerta de tempestade||indicar nao ha alerta
    velocidade=int(input('Velocidade do vento: '))
    chuva =int(input('Chuva prevista em mm: '))

    if velocidade > 60 and chuva >50:
        print ('ALERTA DE TEMPESTADE')
    else:
        print('Não há alerta meteorológico')




ex03()
