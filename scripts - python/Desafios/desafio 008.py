#Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milímetros.
mt = float(input('Digite o valor em metros: '))
cm =float(mt*100)
mm =float(mt*1000)
print('O valor de {}mt em centímetros é de: {}cm \nO valor de {} para milímetros é de: {}mm'.format(mt,cm,mt,mm))