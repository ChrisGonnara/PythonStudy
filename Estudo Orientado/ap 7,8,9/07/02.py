#leia qtd turmas
#cada turma -- leia qtd_alunos, declarar reprovados e media geral, soma geral
#cada aluno --  leia 2 notas, mostre media e status (a >=7 R >=5 else rep)
#final cada turma mostre media geral da turma e o numero reprovados


qtd_turma = int(input('qtd turma: '))

for turma in range(1,qtd_turma+1):

    reprovados, media_geral, soma_geral = 0,0,0
    qtd_alunos = int(input('qtd alunos'))

    for aluno in range (1,qtd_alunos+1):
        n1=int(input('nota 1: '))
        n2=int(input('n2: '))

        media = (n1+n2) /2
        soma_geral+=media
        if media >=7: print(f'status: aprovado | media: {media:.1f} ')
        elif media >=5: print(f'status: recuperaçao | media: {media:.1f}')
        else: 
            print(f'status: reprovado | media: {media:.1f}')
            reprovados +=1
    
    media_geral = soma_geral / qtd_alunos

    print(f'media geral: {media_geral:.1f} | reprovados: {reprovados}')
