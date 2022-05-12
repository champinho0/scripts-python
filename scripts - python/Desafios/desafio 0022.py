#Crie um programa que leia o nome de uma pessoa e mostre: O nome com todas as letras maiúsculas, o nome com todas as letras minúsculas
#quantas letras tem ao total (desconsiderando espaços) e quantas letras tem o primeiro nome
nome = str(input('Digite o nome completo de uma pessoa: ')).strip() #.strip irá já remover os espaços da direita e esquerda
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower))
print('Seu nome tem um total de {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#ou
#separa = nome.split()
#print ('Seu primeiro nome tem {} letras.'.format(separa[0],len(separa[0])))