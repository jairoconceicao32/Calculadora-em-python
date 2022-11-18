import pandas as pd

def criarHistorico(lista):
    historico = {resultado: 1}
    historicoDf = pd.DataFrame(historico)
    historicoDf