#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número qualquer: '))
tot = 0
for c in range(1, num +1):
    if num % c==0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end =' ')
print('\nO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('\nPor isso ele É primo!')
else:
    print('Por isso ele NÃO é primo')
