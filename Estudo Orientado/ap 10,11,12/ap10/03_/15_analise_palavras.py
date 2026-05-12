def analise_palavras():
    palavras=[]
    for i in range(10):
        p=input(f'{i+1} palavra : ')
        palavras.append(p)

    maior=palavras[0]
    menor=palavras[0]
    contar_palavra_a=0
    maisde_5=[]
    
    for palavra in palavras:
        if len(palavra) > len(maior):
            maior= palavra
        if len(palavra) < len(menor):
            menor=palavra

        if palavra[0] =='a':
            contar_palavra_a +=1
        
        if len(palavra)>5:
            maisde_5.append(palavra)

    print(f'maior: {maior} | menor: {menor}')
    print(f'qtd palavra comeca com a: {contar_palavra_a}')
    print(f'palavras que contem mais de 5 caracter : {maisde_5}')
analise_palavras()


