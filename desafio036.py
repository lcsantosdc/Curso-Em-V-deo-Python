from time import sleep

print('\033[1;97m~\033[m'*28)
print('\033[1;34m- EMPRÉSTIMO PARA IMÓVEIS -\033[m')
print('\033[1;97m~\033[m'*28)
valor_casa = float ( input ('Valor da casa: R$'))
salario = float ( input ('Salário do comprador: R$ '))
ano = int ( input ('Quantos anos de financiamento? '))
print('\033[1;31mAVALIANDO...\033[m')
sleep(1)
#vanual = valor_casa/ano

valor_mensal = (valor_casa / ano) / 12
porcento_salarial = (30 / 100) * salario

if valor_mensal > porcento_salarial:
    print('\033[31m=\033[m'*18)
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')
    print('\033[31m=\033[m'*18)
    print(f'Você não pode financiar essa casa.')
    print('\033[1;97m~\033[m'*28)
else:
    print('\033[32m=\033[m'*20)
    print('\033[32mEMPRÉSTIMO APROVADO!\033[m')
    print('\033[32m=\033[m'*20)
    print('-'*64)
    print(f'DADOS:\nValor do imóvel: R${valor_casa:.2f} \nVocê irá pagar R${valor_mensal:.2f} por mês. Terá um total de {ano * 12} \033[4mMESES\033[m. \nTotal de parcelas anuais: R${valor_casa / ano:.2f}')
    print('-'*64)
