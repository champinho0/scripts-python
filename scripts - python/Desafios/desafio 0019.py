#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
a1 = str(input('Digite o nome dos alunos: '))
a2 = str(input('Digite o nome dos alunos: '))
a3 = str(input('Digite o nome dos alunos: '))
a4 = str(input('Digite o nome dos alunos: '))
lista = (a1,a2,a3,a4)
sorteado = choice(lista)
print('O aluno sorteado foi: ',sorteado)