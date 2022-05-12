#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
num = int(input('Digite um número entre 0 e 9999: '))
un = num // 1 % 10 #isso representa a dezena pq o numero é divido pelo modulo de 1%10, assim, sendo a unidade
dz = num // 10 % 10
ct = num // 100 % 10
mi = num // 1000 % 10
print('No número {}, temos como\n Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num, un, dz, ct, mi))