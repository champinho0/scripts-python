#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
# uma mensagem no final, de acordo com a média atingida
nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota + nota2)/2
if media <5:
    print('Sua media foi de: {}. Ih rapaz, tá REPROVADO'.format(media))
elif 7 > media >= 5: #esse é um dos jeitos python de se fazer
    print('Sua media foi de: {}. Você irá pegar uma RECUPERAÇÃO aí de boa.'.format(media))
elif media >= 7:
    print('Sua media foi de: {}. Você foi Aprovadissímo!!'.format(media))