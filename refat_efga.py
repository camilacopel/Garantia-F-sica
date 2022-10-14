


import pandas as pd
from pathlib import Path

class Efga():
    
    def __init__(self, path: Path) :
        
        self.path = path
        efga = pd.read_csv(self.path, 
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
        self.efga = efga
    
    def energia_firme(self):
        efga = self.efga
        somatorio_energia_firme = efga["Energia Firme"].sum()
        
        return efga
    
    def media(self):
        somatorio = self.energia_firme
        media = self.efga['Energia Firme']/ somatorio
        
        return media
    

if __name__ == '__main__':
    arq = 'C:/Users/E805511/Documents/modelos_cepel_python-master/EFGA.csv'
    efga = Efga(arq)