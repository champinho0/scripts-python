#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número: '))
div = num % 2
if  (div==1):
    print('O número {}, é um número ímpar'.format(num))
else:
    print('O número {}, é um número par'.format(num))
