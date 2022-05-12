#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
# 10 primeiros termos dessa progressão.
termo = int(input('Digite o primeiro termo para a PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razao #formula matematica para descobrir o enesimo termo da pa
for c in range(termo, decimo + razao, razao): #termo = inicio do contador// decimo+razao = ultimo termo// razao = passo
    print('{}'.format(c), end=' -> ')