#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
pag = int(input('Digite o salário do funcionário: '))
aum = float(pag*0.15) + pag
print ('O novo salário será de {}'.format(aum))

