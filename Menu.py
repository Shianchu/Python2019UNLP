import PySimpleGUI as sg
from config import config
from Jugar import play


layout=[[sg.Text("Sopa de letras")],
		[sg.Button('Configuración'),sg.Button('Jugar'),sg.Button('Salir')]]
window=sg.Window('Sopa de letras',layout)


cant={'verb':0,'sus':0,'adj':0}
vert=True
caps=True
ayuda=False
while True:
	event,values=window.Read()
	if event is None or event=='Salir':
		break
	if event == 'Configuración':
		dic=config(cant,vert,caps,ayuda)
	if event == 'Jugar': 
		play(dic['palabras'],dic['cant'],dic['vert'],dic['caps'],dic['ayuda'],dic['color'])
window.Close()
