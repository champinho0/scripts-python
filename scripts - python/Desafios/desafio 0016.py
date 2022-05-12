#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import floor
n = float(input('Digite um número real: '))
num = floor(n)
print('O número real na sua porção inteira é:',num)