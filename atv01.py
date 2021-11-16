tempMed = list(range(4))
tempMed[0] = 21,5
tempMed[1] = 21,7
tempMed[2] = 20,6
tempMed[3] = 18,5




for i in range (0,4):
    if tempMed[i] > tempMed[i-1]:
        maior = tempMed[i]
    else:
        menor = tempMed[i]


print(maior)
print(menor)



