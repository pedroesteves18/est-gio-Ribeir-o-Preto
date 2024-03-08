
num = int(input("numero desejado"))
numeros = []
numeros.append(0)
numeros.append(1)

for item in range(0,num):
    numeros.append(numeros[item] + numeros[item+1])
    result = numeros[-1]
    if result > num:
        print(f'o numero informado ${num} nao esta na sequencia')
        break
    elif result == num:
        print(f'o numero informado ${num} esta na sequencia')
        break

