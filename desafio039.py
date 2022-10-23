from datetime import date

print('\033[32m+'*31)
print('\033[1;32m+++++ ALISTAMENTO MILITAR +++++\033[32m')
print('\033[32m+'*31)
print('\033[1;97mINFORME SEU ANO DE NASCIMENTO:')
print('-\033[m'*31)

anoatual = date.today().year
nasc = int(input('Ano:\033[m '))
idade = anoatual - nasc


print(f'Quem nasceu em {nasc} tem {idade} ano(s) em {anoatual}')
if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print(f'Você ainda vai se alistar. Faltam {18-idade} ano(s) para o alistamento \nSeu alistamento será em {anoatual+(18-idade)}')
elif idade > 18:
    print(f'Passou {idade-18} ano(s) de seu alistamento \nSeu alistamento foi em {anoatual-(idade-18)}')
print('\033[97m-\033[m'*31)
