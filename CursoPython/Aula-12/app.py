# estrutura do open => r = read / leitura a = append / incrementar
# w = write / escrever x = create / criar arquivo r+ = leitura + escrita

# arquivo = open('CursoPython/Aula-12/test.txt', 'r')

'''arquivo = arquivo.readable()
print(arquivo)''' # Para saber se o arquivo pode ser lido (True or False)

'''arquivo = arquivo.read()
print(arquivo)''' # Lê o arquivo todo

'''arquivo = arquivo.readline()
print(arquivo)''' # Lê a primeira linha do arquivo

'''print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())'''

'''arquivo.close()''' # Só funciona quando se abre o arquivo e não tem criação de variáveis após a abertura.

'''lista = arquivo.readlines()
print(lista)'''

'''arquivo = open('CursoPython/Aula-12/test.txt', 'a')

arquivo.write('C\n')
arquivo.write('C++\n')
arquivo.write('Terraform\n')'''

'''arquivo = open('CursoPython/Aula-12/test.txt', 'w')''' # Apaga todo arquivo e reescreve o que quiser

# Melhor usar 'a' append

# Para criar um arquivo novo pode-se usar o 'w'
'''arquivo = open('CursoPython/Aula-12/create_file.txt', 'w')

arquivo.write('C\n')
arquivo.write('C++\n')
arquivo.write('Terraform\n')'''

# Exclusão de arquivo
'''import os

if os.path.exists('CursoPython/Aula-12/remove.txt'):
    os.remove('CursoPython/Aula-12/remove.txt')

else:
    print('\nO arquivo não existe!\n')'''

# Exclusão de pasta (Diretório)
'''import os

if os.path.exists('CursoPython/Aula-12/nova_pasta'):
    os.rmdir('CursoPython/Aula-12/nova_pasta')

else:
    print('\nA pasta (diretório) não existe!\n')'''

