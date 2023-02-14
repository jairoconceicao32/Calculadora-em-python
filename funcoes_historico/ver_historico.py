from funcoes.mensagens import *
from funcoes_historico.historico import *

def verHistorico(h):
    h = str(historico)
    h=h.replace(",", "")
    h = h.replace("[", "")
    h = h.replace("[", "")
    h = h.replace("]", "")
    h = h.replace("'", "")
    h = h.replace("'", "")
    if len(h) == 0:
        mensagem("Nada no histórico!")
    for m in h:
        mensagem("Mostrando o histórico da calculadora: \n")
        mensagem(f"{h}")
        break