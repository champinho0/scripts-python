import easyocr
reader = easyocr.Reader(['pt'])
resultados = reader.readtext('teste.jpeg', paragraph=True)

for resultado in resultados:
    print(f'Texto:\n'
          f'\tP: {resultado[0]}\n'
          f'\tTexto: {resultado[1]}\n')