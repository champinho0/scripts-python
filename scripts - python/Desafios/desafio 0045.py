#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 3)
op = int(input('''Suas opções
=-=-=-=-=-=-=
[1] PEDRA
[2] PAPEL
[3] TESOURA
=-=-=-=-=-=-=
Qual a sua jogada? '''))
sleep(0.25)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.25)
print('PO')
sleep(1)
if op == 1 and maquina == 1:
    print('''-=-=-=-
    EMPATE
a maquina escolheu{}'''.format(itens[maquina]))
elif op == 1 and maquina == 2:
        print ('''-=-=-=-
        VOCÊ PERDEU :(
a maquina escolheu {}'''.format(itens[maquina]))
elif op == 1 and maquina == 3:
    print('''-=-=-=-
    VOCÊ GANHOU :)
a maquina escolheu {}'''.format(itens[maquina]))
elif op == 2 and maquina == 1:
        print ('''-=-=-=-
        VOCÊ GANHOU :) :(
a maquina escolheu {}'''.format(itens[maquina]))
elif op == 2 and maquina == 2:
        print ('''-=-=-=-
        EMPATE :(
a maquina escolheu {}'''.format(itens[maquina]))
elif op == 2 and maquina == 3:
        print ('''-=-=-=-
        VOCÊ PERDEU :(
a maquina escolheu {}'''.format(itens[maquina]))
elif op == 3 and maquina == 1:
        print ('''-=-=-=-
        VOCÊ PERDEU :(
a maquina escolheu {}'''.format(itens[maquina]))
elif op == 3 and maquina == 2:
        print ('''-=-=-=-
        VOCÊ GANHOU :)
a maquina escolheu {}'''.format(itens[maquina]))
elif op == 3 and maquina == 3:
        print ('''-=-=-=-
        EMPATE :(
a maquina escolheu {}'''.format(itens[maquina]))
else:
    print('Opção não encontrada, Tente novamente!')