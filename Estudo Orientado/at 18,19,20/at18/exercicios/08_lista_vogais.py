def lista_vogais_encontradas(palavra):
    vogais=[]
    for i in palavra:
        if i in 'AEIOUaeiou':
            vogais.append(i)

    return vogais