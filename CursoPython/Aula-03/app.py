num_1 = 5
num_2 = 3.5

print(type(num_1))
print(type(num_2))

print()

a = float(num_1)
print(a) # float

b = int(num_2)
print(b) # inteiro (int), mas pegou somente a cada do inteiro e sem a casa decimal.

print()

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1 ** num_2)
print(num_1 // num_2)
print(num_1 % num_2)

print()

print(3 + 5 * 7 + 3)
print((3 + 5) * (7 + 3))

print()

print(abs(-15)) # valor absoluto. Sem o negativo

print()

print(pow(3, 3)) # exponenciação

print()

print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))

print()

print(round(8.3)) # arredondamento por aproximação
print(round(8.4)) # arredondamento por aproximação
print(round(8.5)) # arredondamento por aproximação = Arredonda para baixo
print(round(8.6)) # arredondamento por aproximação
print(round(8.7)) # arredondamento por aproximação

print()

import math

print(math.floor(8.3)) # arredondamento para baixo
print(math.floor(8.4)) # arredondamento para baixo
print(math.floor(8.5)) # arredondamento para baixo
print(math.floor(8.6)) # arredondamento para baixo
print(math.floor(8.7)) # arredondamento para baixo

print()

print(math.ceil(8.3)) # arredondamento para cima
print(math.ceil(8.4)) # arredondamento para cima
print(math.ceil(8.5)) # arredondamento para cima
print(math.ceil(8.6)) # arredondamento para cima
print(math.ceil(8.7)) # arredondamento para cima

print()

print(int(math.sqrt(144))) # raiz quadrada. int porque o resultado é float. se quiser.

print()
