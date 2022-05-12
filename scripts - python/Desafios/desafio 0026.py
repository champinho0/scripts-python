#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print ('Nessa frase aparece {} letras "A"'.format(frase.count('A')))
print ('O primeiro "A" está localizado na posição: ',frase.find('A'))
print('A uúltima letra "A" está localizada na posição', frase.rfind('A')) #rfind = vai começar a contar da direita para a direita
