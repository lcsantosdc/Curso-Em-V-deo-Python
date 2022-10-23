from random import randint
from time import sleep

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-'*25)

print(f'Computador jogou {lista[computador]}')
print(f'Jogador jogou {lista[jogador]}')
print('-'*25)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCE')
    elif jogador == 2:
        print('Computador VENCE')
    else:
        print('Jogada INVÁLIDA')
if computador == 1:
    if jogador == 0:
        print('Computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('Jogada INVÁLIDA')
if computador == 2:
    if jogador ==0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA')
