from  funcoes.menus import iniciar
from funcoes.menus import  resultados
from  funcoes.menus import limpar
from funcoes.menus import confirmacoes

def menu():
    print("\t Menu principal \n")
    while True:
        opcoes = str(input(
            "Calculadora qual a opção que deseja: \+"
            "\ni Iniciar calculadora: "
            "\nv Ver histórico de resultados: "
            "\nl Limpar histórico: "
            "\ns Sair: "
        )).lower()
        if opcoes == "i" and "I":
            iniciar.iniciar()
        if opcoes == "v" and "V":
            resultados.verHistorico()
        if opcoes == "l" and "L":
            limpar.limparMemoria()
        if opcoes == "s" and "S":
            c = confirmacoes.confirmacao("Deseja encerrar a calculadora? Dijite s para sim e N para não")
            if c:
                print("Calculadora desligada!")
                break
            else:
                print("Retornando ao menu principal...")