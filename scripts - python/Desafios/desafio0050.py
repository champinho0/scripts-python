#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n%2==0:
        soma = soma + n #soma + n, pois o quando o programa reinicia ele vai estar gravado com o último valor, se deixar soma= n + n, só vai mostrar os dois últimos valores
        cont = cont + 1
print('Você informou {} número pares e a  soma desses números pares é igual {}'.format(cont,soma))