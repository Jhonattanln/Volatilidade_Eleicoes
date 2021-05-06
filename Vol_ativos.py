import pandas as pd
import matplotlib.pyplot as plt

########### Importando os dados

df = pd.read_excel('economatica.xlsx', parse_dates=True, index_col=0).dropna()

#### Calculando IBOV
ibov = pd.DataFrame()

for year in ['2006', '2010', '2014', '2018']:
    preço_ibov = df.loc[year, ['IBOV']].reset_index(drop=True)
    preço_ibov.rename(columns={'IBOV':year}, inplace=True)
    ibov = pd.concat([ibov, preço_ibov], axis=1)

