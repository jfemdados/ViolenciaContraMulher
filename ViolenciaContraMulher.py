#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

data_path = "D:\\Usuarios\\Dell\\Documents\\jf em dados\\mulheres\\seguranca_municipio_br\\seguranca_municipio_geral.csv"

df = pd.read_csv(data_path, index_col=0, low_memory = False, header=0)
df_mg = df.loc[df["Cod_Estado"] == 31]
df_jf = df_mg[df_mg["Cod_Município"]=="313670"]
df_jf["Quantidade_de_Casos"] = df_jf["Quantidade_de_Casos"].astype('int64')

#Gráfico 1: gráfico de barras de violência por faixa etária 
df_jf["Faixa_Etária"] = df_jf["Faixa_Etária"].str.lower()
violencia_faixa_pivot = df_jf.pivot_table(values="Quantidade_de_Casos",index="Faixa_Etária",columns="Ano",aggfunc=sum,margins=True)
violencia_faixa_pivot = violencia_faixa_pivot.fillna(0)
faixa = violencia_faixa_pivot.loc["0-14":"não especificado","All"].plot(kind="bar")

#Gráfico 2: gráfico de barras do tipo de violência 
tipo_violencia_pivot = df_jf.pivot_table(values="Quantidade_de_Casos",index="Tipo_de_Violência",columns="Ano",aggfunc=sum,margins=True)
tipo_violencia_pivot = tipo_violencia_pivot.fillna(0)
tipo = tipo_violencia_pivot.loc["Violência Física":"Violência Sexual","All"].plot(kind="bar")

#Gráfico 3: total de casos por ano 2012-2018
total_ano = df_jf.groupby("Ano")["Quantidade_de_Casos"].sum()
total_ano = pd.DataFrame(total_ano)
total_ano = total_ano.reset_index()
total = total_ano.plot(y="Quantidade_de_Casos",kind="line")


# In[2]:


#Gráfico 4: tipos de ocorrência entre 2012-2018
tipo_ocorrencia_pivot = df_jf.pivot_table(values="Quantidade_de_Casos",index="Ocorrência",columns="Ano",aggfunc=sum,margins=True)
tipo_ocorrencia_pivot = tipo_ocorrencia_pivot.fillna(0)
ocorrencia = tipo_ocorrencia_pivot.loc["Ameaça":"Violação de Domicílio","All"].plot(kind="bar")


# In[ ]:





# In[ ]:




