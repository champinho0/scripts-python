#Desafio 04
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n1 = input('Digite algo: ')
print('O que foi digitado é um número {}, o que foi digitado é uma letra {}, o que foi digitado é um caractere alfanumerico {} e o tipo primitivo é {}'.format(n1.isnumeric(),n1.isalpha(), n1.isalnum(),type(n1)))