D = int(input("Total de dias alugado: "))
K = float(input("Total de KM rodado: "))
diaria = 60 * D
km = 0.15 * K
print(f"De acordo com o dados, o aluguel do veículo custará R${diaria + km:.2f}")   
