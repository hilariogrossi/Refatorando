'''def big_mac():
    print('\nSanduiche Big Mac!\n')

big_mac()'''

def fazer_big_mac(nome):
    print(f'\nO Sanduiche Big Mac do {nome} está pronto!\n')


def fazer_batata(tamanho):
    print(f'\nA batata {tamanho} está pronta!\n')


def refrigerante(tipo, tamanho):
    print(f'\nO refrigerante {tipo} do tamanho {tamanho} está pronto!\n')

'''fazer_big_mac('Hilário')
fazer_batata('Grande')
refrigerante('Soda', 'Grande')'''

def fazer_combo_big_mac(nome, tamanho, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho)
    refrigerante(tipo_refri, tamanho_refri)


# fazer_combo_big_mac('Hilário', 'grande', 'Sprite', 'grande')

def soma_num(num_1, num_2):
    print(f'\nO resultado da soma dos números {num_1} e {num_2} é ', end='')
    return num_1 + num_2

resultado = soma_num(15, 20)

print(f'{resultado}.\n')


def maior_num(lista_num):
    lista_num.sort() # ordena
    lista_num.reverse() # coloca o maior primeiro
    maior_num = lista_num[0] # pega o primeiro que por consequência será o maior número

    return maior_num

lista = [20, 100, 4890905, 5339720, 236000, 5548]

maior_numero = maior_num(lista)

print(f'O maior número da lista {lista} é {maior_numero}.\n')
