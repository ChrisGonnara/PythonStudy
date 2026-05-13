def apenas_positivos(numeros):
    positivos=[]

    for i in range(len(numeros)):
        if numeros[i] >0:
            positivos.append(numeros[i])

    return positivos