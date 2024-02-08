# Colletions (Listas e Tuples)

familia = ['Hilário', 'Patrícia', 'Gabriel', 'Pedro']

print(f'\nA lista família completa é: {familia}.\n')
'''print(f'O primeiro nome da lista família é: {familia[0]}.\n')
print(f'O Segundo nome da lista família é: {familia[1]}.\n')
print(f'O Terceiro nome da lista família é: {familia[2]}.\n')
print(f'O quarto nome da lista família é: {familia[3]}.\n')'''

i = 1

for nome in familia:
    print(f'O {i}° nome da lista família é: {nome}.\n')

    i += 1

j = 4
i_2 = -1

print(f"{'*' * 50}\n")

for _ in familia:
    print(f'O {j}° nome da lista família é: {familia[i_2]}.\n')

    j -= 1
    i_2 -= 1

print(f"{'*' * 50}\n")

print(f'{familia[2:]}\n')

print(f"{'*' * 50}\n")

# Modificando valores
print(familia)
familia[3] = 'Pedro Henrique'
print(familia)

print(f"\n{'*' * 50}\n")
