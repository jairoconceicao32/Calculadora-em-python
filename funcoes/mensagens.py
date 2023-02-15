from accessible_output2 import outputs
mensagem=outputs.auto.Auto().speak

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO: por favor digite um número inteiro válido")
            continue
        except(KeyboardInterrupt):
            print("Opção inválida")
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("ERRO: por favor digite um número real válido")
            continue
        except(KeyboardInterrupt):
            print("O usuário preferiu não digitar este valor.")
            return 0
        else:
            return n

def escrever(msg):
    return str(input(msg))