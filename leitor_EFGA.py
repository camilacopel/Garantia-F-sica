
# -*- coding: utf-8 -*-

"""
Created on Tue Aug 23 18:51:27 2022.
@author: E805511

LEITURA EFGA

Dados:
--------------------
código | usina | energia firma | media
---------------------------------------
skiprows = 5
drop = última linha (total)


Step to step:
    1. sort(organizar as usinas em ordem crescente através do código delas);
    2. Dados das usinas hidro
    3. Dados configuração
    4. Leitura do arquivo hidr.dat
    --------------
    
    4. Potência Total = numero_maquinas * potencia_unitária
    5. GF local = EH * (energia firme/ sum(energia firme))
    
    
    --------------
    6. colnames(df.hidros) <- c("Codigo", "Usina", "codSubsistema", 
  "Energia Firme", "GFlocal", "Potencia Total", "Num. de Unidades Geradoras", 
  "TEIF", "IP")
    
    
"""

import pandas as pd

arq = 'C:/Users/E805511/Documents/modelos_cepel_python-master/EFGA.csv'
efga = pd.read_csv(arq, 
                    encoding='utf-8',
                    engine= 'python',
                    header=0,
                    index_col= 'Codigo',
                    #delimiter= ',',
                    #delim_whitespace=True,
                    skiprows=4,
                    skipinitialspace= True,
                    #lineterminator=","
                    quotechar=',',
                    #doublequote=True,
                    #Retira as vírgulas
                    escapechar='"',
                    #na_values=True,
                    skipfooter= 1,
                    )


#%%
import pandas as pd
somatorio_energia_firme = efga["Energia Firme"].sum()
#efga.dtypes

efga = efga.sort_index()
#wrong
#t = efga/ energia_firme

u = efga['Energia Firme']/ somatorio_energia_firme


 
