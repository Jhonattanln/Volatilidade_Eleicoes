import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

########### Importando os dados

df = pd.read_excel('economatica.xlsx', parse_dates=True, index_col=0).dropna()

#### Calculando IBOV
ibov = pd.DataFrame()

for year in ['2006', '2010', '2014', '2018']:
    preço_ibov = df.loc[year, ['IBOV']].reset_index(drop=True)
    preço_ibov.rename(columns={'IBOV':year}, inplace=True)
    ibov = pd.concat([ibov, preço_ibov], axis=1).dropna()

#### Calculando IMAB 5
imab = pd.DataFrame()

for year in ['2006', '2010', '2014', '2018']:
    preço_imab = df.loc[year, ['IMAB 5']].reset_index(drop=True)
    preço_imab.rename(columns={'IMAB 5':year}, inplace=True)
    imab = pd.concat([imab, preço_imab], axis=1).dropna()

#### Calculando IMAB 5+
imab_5 = pd.DataFrame()

for year in ['2006', '2010', '2014', '2018']:
    preço_imab_5 = df.loc[year, ['IMAB 5+']].reset_index(drop=True)
    preço_imab_5.rename(columns={'IMAB 5+':year}, inplace=True)
    imab_5 = pd.concat([imab_5, preço_imab_5], axis=1).dropna()

#### Calculando Dólar
dol = pd.DataFrame()

for year in ['2006', '2010', '2014', '2018']:
    preço_dol = df.loc[year, ['DÓLAR']].reset_index(drop=True)
    preço_dol.rename(columns={'DÓLAR':year}, inplace=True)
    dol = pd.concat([dol, preço_dol], axis=1).dropna()

###################################### Calaculando volatilidade de cada ano ###########################################################

##### Volatilidade ibov
ibov_pct = ibov.pct_change()
vol_ibov = pd.DataFrame()
"""
for year in ibov:
    vol_ibov[year] = ibov[year].rolling(21).
"""
print(ibov_pct)