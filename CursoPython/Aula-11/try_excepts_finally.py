try:
    numero = int(input('\nDigite um número: '))
    print(f'\n{numero}')

except ZeroDivisionError:
    print('Divisão por zero não é possível!')

except ValueError:
    print('\nDigite um valor numérico válido!\n')

except:
    print('Erro inexperado!')

finally:
    print('\n\033[1;31mSempre executa!\n\033[m')