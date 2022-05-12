# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.
ret1 = float(input('Digite um valor para reta: '))
ret2 = float(input('Digite um segundo valor para outra reta: '))
ret3 = float(input('Digite um terceiro valor para mais outra reta: '))
if (ret1 < ret2 + ret3) and (ret2 < ret1 + ret3) and (ret3 < ret1 + ret2):
    print('Ora, ora temos um triangulo')
else:
    print('As retas não podem formar um trinagulo :(')
