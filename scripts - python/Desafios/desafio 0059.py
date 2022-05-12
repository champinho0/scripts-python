#Crie um programa que leia dois valores e mostre um menu na tela: 1  somar  2 multiplicar 3  maior  4
# novos números 5  sair do programa Seu programa deverá realizar a operação solicitada em cada caso.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
menu = 0
while menu != 5:
    print('-=-'*10)
    print('''DIGITE UMA OPÇÃO
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números 
    [5] Sair do Programa
    ''')
    menu = int(input('>>>> Digite a opção desejada: '))
    print('-=-' * 10)
    if menu == 1:
        soma = num1 + num2
        print('\nA soma de {} + {} é {}\n'.format(num1,num2,soma))
    elif menu == 2:
        mult = num1 * num2
        print('\nA multiplicação entre {} x {} é {}\n'.format(num1, num2, mult))
    elif menu == 3:
        if num1 > num2:
            print('\nO número {} é maior que o número {}\n'.format(num1,num2))
        else:
            print('\nO número {} é maior que o número {}\n'.format(num2, num1))
    elif menu == 4:
        print('Informe novos números')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif menu == 5:
        print('\n>>>Você finalizou o programa. Até logo!<<<')



