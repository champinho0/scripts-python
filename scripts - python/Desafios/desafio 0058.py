# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('Sou o computador, pensei em número entre 0 e 10 aqui....\nSerá que você consegue adivinhar qual é?')
computador = randint(0,10)
acertou = False
palpites = 0
while not acertou:
   jogador = int(input('Escolha um número entre 0 e 10: '))
   palpites = palpites + 1
   if jogador == computador:
        acertou = True
   else:
       if jogador > computador:
           print('\nO número escolhido pelo computador é MENOR... Tente de novo!')
       elif jogador < computador:
           print('\nO número escolhido pelo computador é MAIOR... Tente de novo!')
print('\n\nParabéns! O número era {}, você acertou com {} tentativas.'.format(computador,palpites))