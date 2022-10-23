#s = float(input("Salário do funcionário R$"))
#a = int(input("Aumento: "))
#a2 = a / 100
#a3 = a2 + 1
#print(f"com {a}% de aumento o salário passa a ser R${s*a3:.2f}")

s = float(input("Salário do funcionario R$ "))
a = float(input("Aumento: "))
novo = s + (s * a / 100)

print(f"Salário inicial: R${s} \nCom {a}% de reajuste: R${novo:.2f}")
