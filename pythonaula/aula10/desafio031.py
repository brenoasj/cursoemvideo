# aula10

d = int(input('Qual a distância da viagem? '))
p1 = d * 0.5
p2 = d * 0.45
if d <= 200:
    print('A viagem custará R${:.2f}' .format(p1))
else:
    print('A viagem custará R${:.2f}'.format(p2))

#É possível escrever a condição em uma linha

