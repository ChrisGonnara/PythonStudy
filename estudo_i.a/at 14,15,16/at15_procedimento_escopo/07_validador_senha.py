def validar_senha(senha):
    if len(senha) <6:
        return False
    
    tem_numero = False
    for c in senha:
        if c in ['0','1','2','3','4','5','6','7','8','9']:
            #c.isdigit()
            tem_numero=True
    
    return tem_numero

def main():
    senha=input('senha: ')
    print(validar_senha(senha))
main()

        