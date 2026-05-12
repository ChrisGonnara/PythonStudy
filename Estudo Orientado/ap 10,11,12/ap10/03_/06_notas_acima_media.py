def notas_acima_media():
    notas=[]
    soma = 0
    acima=[]

    for i in range(10):
        n=int(input('notas: '))
        notas.append(n)
        soma +=n

    media= soma/ len(notas)

    for nota in notas:
        if nota > media:
            acima.append(nota)

    n_acima = len(acima)
    print(f'media turma: {media}')
    print(f'qtd acima da media: {n_acima}')
    print(f'notas acima: {acima}')

notas_acima_media()


