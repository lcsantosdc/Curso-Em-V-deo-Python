p = float(input("Preço do produto: R$"))
d = float(input("Desconto: "))
desc = (d/100)*p
print(f"Com {d}% de desconto o seu poduto fica com o novo valor de R${p-desc}")
