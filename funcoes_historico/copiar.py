from pyperclip import *
from funcoes_historico.historico import *
from funcoes.mensagens import *


def copiarHist():
    h = str(historico)
    h = h.replace(",", "")
    h = h.replace("[", "")
    h = h.replace("]", "")
    h = h.replace("'", "")
    h = h.replace("'", "")
    if len(h) == 0:
        mensagem("Não há nada no histórico a ser copiado")
    else:
        copy(h)
        mensagem("Histórico copiado para a área de transferência")