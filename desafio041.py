from datetime import date

print('-' * 25)
print('TABELA DE CATEGORIAS: \n- Até 9 anos: \033[34mMIRIM\033[m. \n- Até 14 anos: \033[34mINFANTIL.\033[m \n- Até 19 anos: \033[34mJÚNIOR\033[m. \n- Até 25 anos: \033[34mSÊNIOR\033[m. \n- Acima: \033[34mMASTER\033[m.')
print('-' * 37)

ano_de_nascimento = int( input('Qual é o seu ano de nascimento? '))

print('-' * 37)

ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento

print(f'O aleta tem {idade} ano(s)')

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'Categoria \033[34m{categoria}\033[m')
