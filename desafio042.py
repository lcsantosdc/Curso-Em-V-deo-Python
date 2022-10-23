r1 = int(input('Primeira medida: '))
r2 = int(input('Segunda medida: '))
r3 = int(input('Terceira medida: '))

if r1 == r2 == r3:
    print('FORMA um triangulo EQUILÁTERO')
elif r1 != r2 == r3 or r2 != r1 == r3 or r3 != r1 == r2:
    print('FORMA um triângulo ISÓSCELES')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('FORMA um triângulo ESCALENO')
else:
    print('Não FORMA nenhum triângulo')
