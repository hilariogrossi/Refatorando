from datetime import date

nome = input('\nDigite seu nome: ')
idade = int(input(f'\nQual a sua idade {nome}? '))
aniversario = input(f'\n{nome}, você já fez aniversário esse ano? [S/N] ').upper()

corrente_ano = date.today().year

if aniversario == 'S':
    corrente_ano = corrente_ano 

elif aniversario == 'N':
    corrente_ano -= 1

nascimento = corrente_ano - idade

print(f'\nSeu nome é {nome}, você tem {idade} anos e você nasceu no ano de {nascimento}!\n')
