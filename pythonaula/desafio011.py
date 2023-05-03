# Faça um programa que leia a largura altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta  pinta uma área de 2m².

a = float(input('Qual a altura da parede?'))
l = float(input('Qual a largura da parede?'))
print('A área da parede é de {:.2f}m² e serão necessários {}litros de tinta para pintá-la' .format(a*l, (a * l)/2))
print(f'A área da parede é de {a*l:.2f}m² e serão necessários {(a * l)/2}litros de tinta para pintá-la')