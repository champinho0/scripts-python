#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número para ser convertido: '))
print('-=-'*18)
op = int(input('''Digite a opção desejada de conversão 
[1] Binário 
[2] Octal 
[3]Hexadecimal
--> '''))
if op == 1:
    print('O número {} em binário é: {}'.format(num,bin(num)[2:])) #O [2:] é para fatiar a string, tirando os dois primeiros caracteres, pois, o python por padrão, mostra dois caracteres sem necessidades.
elif op == 2:
    print('O número {} em octal é: {}'.format(num,oct(num)[2:]))
elif op == 3:
    print('O número {} em hexadecimal é: {}'.format(num,hex(num)[2:]))
else:
    print('Opção não encontrada, tente novamente.')