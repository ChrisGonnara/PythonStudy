def ex01():
    #potencia   |horas uso dia  |dias de uso mes    |preço energia
    #calcule consumo diario, mensal custo mensal(reais) e imprima na tela
    #consumo diario: (potencia * horas) / 1000
    pot=int(input('Potencia: '))
    horas_dia=int(input('Horas de uso no dia: '))
    uso_mensal=int(input('Dias no mes uso: '))
    preço=float(input('Custo da energia (r$/kWh)'))

    consumo_dia= (pot*horas_dia) / 1000
    consumo_mensal =  consumo_dia* uso_mensal
    custo_mensal = consumo_mensal * preço
    print ('Relatorio de consumo')
    print ('---------------------')
    print (f'Consumo diario (kWh): {consumo_dia} ')
    print (f'Consumo mensal:(kwh): {consumo_mensal} ')
    print (f'Custo mensal (r$): {custo_mensal}')


def ex02():
    #litros necessario  |custo total viagem
    distancia=int(input('Distancia: '))
    consumo= int (input('Consumo km/l: '))
    preço= float(input('Preço gasolina: '))

    necessario = distancia / consumo
    custo = necessario * preço

    print (f'Combustivel necessario: {necessario}')
    print (f'Custo total: {custo}')


def ex03():
    n1=int(input('Nota 1: '))
    n2=int(input('Nota 2: '))
    n3=int(input('Nota 3: '))

    soma = n1+n2+n3
    media = soma/3
    media_max = 10 - media

    print (f'soma notas: {soma}')
    print (f'media: {media}')
    print (f'pontos pra media max: {media_max} ')


def ex04():
    preço=float(input('Preco produto: '))
    imposto=float(input('imposto:  (de 0 a 100%)')) / 100
    frete= float(input('Frete valor: '))

    custo_imposto= preço * imposto
    valor_total= custo_imposto + frete + preço

    print (f'valor imposto:  {custo_imposto}')
    print (f'Valor total: {valor_total}')

def ex05():
    #distancia total  |distancia semanal  |combustivel necessario  |custo semanal
    dist_entr= int (input('media km entrega: \t'))
    entrega_dia=int(input('entregas por dia: \t'))
    dias_trabalhados= int(input('dias trabalhados na semana: \t'))
    consumo_medio=float(input('Consumo medio: km/l: \t'))
    preço_combustivel = float(input('Combustivel preço: \t'))

    distancia_dia= dist_entr * entrega_dia
    distancia_semanal = distancia_dia * dias_trabalhados
    combustivel_necessario = distancia_semanal / consumo_medio
    custo_semanal = preço_combustivel * combustivel_necessario

    print (f'\nDistancia diaria: \t{distancia_dia}')
    print (f'Distancia semanal km/h: \t{distancia_semanal}')
    print (f'Combustivel necessario (litros): \t{combustivel_necessario}')
    print (f'Custo semanal de combustivel: R$ \t{custo_semanal}')

def ex06(): 
    #total de palavras livro| tempo total de leitura, em min e depois horas|
    #quantos dias serao necessario pra terminar o livro
    paginas=float(input('Numero de paginas total: \t'))
    palavras_media=float(input('Numeros palavras media pagina: \t'))
    velocidade_media= float(input('lido palavras por min: \t'))
    minutos_diario = float(input('Minutos livre por dia: \t'))

    total_palavras = paginas * palavras_media
    tempo_minutos= total_palavras / velocidade_media
    tempo_horas = tempo_minutos / 60
    termino_dias= tempo_minutos / minutos_diario

    print (f'\nTotal palavras no livro:\t {total_palavras:.0f}')
    print (f'Tempo total de leitura (min):\t {tempo_minutos:.2f}')
    print (f'Tempo total de leitura (horas):\t {tempo_horas:.2f} ')
    print(f'Dias estimados para terminar o livro:\t {termino_dias}')






ex06()