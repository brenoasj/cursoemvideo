# aula10

v = float(input('Qual a velocidade do veículo? '))
multa = 7 * (v - 80)
if v > 80:
    print('O veículo exedeu o limite de 80km/h e será multado em R${:.2f}' .format(multa))
print('Boa viagem, dirija com segurança.')


