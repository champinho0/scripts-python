from time import sleep

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print (' A su média foi {:.2f}'.format(m))
if m >=6:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim, Estude mais!')