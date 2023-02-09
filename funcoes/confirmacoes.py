from funcoes.mensagens import *

def confirmar(mensagem):
    while True:
        c = escrever(mensagem)
        if c.lower() == "s" and "S":
            return True
        elif c.lower() == "n" and "N":
            return False
        mensagem("Opção inválida")