def contar_abaixo_media(tempos):
    soma=0
    abaixo=0
    for tempo in tempos:
        soma+=tempo

    media= soma / len(tempos)

    for tempo in tempos:
        if tempo < media:
            abaixo+=1
        
    return abaixo

def main():
    tempos=[]
    numero=int(input('-1 pra parar, numero:'))
    while numero !=-1:
        tempos.append(numero)
        numero=int(input('-1 pra parar, numero:'))

    abaixo_media=contar_abaixo_media(tempos)
    print(f'qtd abaixo da media: {abaixo_media}')
main()