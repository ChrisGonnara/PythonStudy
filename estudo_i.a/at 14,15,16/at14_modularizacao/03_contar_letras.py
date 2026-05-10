def apenas_letras(string):
    contador = 0
    for i in string:
        if 'a' <= i <= 'z' or 'A' <=i <='Z':
            contador+=1
    return contador

def main():
    string=input('String: ')
    print(apenas_letras(string))
main()