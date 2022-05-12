#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velo = int(input('Digite a velocidade do carro: '))
if (velo > 80):
    multa = (velo-80) * 7
    print('Parcerin, você será multado em R$7,00 por KM excedido.\nA sua multa será de: R${:.2f}'.format(multa))
else:
    print('Boa mlkin, continue assim, respeite as leis, beba muita água e fé nas crianças.')