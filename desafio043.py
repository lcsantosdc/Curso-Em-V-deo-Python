from math import pow
print('\033[1;37m-' * 27)
print('      CÁLCULO DE IMC')
print('-\033[m' * 27)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
print('-\033[m' * 27)

imc = peso / (pow(altura, 2))
if imc < 18.5:
    valor_corporal = '\033[31mAbaixo do peso\033[m'
elif imc > 18.5 and imc < 25:
    valor_corporal = '\033[32mPeso ideal\033[m'
elif imc > 25 and imc < 30:
    valor_corporal = '\033[33mSobrepeso\033[m'
elif imc > 30 and imc < 40:
    valor_corporal = '\033[1;31mObesidade\033[m'
elif imc > 40:
    valor_corporal = '\033[31mObesidade mórbita\033[m'
print(f'\033[4;97mSeu Status\033[m: {valor_corporal}')
