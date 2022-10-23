salario = float(input('Qual é o salário do funcionário? R$'))
print(f'O seu novo reajuste com 10% de aumento passa a ser R${salario+((10/100)*salario):.2f}'if salario >= 1250.00 else f'O seu novo reajuste com 15% de aumento passa a ser R${salario+((15/100)*salario):.2f}')
