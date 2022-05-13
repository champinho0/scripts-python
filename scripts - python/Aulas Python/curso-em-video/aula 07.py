n1 = int(input('Digite Uma valor: '))
n2 = int(input(('Outro valor: ')))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {},\no produto é {} e a\ndivisão é {:.3f}'.format(s,m,d), end=' aoba')
print('\nDivisão inteira {} e \npotência {}'.format(di,e))