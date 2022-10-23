v = float(input('Qual a velocidade atual do veículo? '))
print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h! \nA multa custará R${7*(v-90):.2f}\nTenha um ótimo dia! Dirija com segurança!' if v > 90 else'Tenha um ótimo dia! Dirija com segurança!')
