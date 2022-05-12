#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = int(input('Digite o salário do funcionário: '))
if salario > 1250:
    novo = ((salario * 0.10) + (salario))
    print('Patrozin tá bão e te deu um amumento de 10%, seu novo salário será de {} '.format(novo))
else:
    novo = ((salario * 0.15 ) + (salario))
    print('Patrozin ficou maluco e te deu um amumento de 15%, seu novo salário será de {} '.format(novo))