#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessária para pintá-la.
#Saiba que cada litro de tinta pinta uma area de 2m²
larg = int(input('Digite a largura da parede: '))
alt = int(input('Digite a altura da parede: '))
m2 = larg*alt
tint = m2/2
print('Serão necessários {} litros de tinta'.format(tint))