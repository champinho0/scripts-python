#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pessoas in range (1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1: #esse primeiro if é para receber os primeiros valores
        maior = peso
        menor = peso
    else: #esse else vai comparar os valores depois do primeiro valor inserido.
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[32mO MAIOR peso é de {}\033[0m\n\033[31mO MENOR peso é de {}\033[0m'.format(maior, menor))
