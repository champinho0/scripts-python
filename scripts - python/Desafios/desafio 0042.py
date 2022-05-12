#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
#– EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente - ESCALENO: todos os lados diferentes
ret1 = float(input('Digite o valor da primeira reta: '))
ret2 = float(input('Digete o valor da segunda reta: '))
ret3 = float(input('Digite o valor da terceira reta: '))
if (ret1 < ret2 + ret3) and (ret2 < ret1 + ret3) and (ret3 < ret1 + ret2):
    print('Os segmentos FORMAM um triângulo do tipo: ',end='')
    if (ret1 == ret2 == ret3):
        print('EQUILÁTERO')
    elif (ret1 == ret2 != ret3) and (ret1 == ret3 != ret2) and (ret2 == ret3 != ret1):
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('As retas informadas NÃO  formam um triângulo.')