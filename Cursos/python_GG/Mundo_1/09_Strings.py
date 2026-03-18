# === RESUMO TEÓRICO (AULA 09) ===

def teoria():
    frase = 'Curso em video Python'
    lista = ['Curso', 'em', 'video']

    # FATIAMENTO
    print(frase[9], frase[9:13], frase[:5], frase[15:], frase[9::3])

    # ANÁLISE
    len(frase)              # Tamanho
    frase.count('o')        # Conta letra
    frase.find('video')     # Posição (rfind para última)
    'Curso' in frase        # Existe? (True/False)

    # TRANSFORMAÇÃO
    frase.replace('Python', 'Android')
    frase.upper()           # MAIÚSCULO
    frase.lower()           # minúsculo
    frase.capitalize()      # Só a 1 letra
    frase.title()           # 1 letra de cada Palavra
    frase.strip()           # Remove espaços inúteis

    # DIVISÃO/JUNÇÃO
    palavras = frase.split() # Vira lista
    '-'.join(lista)          # Junta lista


def pratico():
    frase = 'Curso em video python'
    print(frase.upper().count('O'))
    print(len(frase.strip()))
    
    # Acessando: Lista [palavra] [letra]
    dividido = frase.split()
    print(dividido[0][3]) 

# === EXERCÍCIOS ===

def ex22():
    """Análise de nome: Maiúsculo, minúsculo e contagem de letras."""
    nome = str(input('Nome completo: ')).strip()
    print(f'MAIÚSCULA: {nome.upper()}')
    print(f'Minúscula: {nome.lower()}')
    print(f'Total de letras: {len(nome) - nome.count(" ")}')
    print(f'Letras no 1º nome: {len(nome.split()[0])}')

def ex23():
    """Separador de dígitos: Milhar, Centena, Dezena e Unidade."""
    num = int(input('Digite um número (0 a 9999): '))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print(f'U: {u} | D: {d} | C: {c} | M: {m}')

def ex24():
    """Valida se a cidade começa com 'SANTO'."""
    cdd = str(input('Cidade natal: ')).strip()
    print(f'Começa com Santo? {cdd[:5].upper() == "SANTO"}')

def ex25():
    """Busca sobrenome 'Silva' em qualquer parte do nome."""
    nome = str(input('Nome: ')).strip()
    print(f'Tem Silva? {"SILVA" in nome.upper()}')

def ex26():
    """Análise de letra 'A': Contagem e posições (primeira/última)."""
    frase = str(input('Frase: ')).strip().lower()
    print(f'Vezes que aparece: {frase.count("a")}')
    print(f'Primeira posição:  {frase.find("a") + 1}')
    print(f'Última posição:    {frase.rfind("a") + 1}')

def ex27():
    """Isola o primeiro e o último nome de uma pessoa."""
    nome = str(input('Nome completo: ')).strip().split()
    print(f'Primeiro nome: {nome[0]}')
    print(f'Último nome:   {nome[-1]}')

#chamar a função aqui:
ex27()