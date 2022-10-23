from datetime import date

anoatual = date.today().year
quant1 = 0
quant2 = 0

for pess in range(1,8):
    data = int(input(f'Data de nascimento da {pess}ª pessoa: '))
    idade = anoatual - data
    if idade >= 21:
        quant1 = quant1 + 1
    else:
        quant2 = quant2 + 1

print(f'{quant1} pessoas são maiores de idade e {quant2} são menores')
