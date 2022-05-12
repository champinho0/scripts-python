#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
prec = float(input('Digite o valor do produto: '))
predesc = prec -(prec*5/100)
print('O produto com desconto custa {}'.format(predesc))