def criptografar(texto):
    resultado=''
    for c in texto:
        if c == 'z':
            resultado +='a'
        else:
            resultado += chr(ord(c) +1)
    return resultado

def main():
    texto=input('texto: ')
    while texto != 'fim':
        print(criptografar(texto))
        texto=input('texto: ')
main()
