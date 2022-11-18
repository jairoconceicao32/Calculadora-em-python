from funcoes.menus import operacoes
from funcoes.menus import resultados

global result
historico = []

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO: por favor digite um número inteiro válido")
            continue
        except(KeyboardInterrupt):
            print("O usuário preferiu não digitar este valor.")
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

def iniciar():
    print("Vamos calcular!")
    while True:
        n1 = leiaInt("Qual o valor desejado?")
        operar = leiaInt("Informe qual a operação que deseja fazer:\n1- para adção:\n2- para subtração\n3- para multiplicação:\n4 para divisão:\n5 para potência\n6- para raíz quadrada")
        if operar == 1:
            n2 = leiaInt("Qual o valor?")
            print(f"O resultado da adção foi {operacoes.somar(n1, n2)}")
            result = operacoes.somar(n1, n2)
            historico.append(result)
            break
        if operar == 2:
            n2 = leiaInt("Qual o valor?")
            print(f"O resultado da subtração foi: {operacoes.subtrair(n1, n2)}")
            result = operacoes.subtrair(n1, n2)
            historico.append(result)
            break
        if operar == 3:
            n2 = leiaInt("Qual o valor?")
            print(f"O resultado da multiplicação foi: {operacoes.multiplicar(n1, n2)}")
            result = operacoes.multiplicar(n1, n2)
            historico.append(result)
            break
        if operar == 4:
            n2 = leiaInt("Qual o valor?")
            result = operacoes.dividir(n1, n2)
            if result == None:
                print("O resultado não será transferido para memória pois o resultado da divisão não é válido")
                break
            else:
                print(f"O resultado da divisão foi: {operacoes.dividir(n1, n2)}")
                historico.append(result)
                break
        if operar == 5:
            n2 = leiaInt("Qual o valor?")
            print(f"O resultado da potência foi: {operacoes.potencia(n1, n2)}")
            result = operacoes.potencia(n1, n2)
            historico.append(result)
            break
        if operar == 6:
            print(f"O resultado da raíz foi: {operacoes.raiz(n1)}")
            result = operacoes.raiz(n1)
            historico.append(result)
            break