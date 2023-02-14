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
                historico.append("A adção resultante entre os números asseguir foi:")
                historico.append(n1)
                historico.append("Mais,")
                historico.append(n2)
                historico.append("igual")
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
                historico.append("A Subtração resultante entre os números asseguir foi:")
                historico.append(n1)
                historico.append("Menos")
                historico.append(n2)
                historico.append("igual")
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
                historico.append("A Multiplicação resultante entre os números asseguir foi:")
                historico.append(n1)
                historico.append("Vezes")
                historico.append(n2)
                historico.append("igual")
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
                historico.append("A divisão resultante entre os números asseguir foi:")
                historico.append(n1)
                historico.append("Dividido")
                historico.append(n2)
                historico.append("igual")
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
                historico.append("A potenciação resultante entre os números asseguir foi:")
                historico.append(n1)
                historico.append("Elevada")
                historico.append(n2)
                historico.append("igual")
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
                historico.append("A Raíz resultante entre os números asseguir foi:")
                historico.append(n1)
                historico.append("Raíz")
                historico.append(n2)
                historico.append("igual")
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
                historico.append("O fatorial de")
                historico.append(n1)
                historico.append("igual")
                historico.append(result)
                mensagem("Operação adicionada!")
                break
            else:
                mensagem("Os valores não serão passados para a memória")
                break
        else:
            mensagem("Operação inválida")