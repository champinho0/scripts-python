#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto – à vista no cartão: 5% de desconto – em até 2x no cartão: preço normal  – 3x ou mais no cartão: 20% de juros
preco = float(input('Qual é o valor do produto? '))
print('-=-'*20)
pgto = int(input('''FORMAS DE PAGAMENTO
[1] À VISTA DINHEIRO OU CHEQUE
[2] À VISTA NO CARTÃO
[3] ATÉ 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO
--> '''))
print('-=-'*20)
if pgto == 1:
    desc = (preco*0.10)
    nprec = preco - desc
    print('O novo valor do produto com o preço de R${}, será de R${}, com desconto de 10%'.format(preco, nprec))
elif pgto == 2:
    desc = (preco*0.05)
    nprec = preco - desc
    print('O novo valor do produto com o preço de R${}, será de R${}, com desconto de 5%'.format(preco, nprec))
elif pgto == 3:
    print('Não há descontos em pgtos em 2x no cartão, o preço continuará sendo R${}'.format(preco))
elif pgto == 4:
    nprec = (preco*0.20)+preco
    print('Para produtos parcelados 3x ou mais, sofre um acréscimo de 20% ao valor de R${}. O preço com acréscimo será de R${}'.format(preco, nprec))
else:
    print('Opção não encontrada, tente novamente')