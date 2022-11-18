import pyperclip
from  funcoes.menus import iniciar
from funcoes.menus import confirmacoes

def verHistorico():
    mostrar = iniciar.historico
    for c in mostrar:
        print(f"Resultados na memória: {mostrar}")
        break
    if len(mostrar) == 0:
        print("Nada para mostrar no histórico!")
        return 0
    c = confirmacoes.confirmacao("Deseja copiar o histórico de resultados para a sua área de transferência? Dijite S para sim e N para não")
    if c:
        mostrar2 = str(mostrar)
        mostrar2.replace("[]", "")
        print(mostrar2)
        pyperclip.copy(mostrar2)
        print("Conteúdo do histórico copiado para a área de transferência!")
    else:
        print("Operação canselada")