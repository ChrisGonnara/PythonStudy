def calcular_calorias(calorias_base,bonus=0):
    return calorias_base + bonus

def calcular_tempo_treino(tempo_principal,aquecimento=10):
    return tempo_principal + aquecimento

def analisar_desempenho(tempo_minutos):
    return tempo_minutos //60, tempo_minutos % 60

def consolidar_treino(calorias,tempo,meta=300):
    diferenca=calorias-meta

    atingiu = calorias >= meta  # retorna True ou False direto
    mensagem = 'Meta atingida' if atingiu else 'Meta não atingida'

    return diferenca, atingiu,mensagem