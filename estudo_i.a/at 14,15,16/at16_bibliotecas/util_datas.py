def verificar_formato_data(data):
    tamanho = len(data)
    if tamanho !=10:
        return False
    elif data[2] != '/' or data[5] !='/':
        return False
    
    for i in range(len(data)):
        if i !=2 and i !=5:
            if data[i] < '0' or data[i] >'9':
                return False
    return True

def separar_data(data):
    d=m=a=''
    for c in range (len(data)):
        if c <2:
            d+=data[c]
        if c >2 and c <5:
            m+=data[c]
        elif c >5:
            a+=data[c]
    return int(d),int(m),int(a)

def ano_bissexto(ano):
    if ano % 400 ==0:
        return True
    elif ano % 4 ==0 and ano % 100 !=0:
        return True
    else:
        return False
    
def data_valida(data):
    formato =verificar_formato_data(data)

    if formato == False:
        return False

    dia,mes,ano= separar_data(data)
    bissexto= ano_bissexto(ano)
    
    if mes <1 or mes >12:
        return False
    
    if mes == 2:
        if bissexto == True:
            return 1 <= dia <= 29
        else:
            return 1<= dia <= 28
        
    if mes in (4,6,9,11):
        return 1<= dia <=30
    
    else:
        return 1 <=dia <=31

def dias_no_mes(mes,ano):
    if mes ==2:
        if ano_bissexto(ano):
            return 29
        else:
            return 28
    if mes in (4,6,9,11):
        return 30
    return 31

def calcular_idade(data_atual,data_nascimento):
    data1=data_valida(data_atual)
    data2=data_valida(data_nascimento)
    if data1 == False or data2==False:
        return -1
    dia_atual,mes_atual,ano_atual= separar_data(data_atual)
    dia_nascimento,mes_nascimento,ano_nascimento=separar_data(data_nascimento)

    idade = ano_atual-ano_nascimento

    if mes_atual < mes_nascimento:
        idade -=1
    elif mes_atual == mes_nascimento:
        if dia_atual < dia_nascimento:
            idade -=1
    return idade
    
