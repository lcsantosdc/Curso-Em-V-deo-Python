n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão: \n[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convetido para OCTAL é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente')
