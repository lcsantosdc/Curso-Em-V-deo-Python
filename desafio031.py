dist = float(input('Digite a distância de sua viagem: '))
if dist <= 200:
    preço = dist*0.50
else:
    preço = dist*0.45
print(f'O preço de sua viagem será de R${preço:.2f}')
