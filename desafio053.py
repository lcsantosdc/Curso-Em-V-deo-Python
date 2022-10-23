frase = str(input('Digite uma frase: ')).upper().strip().split()
frase1 = ''.join(frase)
frase2 = ''.join(reversed(frase1))

if frase1 == frase2:
    print(f'Essa frase É UM PALÍNDROMO.\nFrase normal: {frase1}\nFrase de trás pra frente: {frase2}')
else:
    print(f'Essa frase NÃO É UM PALÍNDROMO, pois não são iguais.\nFrase normal: {frase1}\nFrase de trás pra frente: {frase2}')
