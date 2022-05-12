#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
salario = int(input('Olá, digite o valor do seu salário: R$ '))
casa = int(input('Digite o valor da casa que deseja comprar: '))
prest = int(input('Digite a quantidade de anos em que deseja parcelar o casebre: '))
porcent = salario * 0.30
porcent2 = casa/(prest*12)
if porcent2 > porcent:
    print('\033[0:31:40mEMPRESTIMO NEGADO!\033[m \nO valor das prestações será de {:.2f} e você pode compromoter somente {:.2f}, por prestação.'.format(porcent2,porcent))
else:
    print('\033[0:32:40mEMPRESTIMO APROVADISSIMO!\033[m\nParabéns, você foi pré-aprovado em nossa simulação!')