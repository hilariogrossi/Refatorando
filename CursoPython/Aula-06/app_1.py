familia = ['Hilário', 'Patrícia', 'Gabriel', 'Pedro']
idade_familia = [53, 56, 24, 22]

familia_2 = familia.copy()

print(f"\n{'*' * 100}")

print('Removendo o nome "Hilário" da lista original familia.')
familia.remove('Hilário')
print(f'Imprimindo a lista com o nome "Hilário" removido: {familia}')

print()

print('Como a familia_2 foi uma cópia primária de familia (antes de remover "Hilário") ela ainda está completa.')
print(familia_2)

print(f"\n{'*' * 100}\n")
