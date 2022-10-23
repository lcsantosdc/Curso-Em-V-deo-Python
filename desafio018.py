from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
print(f'O ângulo de {ang}° tem o SENO de {sin(radians(ang)):.2f} \nO ângulo de {ang}° tem o COSSENO de {cos(radians(ang)):.2f} \nO ângulo de {ang}° tem a TANGENTE de {tan(radians(ang)):.2f}')
