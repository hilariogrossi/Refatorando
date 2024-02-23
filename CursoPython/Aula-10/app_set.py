# Lista desordenada, consegue-se colocar e tirar valores, mas não consegue-se 
# modificar valores e não aceita valores duplicados.

frutas = {'Maçã', 'Laranja', 'Abacate'}
print(frutas) # Os valores não estarão na mesma ordem sempre...

frutas.add('Pêra')
print(frutas)

frutas.remove('Maçã')
print(frutas)

frutas.pop() # Remove o último valor, mas não saberemos qual é o último.
print(frutas)

set_1 = {'Maçã', 'Laranja', 'Abacate'}
set_2 = {1, 2, 3, 4, -4, -3, -2, -1}
set_3 = {True, False, False, True}
set_4 = {'Hilário', 53, True}

print(f'\nO set-1 é {set_1},\nO set-2 é {set_2},\nO set-3 é {set_3},\nO set-4 é {set_4}.\n')

