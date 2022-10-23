termo = int(input('Primeiro termo: '))
razao = int(input("Razão: "))
décimo = termo + (10 - 1) * razao

for c in range(termo, décimo+razao, razao):
    print(c, end=' -> ')
print('ACABOU')
