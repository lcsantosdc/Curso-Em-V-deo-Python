soma = 0
cont = 0
for c in range(2, 501, 2):
    if c%10 == 0:
        soma = soma + c
        cont = cont + 1
print(f' soma de todos os {cont} valores soicitados é de {soma}')
