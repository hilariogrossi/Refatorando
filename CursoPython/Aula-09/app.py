"""i = 1

while i <= 10:
    print(i)
    i += 1

print()
print('Terminou o while')
print()

print(f'Esse é o valor final de "i" o qual ele não passou pelo while => {i}.')
print()"""

'''pessoas = ['Hilário', 'Patrícia', 'Gabriel', 'Pedro Henrique']

for nome in pessoas:
    print(nome)'''

'''canal = 'Refatorando'

for letra in canal:
    print(letra)'''

'''for i in range(20): # São três parâmetros, porém somente a parada final é obrigatória.
    print(i) # Nesse caso a impressão vai do 0 ao 19 (20 - 1)'''

'''for i in range(7, 20): # Nesse caso irá começar no 7 e vai parar no 19
    print(i)'''

'''for i in range(6, 20, 2): # Nesse caso irá começar no 6, vai pular de 2 em 2 e vai parar no 18
    print(i) # O pulo, step, vai como último parâmetro'''

'''pessoas = ['Hilário', 'Patrícia', 'Gabriel', 'Pedro Henrique']'''

'''for i in range(len(pessoas)):
    #print(i)
    #print(pessoas[i])
    print(i, pessoas[i])
'''

'''for i in range(5):
    if i == 0:
        print('Primeira linha')
    
    else:
        print(f'Outras linhas - {i}')'''

matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7 ,8, 9],
    [0],

]

for linha in matriz_numeros:
    print('*' * 5)
    for coluna in linha:
        print(coluna)
