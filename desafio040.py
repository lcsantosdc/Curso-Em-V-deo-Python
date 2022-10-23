from time import sleep


print('-'*44)
print('\033[1;97m- MÉDIA ABAIXO DE\033[m \033[1;31m5.0\033[m \033[1;97mESTÁ REPROVADO.\033[m\n\033[1;97m- MÉDIA ENTRE\033[m \033[1;31m5.0 \033[1;97mE\033[m \033[1;31m6.9\033[m \033[1;97mESTÁ DE RECUPERAÇÃO.\033[m\n\033[1;97m- MÉDIA\033[m \033[1;34m7.0 \033[1;97mOU SUPERIOR ESTÁ APROVADO.\033[m')
print('-'*44)

nota_1 = float(input('\033[1;97mValor da primeira nota: '))
nota_2 = float(input('Valor da segunda nota:\033[m '))
media = (nota_1 + nota_2) / 2

print('\033[31mAVALIANDO...\033[m')
print('-'*44)
sleep(1)
print(f'Média {media:.1f}')

if media <= 5.0:
    print('\033[31mReprovado\033[m.')

elif 6.9 > media >= 5.0:
    print('\033[33mRecuperação\033[m.')

elif media >= 7.0:
    print('\033[32mAprovado\033[m.')
