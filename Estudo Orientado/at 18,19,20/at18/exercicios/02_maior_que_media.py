def maior_media(numeros):
    soma=0
    for numero in numeros:
        soma+=numero

    media= soma/ len(numeros)
    maior=0

    for numero in numeros:
        if numero > media:
            maior+=1
    return maior