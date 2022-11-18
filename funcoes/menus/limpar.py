from funcoes.menus import iniciar
from funcoes.menus import confirmacoes

def limparMemoria():
    c = confirmacoes.confirmacao("Deseja realmente limpar a memória? Dijite s para sim e n para não")
    if len(iniciar.historico) == 0:
        print("Não a nada para limpar!")
    elif c:
        iniciar.historico.clear()
        print("Memória limpa com sucesso!")
    else:
        print("A memória não será limpa!")