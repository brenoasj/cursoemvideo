# aula 9

nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.split()
print(nome.upper())
print(nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print(f'Seu primeiro nome tem {len(nome1[0])} letras')

# por alguma razão o código não rodou usando: print(f'{len(nome) - nome.count(' ')}')
# em vez de usa a variável nome1 poderia utilizar nome.find(' ')