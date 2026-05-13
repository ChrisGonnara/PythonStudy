def ordem_crescente(numeros):
    for i in range (1,len(numeros)):
        if numeros[i] <= numeros [i-1]:
            return False
    return True