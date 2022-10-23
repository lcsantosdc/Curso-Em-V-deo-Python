soma_idade = 0
média_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
totmulher20 = 0

for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    média_idade = soma_idade / 4
    
    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_mais_velho = nome
    
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

    if sexo in 'F' and idade < 20:
        totmulher20 += 1
        
print(f'A média de idade do grupo é de {média_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_mais_velho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')