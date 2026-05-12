def contador_espaco(texto):
    contador=0
    for c in texto:
        if c == ' ':
            contador+=1
    return contador

def main():
    texto=input('texto: ')
    print(contador_espaco(texto))
main()
