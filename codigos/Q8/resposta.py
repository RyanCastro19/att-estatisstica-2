# Renomear a coluna com caracteres estranhos para facilitar o uso e focar nas colunas relevantes
df.rename(columns={'ï»¿Regiao - Sigla': 'Regiao'}, inplace=True)

# Filtrar os dados apenas para a Gasolina
df_gasolina = df[df['Produto'] == 'GASOLINA']

# Remover colunas desnecessárias para essa análise
df_gasolina = df_gasolina[['Regiao', 'Valor de Venda']]

# Converter os valores de venda para numérico (caso haja algum problema com o formato)
df_gasolina['Valor de Venda'] = pd.to_numeric(df_gasolina['Valor de Venda'].str.replace(',', '.'), errors='coerce')

# a) Calcular o preço médio de venda da gasolina por região
preco_medio_por_regiao = df_gasolina.groupby('Regiao')['Valor de Venda'].mean().round(2)

# b) Análise dos quantis do preço de venda da gasolina por região
quantis_por_regiao = df_gasolina.groupby('Regiao')['Valor de Venda'].quantile([0.25, 0.5, 0.75]).unstack().round(2)

preco_medio_por_regiao, quantis_por_regiao
