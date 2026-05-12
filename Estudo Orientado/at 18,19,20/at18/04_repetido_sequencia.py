def repetido_seguido(numeros):
    for i in range (1,len(numeros)):
        if numeros [i] == numeros [i-1]:
            return True
    return False