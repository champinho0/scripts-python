#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior – O segundo valor é maior – Não existe valor maior, os dois são iguais
num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num > num2:
    print('O primeiro número {}, é MAIOR que o segundo número {}'.format(num,num2))
elif num2 > num:
    print('O segundo número {}, é MAIOR que o primeiro número {}'.format(num2,num))
else:
    print('O primeiro número {}, é IGUAL ao segundo número {}'.format(num,num2))
