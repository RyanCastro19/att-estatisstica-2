import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Criação dos dados
data = {
    'Combustível': ['GASOLINA']*5 + ['DIESEL S10']*5 + ['ETANOL']*3 + ['DIESEL']*3 + ['GASOLINA ADITIVADA']*3,
    'Preço': [4.87, 6.95, 6.93, 6.22, 6.26, 4.88, 6.85, 6.84, 5.85, 5.99, 3.27, 5.49, 4.59, 5.75, 5.79, 5.96, 6.29, 6.29, 6.99]
}

df = pd.DataFrame(data)

# Criação do boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Combustível', y='Preço', data=df)
plt.title('Boxplot dos Preços dos Combustíveis')
plt.xlabel('Combustível')
plt.ylabel('Preço (R$)')
plt.show()
