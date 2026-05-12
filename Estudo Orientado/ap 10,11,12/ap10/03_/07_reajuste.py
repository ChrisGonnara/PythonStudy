def reajuste_preco():
    precos=[]
    precos_novos=[]

    for i in range(8):
        p=float(input(f'{i+1} preco: '))
        precos.append(p)

    for p in precos:
        if p <100:
            precos_novos.append(p *1.10)
        else:
            precos_novos.append(p*1.05)
    
    print(f'antigos: {precos} novos: {precos_novos}')

reajuste_preco()

