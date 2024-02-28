import tools

print(f'\nA constante PI tem valor de \033[1;32m{tools.PI}\033[m.\n')
print(f'\nA gravidade do planeta Terra é \033[1;33m{tools.GRAVITY}\033[m m/s².\n')

print(f'\n{tools.get_extensions('test.txt')}\n')
print(f'\n{tools.highest_number([21, 10, 1970])}\n')
