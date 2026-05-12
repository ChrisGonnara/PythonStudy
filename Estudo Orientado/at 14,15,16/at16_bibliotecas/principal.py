from util_datas import *
def main():
    data_atual=input('data: ')
    data_nascimento=input('data nascimento: ')

    if data_valida(data_atual) == False:
        print('Data atual invalida')

    elif data_valida(data_nascimento) == False:
        print('Data nascimento invalida')
    else:
        idade=calcular_idade(data_atual, data_nascimento)
        print(f'idade: {idade} ')

if __name__ == "__main__":
    main()