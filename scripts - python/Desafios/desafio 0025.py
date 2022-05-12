# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite o nome completo de uma pessoa: ')).upper().strip()
print(nome.count('SILVA'))