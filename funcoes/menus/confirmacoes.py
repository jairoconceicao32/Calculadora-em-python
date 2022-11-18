def confirmacao(msg):
    mensagem = input(msg).lower()
    if mensagem == "s" and "S":
        return True
    elif mensagem == "n" and "N":
        return False
    print("Opção inválida")