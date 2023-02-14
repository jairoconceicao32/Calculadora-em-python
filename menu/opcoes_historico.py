from funcoes.mensagens import *
from funcoes_historico.ver_historico import *
from funcoes_historico.limpar import *
from funcoes_historico.copiar import *

def o():
    mensagem("Histórico menu \n")
    while True:
        menu = escrever(
            "Ver hhistórico v: \n"
            "Limpar histórico L: \n"
            "Copiar histórico c: \n"
            "Retornar ao menu anterior R: \n"
        ).lower()
        if menu == "v" and "V":
            verHistorico(historico)
        if menu == "l" and "L":
            limparHistorico()
        if menu == "c" and "C":
            copiarHist()
        if menu == "r" and "R":
            mensagem("Retornando ao menu principal...")
            break