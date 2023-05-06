# aula10

s = float(input('Qual o valor do seu salário? '))
a1 = s * 10/100
a2 = s * 15/100
if s > 1250.00:
    print('Seu salário teve um aumento de R${:.2f} e agora será de R${:.2f}' .format(a1, a1 + s))
else:
    print('Seu salário teve um aumento de R${:.2f} e agora será de R${:.2f}' .format(a2, a2 + s))

#ou

#s = float(input('Qual o valor do seu salário? '))
#if s <= 1250:
#    novo = s + (s * 15/100)
#else:
#    novo = s + (s * 10/100)
#print('Seu salário teve um aumento de R${:.2f} e agora será de R${:.2f}' .format(s, novo))



