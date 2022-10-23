n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#listn = [n1, n2, n3]
#print(f'O número {min(listn)} é menor. \nO número {max(listn)} é maior.')

if n1 < n2 and n1 < n3:
    print(f'O número {n1} é menor.')
if n2 < n1 and n2 < n3:
    print(f'O número {n2} é menor.')
if n3 < n1 and n3 < n2:
    print(f'O número {n3} é menor.')
if n1 > n2 and n1 > n3:
    print(f'O número {n1} é maior.')
if n2 > n1 and n2 > n3:
    print(f'O número {n2} é maior.')
if n3 > n1 and n3 > n2:
    print(f'O número {n3} é maior.')
