from math import hypot

'''o = float(input('Quanto mede o cateto oposto? '))
a = float(input('Quanto mede o cateto adjacente? '))
h = (pow(o,2) + pow(a,2)) ** (1/2) #h = o**(1/2) + a**(1/2)
print(f'\nCateto oposto {o} \nCateto adjacente {a} \nValor da hipotenusa {h:.2f}')'''

co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
h = hypot(co, ca)
print(f'O valor da hipotenusa é igual a {h:.2f}')
