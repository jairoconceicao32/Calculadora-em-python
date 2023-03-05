from funcoes.operacoes import *
import wx
import sys
from accessible_output2 import outputs
import threading
from threading import Thread
from traceback import format_exception

def trataExceptPrograma(type, description, traceback):
	tipoErro=type
	erroDesc=description
	erroTraceback=traceback
	erroFormatado=format_exception(tipoErro, erroDesc, erroTraceback)
	dialog=wx.Dialog(None, title="erro do programa")
	textoErro=wx.TextCtrl(dialog, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP, value="")
	for linha in erroFormatado:
		textoErro.AppendText(linha)
	dialog.ShowModal()
sys.excepthook=trataExceptPrograma
def trataExceptThread(info):
	nomeErro=info.exc_type.__name__
	descErro=info.exc_value
	tb=info.exc_traceback
	erro=format_exception(nomeErro, descErro, tb)
	dialogErro=wx.Dialog(None, title="erro do programa em uma Thread")
	mostraErro=wx.TextCtrl(dialogErro, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP, value="")
	for linhaErro in erro:
		mostraErro.AppendText(linhaErro)
	dialogErro.ShowModal()
	sys.exit()
threading.excepthook=trataExceptThread

mensagem=outputs.auto.Auto().speak
mensagem("Bem-vindo a calculadora!")
class janela(wx.Dialog):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.historico = [	]
		label1=wx.StaticText(self, label="&1º valor")
		self.valor1=wx.TextCtrl(self)
		labelEscolha=wx.StaticText(self, label="Escolha a operação")
		listaOperações=[
			"Somar",
			"Subtrair",
			"Multiplicar",
			"Dividir",
			"Potência",
			"Raíz",
			"Fatorial"
]
		self.escolha=wx.ComboBox(self, choices=listaOperações, style=wx.CB_READONLY)
		self.escolha.SetValue("Somar")
		label2=wx.StaticText(self, label="&2º valor")
		self.valor2=wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
		calcular=wx.Button(self, wx.ID_OK, label="&Calcular")
		self.valor2.Bind(wx.EVT_TEXT_ENTER, self.calcula)
		his = wx.Button(self, label="&Histórico")
		his.Bind(wx.EVT_BUTTON, self.hi)
		sair=wx.Button(self, wx.ID_CANCEL, label="Desligar calculadora")
		sair.Bind(wx.EVT_BUTTON, sys.exit)
		calcular.Bind(wx.EVT_BUTTON, self.calcula)
		self.ShowModal()

	def calcula(self, evento):
		v1=self.valor1.GetValue()
		v2=self.valor2.GetValue()
		if v1=="" or v2=="":return
		try:
			n1=int(v1)
			n2=int(v2)
		except:
			wx.MessageBox("são aceitos apenas números.", "erro", wx.ICON_ERROR)
			return
		operação=self.escolha.GetSelection()
		if operação==0:#Soma
			resultado=somar(n1, n2)
			a = wx.MessageBox(f"O resultado foi {resultado}. Deseja adicionar ao histórico?", "Resultado", wx.ICON_QUESTION|wx.YES_NO) #Exibe a mensagem, e questiona ao usuário se ele quer mesmo adicionar ao histórico a operação e o resultado.
			if a == 2: #Verificação para adicionar o resultado ao histórico
				self.historico.append(f"O resultado da adição entre {n1} e {n2} foi: {resultado}")
				wx.MessageBox("Operação adicionada!", "Mensagem")
			else: #Mensagem exibida caso o usuário decida não adicionar ao histórico de resultados.
				wx.MessageBox("O resultado não será adicionado ao histórico", "Mensagem")
		elif operação==1:#subtrair
			resultado=subtrair(n1, n2)
			a = wx.MessageBox(f"O resultado foi {resultado}. Deseja adicionar ao histórico?", "Resultado", wx.ICON_QUESTION|wx.YES_NO) #Exibe a mensagem, e questiona ao usuário se ele quer mesmo adicionar ao histórico a operação e o resultado.
			if a == 2: #Verificação para adicionar o resultado ao histórico
				self.historico.append(f"O resultado da subtração entre {n1} e {n2} foi: {resultado}")
				wx.MessageBox("Operação adicionada!", "Mensagem")
			else: #Mensagem exibida caso o usuário decida não adicionar ao histórico de resultados.
				wx.MessageBox("O resultado não será adicionado ao histórico", "Mensagem")
		elif operação ==2:#Multiplicação
			resultado=multiplicar(n1, n2)
			a = wx.MessageBox(f"O resultado foi {resultado}. Deseja adicionar ao histórico?", "Resultado", wx.ICON_QUESTION|wx.YES_NO) #Exibe a mensagem, e questiona ao usuário se ele quer mesmo adicionar ao histórico a operação e o resultado.
			if a == 2: #Verificação para adicionar o resultado ao histórico
				self.historico.append(f"O resultado da multiplicação entre {n1} e {n2} foi: {resultado}")
				wx.MessageBox("Operação adicionada!", "Mensagem")
			else: #Mensagem exibida caso o usuário decida não adicionar ao histórico de resultados.
				wx.MessageBox("O resultado não será adicionado ao histórico", "Mensagem")
		elif operação==3:#Divisão
			resultado=dividir(n1, n2)
			if resultado==None:#Verifica se um dos valores da divisão é zero e exibe uma mensagem de erro ao usuário.
				wx.MessageBox("Não é possível dividir por zero", "erro", wx.ICON_ERROR)
			else:
				resultado_ii=int(resultado)
				a = wx.MessageBox(f"O resultado foi {resultado_ii}. Deseja adicionar ao histórico?", "Resultado", wx.ICON_QUESTION|wx.YES_NO) #Exibe a mensagem, e questiona ao usuário se ele quer mesmo adicionar ao histórico a operação e o resultado.
				if a == 2: #Verificação para adicionar o resultado ao histórico
					self.historico.append(f"O resultado da divisão entre {n1} e {n2} foi: {resultado_ii}")
					wx.MessageBox("Operação adicionada!", "Mensagem")
				else: #Mensagem exibida caso o usuário decida não adicionar ao histórico de resultados.
					wx.MessageBox("O resultado não será adicionado ao histórico", "Mensagem")
		elif operação==4:#Potenciação
			resultado=potencia(n1, n2)
			a = wx.MessageBox(f"O resultado foi {resultado}. Deseja adicionar ao histórico?", "Resultado", wx.ICON_QUESTION|wx.YES_NO) #Exibe a mensagem, e questiona ao usuário se ele quer mesmo adicionar ao histórico a operação e o resultado.
			if a == 2: #Verificação para adicionar o resultado ao histórico
				self.historico.append(f"O resultado da potenciação entre {n1} e {n2} foi: {resultado}")
				wx.MessageBox("Operação adicionada!", "Mensagem")
			else: #Mensagem exibida caso o usuário decida não adicionar ao histórico de resultados.
				wx.MessageBox("O resultado não será adicionado ao histórico", "Mensagem")
		elif operação==5:#Raíz
			resultado=raiz(n1, n2)
			a = wx.MessageBox(f"O resultado foi {resultado}. Deseja adicionar ao histórico?", "Resultado", wx.ICON_QUESTION|wx.YES_NO) #Exibe a mensagem, e questiona ao usuário se ele quer mesmo adicionar ao histórico a operação e o resultado.
			if a == 2: #Verificação para adicionar o resultado ao histórico
				self.historico.append(f"O resultado da raíz entre {n1} e {n2} foi: {resultado}")
				wx.MessageBox("Operação adicionada!", "Mensagem")
			else: #Mensagem exibida caso o usuário decida não adicionar ao histórico de resultados.
				wx.MessageBox("O resultado não será adicionado ao histórico", "Mensagem")
		elif operação==6:#Fatorial
			if n1 == n2: #Verificação para ver se os dois números dijitados são iguais em caso sim, o fatorial será feito.
				resultado=fatorial(n1)
				a = wx.MessageBox(f"O resultado foi {resultado}. Deseja adicionar ao histórico?", "Resultado", wx.ICON_QUESTION|wx.YES_NO) #Exibe a mensagem, e questiona ao usuário se ele quer mesmo adicionar ao histórico a operação e o resultado.
				if a == 2: #Verificação para adicionar o resultado ao histórico
					self.historico.append(f"O resultado do fatorial de {n1} foi: {resultado}")
					wx.MessageBox("Operação adicionada!", "Mensagem")
				else: #Mensagem exibida caso o usuário decida não adicionar ao histórico de resultados.
					wx.MessageBox("O resultado não será adicionado ao histórico", "Mensagem")
			else:
				wx.MessageBox("Os números precisam ser iguais para que o fatorial possa ser calculado", "erro", wx.ICON_ERROR)

	def hi(self, evento):
		d = wx.Dialog(self, title="Histórico de operações")
		label=wx.StaticText(d, label="Histórico de operações")
		self.mostrar=wx.TextCtrl(d, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP)
		for h in self.historico:
			self.mostrar.AppendText(h+"\n")
		apagarHistorico=wx.Button(d, label="&Apagar histórico")
		salvar=wx.Button(d, label="salvar histórico em arquivo")
		salvar.Bind(wx.EVT_BUTTON, self.salvaHistorico)
		apagarHistorico.Bind(wx.EVT_BUTTON, self.apagarH)
		voltar = wx.Button(d, wx.ID_CANCEL, label="Voltar")
		d.ShowModal()

	def salvaHistorico(self, evento):
		d=wx.FileDialog(None)
		d.SetMessage("salvar como")
		d.ShowModal()
		caminho=d.GetPath()
		arquivo=open(caminho, "w")
		for h in self.historico:
			arquivo.write(h+"\n")
		arquivo.close()

	def apagarH(self, evento):
		c = wx.MessageBox("Deseja apagar o histórico de operações.", "Mensagem", wx.ICON_QUESTION|wx.YES_NO)
		if c == 2:
			h=self.mostrar.GetValue()
			if len(h) ==0:
				wx.MessageBox("O histórico de operações está vazio", "Mensagem")
			else:
				self.mostrar.Clear()
				wx.MessageBox("Histórico de operações apagado!", "Apagado")
		else:
			wx.MessageBox("Você não deseja apagar o histórico... Então tchau pra você!", "Mensagem")


app=wx.App()
calculadora=janela(None, title="Calculadora")
app.MainLoop()