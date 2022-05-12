#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite o nome de uma cidade: ')).strip() #o strip vai tirar os espaços do inicio e do final
print(cidade[:5].upper() == 'SANTO')
#[:5] vai verificar até o quinto caractere inicial, validando ou nao se existe santo no inicio
#.upper() irá jogar todos os caracteres digitados para maiusculos, assim, o usúario podeá de digitar de várias formas e a validação não terá erros
