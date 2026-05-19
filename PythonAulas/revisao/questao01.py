def validar_senha(senha):
    if len(senha)<8 or ' ' in senha:
        return False
    
    tem_numero =False
    tem_maiuscula=False

    for c in senha: 
        if c.isdigit():
            tem_numero=True
        if c.isupper():
            tem_maiuscula=True
    return tem_numero and tem_maiuscula

def main():
    senha=input('senha: ')
    total=0
    validas=0
    while senha != 'sair':
        total+=1
        if validar_senha(senha) == True:
            print('Válida')
            validas+=1
        else:
            print('Inválida')
        senha=input('senha: ')

    if total >0:
        porcentagem = (validas/total) * 100
        print(f'porcentagem de validas: {porcentagem:.1f}%')
main()