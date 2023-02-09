from funcoes.mensagens import *
from funcoes.operacoes import *
from funcoes.confirmacoes import *
from funcoes_historico.historico import *


def calculando():
    mensagem("É hora de calcular!")
    while True:
        n1 = leiaInt("Informe o valor")
        operar = escrever(
            "Qual a operação que deseja? \n"
            "+ Mais para adção \n"
            "- Menos para subtração\n"
            "* vezes para multiplicação \n"
            "/ divisão para divisão"
            "** potência para potência \n"
            "// Para raíz \n"
            "F Para fatorial \n"
        )
        if operar == "+":
            n2 = leiaInt("Informe o valor")
            result = somar(n1, n2)
            mensagem(f"O resultado entre {n1} e {n2} foi: {result}")
            c = confirmar("Deseja passar os valores para o histórico? Dijite s para sim e n para não")
            if c:
                operacoes.append("A soma entre")
                operacoes.append(n1)
                operacoes.append("e")
                operacoes.append(n2)
                historico.append(result)
                mensagem("Operação adicionada!")
                break
            else:
                mensagem("Os valores não serão passados para a memória")
                break
        elif operar == "-":
            n2 = leiaInt("Informe o valor: ")
            result = subtrair(n1, n2)
            mensagem(f"O resultado da subtração entre {n1} e {n2} foi: {result}")
            c = confirmar("Deseja passar os valores para o histórico? Dijite s para sim e n para não")
            if c:
                operacoes.append("A subtração entre")
                operacoes.append(n1)
                operacoes.append("e")
                operacoes.append(n2)
                historico.append(result)
                mensagem("Operação adicionada!")
                break
            else:
                mensagem("Os valores não serão passados para a memória")
                break
        elif operar == "*":
            n2 = leiaInt("Informe o valor: ")
            result = multiplicar(n1, n2)
            mensagem(f"O resultado da multiplicação entre {n1} e {n2} foi: {result} ")
            c = confirmar("Deseja passar os valores para o histórico? Dijite s para sim e n para não")
            if c:
                operacoes.append("A multiplicação entre")
                operacoes.append(n1)
                operacoes.append("e")
                operacoes.append(n2)
                historico.append(result)
                mensagem("Operação adicionada!")
                break
            else:
                mensagem("Os valores não serão passados para a memória")
                break
        elif operar == "/":
            n2 = leiaInt("Informe o valor: ")
            result = dividir(n1, n2)
            mensagem(f"O resultado da divisão entre {n1} e {n2} foi: {result}")
            c = confirmar("Deseja passar os valores para o histórico? Dijite s para sim e n para não")
            if c:
                operacoes.append("A divisão entre")
                operacoes.append(n1)
                operacoes.append("e")
                operacoes.append(n2)
                historico.append(result)
                mensagem("Operação adicionada!")
                break
            else:
                mensagem("Os valores não serão passados para a memória")
                break
        elif operar == "**":
            n2 = leiaInt("Informe o valor: ")
            result = potencia(n1, n2)
            mensagem(f"O resultado da potenciação entre {n1} e {n2} foi: {result}")
            c = confirmar("Deseja passar os valores para o histórico? Dijite s para sim e n para não")
            if c:
                operacoes.append("A potenciação entre")
                operacoes.append(n1)
                operacoes.append("e")
                operacoes.append(n2)
                historico.append(result)
                mensagem("Operação adicionada!")
                break
            else:
                mensagem("Os valores não serão passados para a memória")
                break
        elif operar == "//":
            n2 = leiaInt("Informe o valor ")
            result = raiz(n1, n2)
            mensagem(f"O resultado da raízentre {n1} e {n2} foi: {result}")
            c = confirmar("Deseja passar os valores para o histórico? Dijite s para sim e n para não")
            if c:
                operacoes.append("A raíz entre")
                operacoes.append(n1)
                operacoes.append("e")
                operacoes.append(n2)
                historico.append(result)
                mensagem("Operação adicionada!")
                break
            else:
                mensagem("Os valores não serão passados para a memória")
                break
        elif operar == "f":
            if n1 < 0:
                mensagem("O fatorial só aceita números positivos")
                continue
            result = fatorial(n1)
            mensagem(f"O fatorial de {n1} foi: {result}")
            c = confirmar("Deseja passar os valores para o histórico? Dijite s para sim e n para não")
            if c:
                operacoes.append("O fatorial de")
                operacoes.append(n1)
                historico.append(result)
                mensagem("Operação adicionada!")
                break
            else:
                mensagem("Os valores não serão passados para a memória")
                break
        else:
            mensagem("Operação inválida")