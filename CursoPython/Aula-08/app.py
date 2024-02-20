# Operadores lógicos ==> or, and e not

'''tenho_sede = True

if tenho_sede:
    print('\nBeber água!\n')

print('Vida que segue...\n')'''

'''esta_frio = False

if esta_frio:
    print('\nVestir um casaco!\n')

else:
    print('\nVestir uma camiseta.\n')'''

tenho_sede = True
tenho_fome = False

'''if tenho_sede or tenho_fome:
    print('\nVou à cozinha...\n')

else:
    print('\nFico de boa...\n')

if tenho_sede and tenho_fome:
    print('\nVou à cozinha...\n')

else:
    print('\nFico de boa...\n')'''

estou_em_dieta = False


'''if tenho_sede and tenho_fome:
    print('\nVou à cozinha fazer um sanduíche e tomar um suco...\n')

elif tenho_sede and not tenho_fome:
    if estou_em_dieta:
        print('\nVou à cozinha tomar água...\n')
    
    else:
        print('\nVou à cozinha tomar um suco...\n')

elif not tenho_sede and tenho_fome:
    print('\nVou à cozinha fazer um sanduíche...\n')

else:
    print('\nFico de boa...\n')'''

# Operadores de comparação

num_1 = 5
num_2 = 32

if num_1 == num_2:
    print(f'\nO número {num_1} é igual ao número {num_2}.\n')

elif num_1 > num_2:
    print(f'\nO número {num_1} é MAIOR que o número {num_2}.\n')

elif num_1 < num_2:
    print(f'\nO número {num_1} é MENOR que o número {num_2}.\n')

if num_1 <= num_2:
    print(f'\nO número {num_1} é igual ou MENOR que o número {num_2}.\n')

elif num_1 >= num_2:
    print(f'\nO número {num_1} é igual ou MAIOR que o número {num_2}.\n')

if num_1 != num_2:
    print(f'\nO número {num_1} é diferente do número {num_2}.\n')


