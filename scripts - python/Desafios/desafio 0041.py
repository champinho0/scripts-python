#041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM – Até 14 anos: INFANTIL – Até 19 anos: JÚNIOR – Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
ano = int(input('Digite o seu ano de nascimento: '))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('A categoria do atleta será a MIRIM.'.format(idade))
elif 9 > idade <= 14:
    print('A categoria do atleta será a INFANTIL.'.format(idade))
elif idade > 14 and idade <=19:
    print('A categoria do atleta será a JÚNIOR.'.format(idade))
elif 19 > idade <= 25:
    print('A categoria do atleta será a SÊNIOR.'.format(idade))
else:
    print('A categoria do atleta será a MASTER.'.format(idade))