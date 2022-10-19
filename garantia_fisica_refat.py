"""Cálculo da garantia física de acordo com a resolução ...
    Explicar um pouco sobre a resolução
    
    Objetivo
    ------
    
    Comparar com os resultados obtidos da EPE usando o R programming.
    """


from pathlib import Path
import utils
import builder_nw as bnw
import logging
from refat_efga import Efga

#Herança
class GarantiaFisicaLocal:
    def __init__(self) -> None:
        self.ghtotm = None
        

    def somatorio_geracao(self):
        pass
    
    def fator_hidreletrico(self):
        pass
    
    def pequenas_geradoras(self):
        pass
    
    def energia_firme(self):
        efga = Efga()
        
    

if __name__ == '__main__':
#    arquivo1 = newave
#    arquivo2 = Efga
    