import PySimpleGUI as sg
from config import config
from Jugar import play
import json
try:
	rta=sg.PopupYesNo('Desea elegir una oficina para modificar el estilo?')
	if rta=='Yes':
		with open('Oficinas.json',"r") as inFile:
			archivo = json.load(inFile)
			inFile.close()
		est=[[sg.Table(values=archivo.keys(),headings=['Oficina'],justification="left")],
		[sg.Input(key='ofi')],[sg.Button('Aceptar')]]
		winest=sg.Window('Estilo',est)
		while True:
			event,values=winest.Read()
			if event==None:
				break
			if event=='Aceptar':
				try:
					oficina=archivo[values['ofi']]
					prom=0
					for i in oficina:
						prom=prom+i['temperatura']
					prom=prom/len(oficina)
					if (prom<20):
						sg.ChangeLookAndFeel('SandyBeach')
					else:
						sg.ChangeLookAndFeel('BrownBlue')
					break
				except:
					sg.Popup('Nombre de oficina no encontrado')
		winest.Close()
except:
	sg.Popup('No se encuentra el archivo de oficinas')


layout=[[sg.Text("Sopa de letras")],
		[sg.Button('Configuración'),sg.Button('Jugar'),sg.Button('Salir')]]
window=sg.Window('Sopa de letras',layout)


cant={'verb':0,'sus':0,'adj':0}
palabras=[['','']]
can=[0,0,0]
vert=True
caps=True
ayuda=False
while True:
	event,values=window.Read()
	if event is None or event=='Salir':
		break
	if event == 'Configuración':
		dic=config(palabras,cant,vert,caps,ayuda)
		palabras=dic['palabras']
		for i in range(len(dic['cant'])):
			can[i]=dic['cant'][i]
	if event == 'Jugar': 
		try:
			if dic['cant']=={} or dic['cant']==[0,0,0]:
				raise
			play(dic['palabras'],dic['cant'],dic['vert'],dic['caps'],dic['ayuda'],dic['color'])
			dic['palabras']=palabras
			for i in range(len(can)):
				dic['cant'][i]=can[i]
		except:
			sg.Popup('Se debe configurar primero')
window.Close()
