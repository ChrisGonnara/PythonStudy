def calcular_fatura(horas):
    if horas <=100:
        fatura = horas * 5
    elif horas <=500:
        fatura = 100 * 5 + (horas-100) *  4
    else:
        fatura = 100 * 5 + 400 * 4 + (horas-500) * 2.5
    return fatura

def main():
    id_cliente =int(input('id: '))
    faturamento_total=0

    while id_cliente !=0:
        horas=int(input('horas: '))
        fatura=calcular_fatura(horas)
        faturamento_total+=fatura

        print(f'fatura: {fatura}')
        id_cliente=int(input('ID: '))
    print(f'faturamento total: {faturamento_total:.2f}')
main()