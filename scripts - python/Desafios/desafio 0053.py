frase = str(input('Digite uma frase ou palavras: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palnídromo!')
else:
    print('Não temos um palíndromo')