#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = str(input('Digite o nome de um aluno: '))
aluno2 = str(input('Digite o nome de um aluno: '))
aluno3 = str(input('Digite o nome de um aluno: '))
aluno4 = str(input('Digite o nome de um aluno: '))
sorteio = [aluno1,aluno2,aluno3,aluno4] #o armazenamento das informações tem que estar em modulo
shuffle(sorteio)
print('A ordem de apresentação é: ',sorteio)