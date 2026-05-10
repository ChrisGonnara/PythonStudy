def para_maiusculo(string):
    resultado=''
    for i in string:
        if 'a' <= i <='z':
            resultado += chr(ord(i)-32)
            #ord(i)- pega ascii da letra
            #chr(65)0 converte para letra (char)
        else:
            resultado +=i
    return resultado

def main():
    string=input('String: ')
    print(para_maiusculo(string))
main()