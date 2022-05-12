#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for pessoa in range (1,8):
    ano = int(input('Digite a data de nascimento da {}ª pessoa: '.format(pessoa)))
    if anoatual - ano >=18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Das 7 pessoas analisadas, \033[32m{} antigiram a maioridade.\033[0m\nE \033[31m{} NÃO antigiram a maioridade.\033[0m'.format(maior, menor))
