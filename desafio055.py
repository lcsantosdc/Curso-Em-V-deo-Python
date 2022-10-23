list = []
for p in range(1,6):
    pesos = float(input(f'Digite o peso da {p}ª pessoa: '))
    list.append(pesos)          #adiciona cada peso digitado a lista

print(f'O maior peso lido foi {max(list)}kg e o menor peso é de {min(list)}kg')
