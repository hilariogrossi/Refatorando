# string -> texto
minha_string = 'qualquer texto'
print(type(minha_string))
print(minha_string)
print('minha_string')
print(f'{minha_string}')
print(f'Concatenar {minha_string} em string')

print()

print(minha_string.upper())
print(minha_string.lower())
print(minha_string.capitalize())
print(minha_string.isupper())
print(minha_string.islower())

print()

print(minha_string.strip()) # remove espaços antes e depois da string

print()

print(minha_string.replace("q", 'Q')) # troca algum parâmetro no texto
print(minha_string.replace("q", 'Q', 1)) # troca algum parâmetro no texto na 1a. posição

print()

print(len(minha_string)) # retorna a quantidade de caracteres tem a string

print()

print(minha_string[4]) # pegando o caracter pela posição na string [0, 1, 2, ...]
print(minha_string[2:5]) # pegando os caracters num intervalo
print(minha_string[-4:-1]) # pegando os caracters num intervalo

print()

print(minha_string.index('u')) # retorna pelo index do caracter pedido
print(minha_string.index('texto')) # retorna pelo index do caracter pedido

print()

x = 'texto' in minha_string
print(x)

y = 'texo' in minha_string
print(y)

print()

minha_string_varias_linhas = '''
linha 1
linha 2
linha 3
'''
print(minha_string_varias_linhas)

print()

minha_string_varias_linhas_caracter_de_escape = 'linha 1\nlinha 2\nlinha 3'
print(minha_string_varias_linhas_caracter_de_escape)

print()

minha_string_aspas = 'Adiciona aspas \" \" no texto.'
print(minha_string_aspas)

print()

