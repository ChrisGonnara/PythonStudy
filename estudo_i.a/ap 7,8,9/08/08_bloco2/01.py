def nota_valida(nota):
    if  0 <= nota <= 100:
        return True
    else:
        return False
    
def main():
    nota=int(input('Nota: '))
    print (nota_valida(nota))

