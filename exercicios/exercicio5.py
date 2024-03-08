
test = input("digite uma string")

aux = []
for i in range(len(test)-1,-1,-1):
    aux.append(test[i])

for i in aux:
    print(i)