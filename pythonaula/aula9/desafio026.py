# aula 9

frase = str(input('Diga uma frase: ')).strip().lower()
print('A letra A parece {} vezes na frase.' .format(frase.count('a')))
print('A primeira letra A apareceu na {}° posição.' .format(frase.find('a')+1))
print('A última letra A apareceu na {}° posição.' .format(frase.rfind('a')+1))



