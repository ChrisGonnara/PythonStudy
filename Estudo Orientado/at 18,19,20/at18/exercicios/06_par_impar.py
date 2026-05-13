def verificar_par_impar(numeros):
    for i in range (1,len(numeros)):
        if numeros[i] % 2 == numeros[i-1] % 2:
            return False
    return True