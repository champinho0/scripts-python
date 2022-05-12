#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$3,27
din = float(input('Digite quanto tem na carteira: R$ '))
dol = float(din/3.27)
print('Você possui na carteira US$ {} '.format(dol))