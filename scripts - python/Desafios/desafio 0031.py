#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = int(input('Qual é a distância da viagem? '))
if  (dist <= 200):
    prec = float(dist * 0.50)
else:
   prec = float(dist * 0.45)
print('A viagem terá um custo de R${}'.format(prec))

# ou pode-se usar:
# prec = dist * 0.50 if dist <= 200 else dist * 0.45