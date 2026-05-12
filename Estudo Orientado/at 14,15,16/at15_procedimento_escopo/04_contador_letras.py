def contador_letras(palavra,letra):
    contador=0
    for letras in palavra:
        if letras == letra:
            contador+=1
    return contador

def main():
    palavra=input('palavra: ')
    letra=input('letra: ')

    print(contador_letras(palavra,letra))
main()
