import pandas as pd
import numpy as np

# Lendo o arquivo CSV com o delimitador correto
data = pd.read_csv('previdencia2.csv', delimiter=';', header=0, skip_blank_lines=True, encoding='utf-8')

coluna = data.iloc[:, 2]
coluna_numpy = coluna.to_numpy()

# Resumo estatístico da coluna 'Receita'
print("\nResumo estatístico da receita:")
print(data['Receita'].describe())

# Exibindo as primeiras 700 linhas
print(data.head(60))

# Ordenando o DataFrame pela coluna 'Receita'
data_sorted = data.sort_values(by='Receita', ascending=False)

# Exibindo as primeiras linhas do DataFrame ordenado por receita
print("\nPrimeiras linhas do DataFrame ordenado por receita:")
#print(data_sorted.head(20))

coluna_ordenada = np.sort(coluna_numpy)
print(np.min(coluna_ordenada))