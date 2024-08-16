#Analise de tabelas

# Percorrer arquivos

import os
import pandas as pd

lista_arquivos = os.listdir("D:/Documents/Vendas")
print (lista_arquivos)

#criar tabela vazia
tabela_total = pd.DataFrame()

# Importar arquivos

for arquivos in lista_arquivos:
  if "Vendas" in arquivos:
   tabela = pd.read_csv(f"D:/Documents/vendas/{arquivos}")
   tabela_total = pd.concat([tabela_total, tabela])


#Calcular maior produto vendido em quantidade

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida" , "Preco Unitario"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)