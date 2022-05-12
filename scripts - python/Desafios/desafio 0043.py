#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso – Entre 18,5 e 25: Peso Ideal – 25 até 30: Sobrepeso – 30 até 40: Obesidade – Acima de 40: Obesidade Mórbida
peso = float(input('Digite seu PESO em Kg: '))
altura = float(input('Digite a sua ALTURA em m: '))
imc = float(peso / (altura ** 2))
if imc <18.5:
    print('Seu IMC é de {:.2f}. CUIDADO, VOCÊ ESTÁ ABAIXO DO PESO!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f}. PARABÉNS, Vc está no PESO IDEAL!'.format(imc))
elif 25 <= imc <40:
    print('Seu IMC é de {:.2f}. CUIDADO, vc está na faixa de OBESIDADE!'.format(imc))
else:
    print('Seu IMC é de {:.2f}. MUITO CUIDADO você está na faixa de OBESIDADE MÓRBIDA.'.format(imc))

