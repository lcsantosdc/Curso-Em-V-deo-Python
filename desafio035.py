print('='*24)
print('Analisador de triângulo')
print('='*24)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('Os segmentos acima PODEM FORMAR um triângulo!'if r1<r2+r3 and r2<r1+r3 and r3<r1+r2 else'Os segmentos acima NÃO PODEM FORMAR um triângulo!')
