from funcoes_historico.historico import *
from funcoes.confirmacoes import *
from funcoes.mensagens import *

def limparHistorico():
    c = confirmar("Deseja limpar o histórico? Dijite s para sim e n para não")
    if c:
        if len(historico) == 0:
            mensagem("Histórico vazio!")
        else:
            historico.clear()
            mensagem("Histórico limpo com sucesso!")
    else:
        mensagem("O histórico não será limpo")