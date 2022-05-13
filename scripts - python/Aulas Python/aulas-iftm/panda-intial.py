import pandas as pd #por padrão o panda é chamado de pd
titanic = pd.read_csv ("C://Users/Paulo/Desktop/Programs/scripts-python/scripts - python/Aulas Python/aulas-iftm/titanic.csv")
titanic.head(10)
titanic.tail(10)
titanic.dtypes
titanic.to_excel ("C://Users/Paulo/Desktop/Programs/scripts-python/scripts - python/Aulas Python/aulas-iftm/titanic.xls")
sheet_name = ("passageiros", index=False)
#instalar o panda