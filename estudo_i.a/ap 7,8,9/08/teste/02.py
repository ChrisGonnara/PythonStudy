def analisar_idade(idade):
    if idade < 18:
        return 'menor de idade'
    elif idade <65:
        return 'adulta'
    else:
        return 'idosa'
    
def main():
    nome = input('Nome: ')
    idade = int (input('Idade: '))

    classificacao= analisar_idade(idade)

    print(f'{nome}, classificaçao = {classificacao}')

main()