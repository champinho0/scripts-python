#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
import sys
y = date.today().year #pegar o ano atual
nasc = int(input('Digite o ano de nascimento: '))
sexo = str(input('Digete o seu sexo.\n[M] Masculino\n[F] Feminino\n--> ')).upper()
idade = (y - nasc)
print('=-='*15)
print('Você é do sexo {}, nasceu em {} e tem/terá {} anos em {}'.format(sexo,nasc, idade, y))
print('=-='*15)
if sexo == "F":
    print('O alistamento não é obrigatório para você')
    sys.exit()
elif idade == 18:
    print('Você é do sexo masculino e o alistamento é obrigátorio')
    print('Amiguinho, está na hora do alistamento, aguardamos você recrutinha!')
elif idade < 18:
    saldo = (18 - idade)
    print('->Amiguinho, não está na hora de se alistar, mas esperemos você em breve!\n-->Falta {} anos para você se alistar.'.format(saldo))
    ano = y + saldo
    print('--->Seu alistamento será em: {}'.format(ano))
elif idade > 18:
    saldo = (idade - 18)
    print('->Amiguinho, já passou do ano de você se alistar, alista logo mané, estamos te aguardando!\n-->Você está atrasado em {} anos'.format(saldo))
    ano = y - saldo
    print('--->Seu alistamento foi em {}'.format(ano))
