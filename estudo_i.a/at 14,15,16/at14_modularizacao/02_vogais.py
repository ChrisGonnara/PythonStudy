def para_vogais(string):
    vogais_presente=''
    for i in string:
        if i in 'aeiouAEIOU':
            vogais_presente +=i
    
    return vogais_presente

def main():
    string=input('String')
    print(para_vogais(string))
main()
        