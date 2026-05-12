def lista_palindromo():
    numeros=[]
    for i in range(7):
        n=int(input('numero: '))
        numeros.append(n)

    eh_palindromo=True
    for n in range (len(numeros)//2):
        if numeros[n] != numeros[len(numeros)-1-n]:
            eh_palindromo = False
    
    print(f'Lista palindromo: {eh_palindromo}')
lista_palindromo()