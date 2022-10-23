valorproduto = float(input('Qual é o valor das compras: '))

print('MENU DE PAGAMENTOS:')
print('''
[ 1 ] à vista no dinheiro ou cheque 
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    total = valorproduto - (valorproduto * (10/100))
    print(f'À vista no dinheiro com 10% de desconto:\nPreço original do produto R${valorproduto:.2f} com desconto = R${total:.2f}')
elif opcao == 2:
    total = valorproduto - (valorproduto * (5/100))
    print(f'À vista no cartão com 5% de desconto:\nPreço original do produto R${valorproduto:.2f} com 5% de desconto = R${total:.2f}')
elif opcao == 3:
    total = valorproduto / 2
    print(f'2x vezez no cartão:\nPreço original R${valorproduto:.2f}. Com parcelas de R${total:.2f} mensais')
elif opcao == 4:
    total = valorproduto + (valorproduto * (20/100))
    parcelas = int(input('Digite as parcelas: '))
    valorparcelado = total / parcelas
    print(f'{parcelas}x no cartão com 20% de juros:\nO preço original R${valorproduto:.2f} passa a ser R${total:.2f}. Com parcelas de R${valorparcelado:.2f} mensais')
else:
    print('Opção INVÁLIDA')
