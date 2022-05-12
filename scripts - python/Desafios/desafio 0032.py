#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Zé, que ano vc quer analisar? Para ficar facil parcerin, digite 0 se for o ano atual: '))
if ano == 0:
   ano = date.today().year #não é necessário, é apenas para dar uma brincada 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # o "!=" significa não igual
    print('O ano {} é um ano bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))