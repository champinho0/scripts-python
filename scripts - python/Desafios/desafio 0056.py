#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.
somaid = 0
maior = 0
nomemaior = ''
idadefem = 0
for pessoas in range(1,5):
    print('---- DADOS DA {}ª PESSOA ----'.format(pessoas))
    nome = str(input('NOME: '.format(pessoas))).strip()
    idade = int(input('IDADE: '.format(pessoas)))
    sexo = str(input('SEXO [M ou F]: '.format(pessoas))).upper().strip()
    somaid = somaid + idade
    if pessoas == 1 and sexo == 'M':
        maior = idade
        nomemaior = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nomemaior = nome
    if sexo == 'F' and idade < 20:
        idadefem = idadefem + 1
mediaid = somaid/4
print('\n'*20)
print('-=-=-'*12)
print('Analisando os dados temos...')
print('-=-=-'*12)
print('\nA média de idade geral é de {} anos. \nO homem mais velho se chama {} e tem {}. {}\nExistem {} mulheres com menos de 20 anos.'.format(mediaid,nomemaior, maior, idadefem))
