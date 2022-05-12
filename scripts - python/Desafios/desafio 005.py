#Faça um programa que leia um numero inteiro e mostre na tela seu
#sucessor  e seu antecessor
n = int(input('Digite um número: '))
suc = n + 1
ant = n - 1
print('O sucessor de {} é {} e o seu atntecessor é {}.'.format(n,suc,ant))