#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep #o sleep faz o programa ter uma pequena espera
aleatorio = (random.randrange(0,5))
print('-=-'* 20)
num =  int(input('Tente adivinhar o meu número: '))
print('-=-'* 20)
print('Processando menô, calma aí...')
sleep(3) #aqui terá uma espera de 3seg
if aleatorio == num:
    print('Uau você acertou, és o brabo demais')
else:
    print('ERROU! O número que eu pensei foi {}\nContinue tentando, uma hora vc acerta Zé.'.format(aleatorio))
