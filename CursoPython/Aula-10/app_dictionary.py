# Dicionários são coleções de Chave e Valor e seguem as regras dos Set´s

meses = {
    'Jan': 'Janeiro',
    'Feb': 'Fevereiro',
    'Mar': 'Março',
    'Apr': 'Abril',
    'May': 'Maio',
    'Jun': 'Junho',
    'Jul': 'Julho',
    'Aug': 'Agosto',
    'Set': 'Setembro',
    'Out': 'Outubro',
    'Nov': 'Novembro',
    'Dez': 'Dezembro',

}

print()
print(meses)
print()
print(meses['Jan'])
print()
print(meses['Jun'])
print()
'''print(meses['ABC'])
print()'''
print(meses.get('May'))
print()
print(meses.get('ABC')) # None => Não exite. Diferente se buscar algo que não existe somente pelo print
print()
print(meses.get('ABC', 'Valor Padrão se não existir o primeiro parâmetro.'))
print()
print(len(meses))
print()
