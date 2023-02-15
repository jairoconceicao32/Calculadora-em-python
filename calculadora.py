from funcoes.operacoes import *
import wx
import sys
from accessible_output2 import outputs
mensagem=outputs.auto.Auto().speak

mensagem("Bem-vindo a calculadora!")
class janela(wx.Dialog):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		label1=wx.StaticText(self, label="&1º valor")
		self.valor1=wx.TextCtrl(self)
		labelEscolha=wx.StaticText(self, label="Escolha a operação")
		listaOperações=[
			"Somar",
			"Subtrair",
			"Multiplicar",
			"Dividir",
			"Potência"
			"Raíz",
			"Fatorial"
]
		self.escolha=wx.ComboBox(self, choices=listaOperações, style=wx.CB_READONLY)
		self.escolha.SetValue("Somar")
		label2=wx.StaticText(self, label="&2º valor")
		self.valor2=wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
		calcular=wx.Button(self, wx.ID_OK, label="&Calcular")
		self.valor2.Bind(wx.EVT_TEXT_ENTER, self.calcula)
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
			wx.MessageBox(f"O resultado foi {resultado}", "resultado")
		elif operação==1:#subtrair
			resultado=subtrair(n1, n2)
			wx.MessageBox(f"O resultado foi {resultado}", "Resultado")
		elif operação ==2:#Multiplicação
			resultado=multiplicar(n1, n2)
			wx.MessageBox(f"O resultado foi {resultado}", "resultado")
		elif operação==3:#Divisão
			resultado=dividir(n1, n2)
			if resultado==None:#Verifica se um dos valores da divisão é zero e exibe uma mensagem de erro ao usuário.
				wx.MessageBox("Não é possível dividir por zero", "erro", wx.ICON_ERROR)
			else:
				wx.MessageBox(f"O resultado foi {resultado}", "resultado")
		elif operação==4:#Potenciação
			resultado=potencia(n1, n2)
			wx.MessageBox(f"O resultado foi {resultado}", "resultado")
		elif operação==5:#Raíz
			resultado=raiz(n1, n2)
			wx.MessageBox(f"O resultado foi {resultado}", "resultado")
		elif operação==6:#Fatorial
			resultado=fatorial(n1)
			wx.MessageBox(f"O resultado foi {resultado}", "resultado")

app=wx.App()
calculadora=janela(None, title="Calculadora")
app.MainLoop()