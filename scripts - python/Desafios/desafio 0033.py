#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um número para ser comparado: '))
n2 = int(input('Digite mais número para ser comparado: '))
n3 = int(input('Ah fi, digita mais oto aí: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n2
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3:
    maior = n3
print('-=-'*20)
(print('Dus número que vc digitou, {} é o maior e {} é o menor'.format(maior, menor)))
print('-=-'*20)