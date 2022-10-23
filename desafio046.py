from time import sleep

print('-'*34)
botao = int(input('Aperte 0 para começar os fogos!!!\n[ 0 ] Contagem Regressiva: '))
print('-'*34)

if botao == 0:
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('PáTUMTUMTUMMPÁAA')

