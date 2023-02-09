from funcoes.mensagens import *
from funcoes_historico.historico import *

def verHistorico(h):
    h = historico
    if len(h) == 0:
        mensagem("Nada no histórico!")
    for m in h:
        mensagem(f"Operação: {operacoes} e o resultado {h}")