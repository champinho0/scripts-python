# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite o seu nome completo: ')).strip().upper()
lista = nome.split()
print('O seu primeiro nome é: ',lista[0])
print('O seu último nome é: ', lista[len(lista)-1])