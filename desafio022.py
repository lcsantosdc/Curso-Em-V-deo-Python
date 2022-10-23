nome = input('Digite seu nome completo: ')
splitado = nome.split()
qtletras = ''.join(splitado)
print(f'Nome com letras maiúsculas: {nome.upper()} \nNome com letras minúsculas: {nome.lower()} \nQuantidade de letras sem espaços: {len(qtletras)} \nSeu primeiro nome é {splitado[0]} e tem {len(splitado[0])} letras')
