def main():
    numeros=[]
    for i in range (5):
        n=int(input('numeros:'))
        numeros.append(n)

    print(numeros)
    for n in numeros:
        print(n)

    for n in range (len(numeros)):
        print(numeros[n])

main()