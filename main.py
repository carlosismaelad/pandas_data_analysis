import pandas as pd
import plotly.express as px

# Importar a base de dados
tabela = pd.read_csv("./clientes.csv", encoding='latin-1', sep=";")

# Deletar uma coluna inútil
tabela = tabela.drop("Unnamed: 8", axis=1) # axis = 0 para linha e 1 para coluna

## Visualizar, entender as informações e procurar os inconsistências da base de dados 
print(tabela, sep=";")

# Tratar os dados -> Valores lidos de forma errada / Salario lido como object
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

# Valores vazios -> Jogar fora 35 linhas com valores vazios
tabela = tabela.dropna()
print(tabela.info())

# Analise inicial -> Entender como estão as notas dos clientes
print(tabela.describe())

## Analise completa -> Traçar o perfil ideal dos clientes e conhecer as características que impactam na nota

# Cria o gráfico para cada coluna da tabela
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=20)

    # Exibe o gráfico
    grafico.show()

### CONCLUSÃO:
## Perfil do cliente ideal
# Clientes acima de 10 anos
# Clientes da área de entretenimento e artistas tem nota muito acima dos outros
# Cliente que tem entre 10 e 15 anos de experiência de trabalho
# Famílias de até 7 pessoas

## OBS:
# Clientes da aŕea da construção tem a menor nota
# Clientes obtidos por promoções tem nota inferior
# O salário parece não implicar em nada significativo