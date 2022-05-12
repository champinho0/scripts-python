from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
nome = str(input('Digite o seu nome: ')).upper()
print('-='*12)
jogador = int(input('''Suas opções
=-=-=-=-=-=-=
[0] PEDRA
[1] PAPEL
[2] TESOURA
=-=-=-=-=-=-=
Qual a sua jogada? '''))
print('-='*12)
print('JO')
sleep(0.25)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.25)
print('A CPU jogou {}'.format(itens[cpu]))
print('O {} jogou {}'.format(nome, itens[jogador]))
print('-='*12)
if cpu ==0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('PERDEU BURRÃO!')
    elif jogador == 2:
        print('BOA JEGUE, GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif cpu == 1:
    if jogador == 0:
        print('BOA JEGUE, GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('PERDEU BURRÃO!')
    else:
        print('JOGADA INVÁLIDA!')
elif cpu ==2:
    if jogador == 0:
        print('PERDEU BURRÃO!')
    elif jogador == 1:
        print('BOA JEGUE, GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
else:
    print('Você é tão burrão que não consegue colocar uma opção válida. Tenta aí de novo de boa.')