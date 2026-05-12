def inverter_string(palavra):
    contrario=''
    tamanho=len(palavra) -1

    for i in range(tamanho,-1,-1):
        contrario+=palavra[i]
    return contrario

def main():
    palavra=input('palavra: ')
    print(inverter_string(palavra))
main()
