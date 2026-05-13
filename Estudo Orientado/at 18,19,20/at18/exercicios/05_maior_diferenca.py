def maior_diferenca(numeros):
    maior= abs(numeros[1] - numeros[0])

    for i in range (1,len(numeros)):
        diferenca= numeros[i] - numeros[i-1]
        
        if diferenca > maior:
            maior = diferenca
    return maior
        