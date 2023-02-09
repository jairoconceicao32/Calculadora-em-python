from funcoes.mensagens import *
from funcoes.calcular import *
from menu.opcoes_historico import *
from  funcoes.confirmacoes import *

def menu():
    mensagem("Menu principal \n")
    while True:
        opcoes =escrever(
            "Calculadora qual a opção que deseja: \n"
            "\nCalcular C: "
            "\nHistórico H: "
            "\nsair S: "
        ).lower()
        if opcoes == "c" and "C":
            calculando()
        if opcoes == "h" and "H":
            o()
        if opcoes == "s" and "S":
            c2 = confirmar("Deseja realmente desligar a calculadora?\n Dijite s para sim e n para não")
            if c2:
                mensagem("Calculadora desligada!")
                break
            mensagem("Retornando ao menu principal...")