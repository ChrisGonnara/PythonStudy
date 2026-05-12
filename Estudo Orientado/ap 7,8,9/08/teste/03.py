def conceito(nota):
    if nota >=9:
        return 'A'
    elif nota >=7:
        return 'B'
    elif nota >=5:
        return 'C'
    else:
        return 'D'
    
def main():
    qtd_alunos = int(input('qtd alunos'))

    for aluno in range(1,qtd_alunos+1):
        nome = input(f'{aluno}: nome aluno: ')
        nota = int(input('nota: '))
        analisar= conceito(nota)
        print(f'nome: {nome} | conceito: {analisar}')
main()