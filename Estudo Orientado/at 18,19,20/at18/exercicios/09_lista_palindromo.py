def palindromo(string):
    inverso=[]

    for i in range (len(string)-1,-1,-1):
        inverso.append(string[i]) 
    return inverso