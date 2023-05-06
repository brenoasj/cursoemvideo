# aula10

print('Diga o comprimento de 3 retas e veremos se formam um triângulo.')
a = int(input('Qual a primeira? '))
b = int(input('Qual a segunda? '))
c = int(input('Qual a terceira? '))
if a + b > c and a + c > b and b + c > a:
    print('As medidas formam um triângulo.')
else:
    print('Não é possível formar um triângulo.')


