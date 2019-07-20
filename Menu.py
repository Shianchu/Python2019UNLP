import PySimpleGUI as sg
from config import config
from Jugar import play
import json
def programlook():
	"""Este modulo da la opcion de utilizar o no un archivo creado mediante una 'Aplicacion ambiental' el actual
	te deja seleccionar un area donde se este utilizando dicha aplicacion que sensa temperatura y en base a un
	promedio modificar el color del juego"""
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


def main():
	"""Modulo principal del juego el cual muestra los botones necesarios para poder configurar, jugar y salir del juego"""
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

if __name__ == '__main__':
	programlook()
	main()
