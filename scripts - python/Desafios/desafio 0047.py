# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for cont in range(1, 51):
    if cont%2 == 0:
        print(cont, end=' ')#end=' ' vai mostrar tudo na mesma linha
print("\nEsses foram os números pares")

#um programa mais rapido e eficiente seria, assim nao precisaria do if, pois o contador já iria contar de 2 em 2, ou seja, contaria somente os pares
#for cont in range(1, 51, 2):
#print(cont, end=' ')
#print("\nEsses foram os números pares")