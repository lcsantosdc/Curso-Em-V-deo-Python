#num = str(input('Digite um valor entre o e 9999: '))
#print(f'Milhar: {num[0]} \nCentena: {num[1]} \nDezena: {num[2]} \nUnidade: {num[3]}')

num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'milhar: {m} \ncentena: {c}\ndezena: {d}\nunidade: {u}')
