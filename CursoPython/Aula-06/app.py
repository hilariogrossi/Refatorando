# Colletions (Listas)

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

print(f"\n{'*' * 100}\n")

familia.extend(['José Antonio', 'Ana Maria'])

print(familia)

print(f"\n{'*' * 100}\n")

familia.append('Dori')

print(familia)

print(f"\n{'*' * 100}\n")

familia.insert(6, 'Clarice')

print(familia)

print(f"\n{'*' * 100}\n")

familia.pop()

print(familia)

print(f"\n{'*' * 100}\n")

familia.remove('Clarice')

print(familia)

print(f"\n{'*' * 100}\n")

# familia.clear()

# print(familia)

# print(f"\n{'*' * 100}\n")

print('Busca por índices:')
print(f'O nome José Antonio está no índice: {familia.index("José Antonio")}')
print(f'O nome Hilário está no índice: {familia.index("Hilário")}')

print(f"\n{'*' * 100}\n")

print('Contando quantos itens possui a lista:')
print(f'A quantidade de Gabriel na lista é: {familia.count("Gabriel")}')
print(f'A quantidade de Pedro Henrique na lista é: {familia.count("Pedro Henrique")}')
print(f'A quantidade de Clarice na lista é: {familia.count("Clarice")}')

print(f"\n{'*' * 100}\n")

idade_familia = [53, 56, 24, 22]
print('Colocando o nome com a referida idade:')
familia.pop()
familia.pop()

i = 0

for nome in familia:
    print(f'O (A) {nome} tem {idade_familia[i]}.')

    i += 1

print(f"\n{'*' * 100}\n")

print('Lista de idade da família:')
print(idade_familia)

print()

print('Ordenando a lista de idade:')
idade_familia.sort()
print(idade_familia)

print()

print('Ordenando a lista de família de trás para frente:')
familia.reverse()
print(familia)

print()

print('Ordenando a lista de idade de trás para frente:')
idade_familia.reverse()
print(idade_familia)

print()

print('Ordenando a lista de idade ORDENADA de trás para frente:')
idade_familia.sort()
idade_familia.reverse()
print(idade_familia)

print(f"\n{'*' * 100}\n")

