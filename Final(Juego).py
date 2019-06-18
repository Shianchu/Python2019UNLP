from pattern.web import Wiktionary,DOM,plaintext,SEARCH
from pattern.es import parse
import pattern
import PySimpleGUI as sg
def config():
	cant={'verb':0,'sus':0,'adj':0}
	numVerbos=0
	numAdj=0
	numSus=0
	con=[[sg.Text('Orientación:')],
		[sg.Button('Vertical',key='Vertical'),sg.Button('Horizontal',key='Horizontal',button_color=('Black','LightGrey'))],
		[sg.Text('Ayuda:')],
		[sg.Button('Activada',key='act',button_color=('Black','LightGrey')),sg.Button('Desactivada',key='des')],
		[sg.Button('Ingresar palabras')],
		[sg.Button('Colores')],
		[sg.Text('Verbos'),sg.Input(key='verb',size=(2,3)),sg.Text('/'+str(cant['verb']))],
		[sg.Text('Adjetivos'),sg.Input(key='adj',size=(2,3)),sg.Text('/'+str(cant['adj']))],
		[sg.Text('Sustantivos'),sg.Input(key='sus',size=(2,3)),sg.Text('/'+str(cant['sus']))],
		[sg.Button('Verificar palabras')],
		[sg.Button('Mayúsculas',key='caps'),sg.Button('Minúsculas',key='min',button_color=('Black','LightGrey'))],
		[sg.Button('Tipografias')],[sg.Button('Estilo')],
		[sg.Button('Salir'),sg.Button('Aceptar',key='Aceptar',disabled=True)]]
	wincon=sg.Window('Configuración',con)
	while True:
		event,values=wincon.Read()
		if event=='Salir' or event is None:
			break
		if event=='Horizontal':
			wincon.FindElement("Horizontal").Update(button_color=('White','DarkBlue'))
			wincon.FindElement("Vertical").Update(button_color=('Black','LightGrey'))
			vert=False
		if event=='Vertical':
			wincon.FindElement("Vertical").Update(button_color=('White','DarkBlue'))
			wincon.FindElement("Horizontal").Update(button_color=('Black','LightGrey'))
			vert=True
		if event=='act':
			wincon.FindElement("act").Update(button_color=('White','DarkBlue'))
			wincon.FindElement("des").Update(button_color=('Black','LightGrey'))
			ayuda=True
		if event=='des':
			wincon.FindElement("des").Update(button_color=('White','DarkBlue'))
			wincon.FindElement("act").Update(button_color=('Black','LightGrey'))
			ayuda=False
		if event=='caps':
			wincon.FindElement("caps").Update(button_color=('White','DarkBlue'))
			wincon.FindElement("min").Update(button_color=('Black','LightGrey'))
			caps=True
		if event=='min':
			wincon.FindElement("min").Update(button_color=('White','DarkBlue'))
			wincon.FindElement("caps").Update(button_color=('Black','LightGrey'))
			caps=False
		if event=='Ingresar palabras':
			pal=[[sg.Input(key='palabra'),sg.Button('Ingresar')],
				[sg.Table(Values=lista,headings=['Palabra','Tipo'],key='tabla')],
				[sg.Input(key='elim'),sg.Button('Eliminar')],
				[sg.Button('Aceptar')]]
			winpal=Window('Ingresar Palabras',pal)
			while True:
				event,values=winpal.Read()
				if event=='Aceptar' or event is None:
					break
				if event=='Ingresar':
					result=engine.search(values['palabra'])
					if result is not None:
						tipo=result.sections[3].string[0:10]
						lista.append([result.title,result.sections[3].string])
						compararConPattern(tipo)
					else:
						if values['palabra'] in pattern.es:
							tipo=parse(palabra)
							defin=input('No se encontró en Wiktionary, por favor ingrese una definición de la palabra')
							lista.append([values['palabra'],tipo,defin])
						else:
							print('Palabra no válida')
					winpal.FindElement('tabla').Update(values=lista)
			winpal.Close()
		if event=='Verificar palabras':
			if (int(values['verb'])>cant['verb'] or int(values['adj'])>cant['adj'] or int(values['sus'])>cant['sus']):
				sg.Popup('No hay palabras suficientes ingresadas')
				values['verb']=cant['verb']
				values['adj']=cant['adj']
				values['sus']=cant['sus']
				wincon.FindElement('verb').Update(values['verb'])
				wincon.FindElement('adj').Update(values['adj'])
				wincon.FindElement('sus').Update(values['sus'])
			else:
				wincon.FindElement('Aceptar').Update(disabled=False)
	wincon.Close()
layout=[[sg.Text("Sopa de letras")],
		[sg.Button('Configuración'),sg.Button('Jugar'),sg.Button('Salir')]]
window=sg.Window('Sopa de letras',layout)
while True:
	event,values=window.Read()
	if event is None or event=='Salir':
		break
	if event == 'Configuración':
		config()
	if event == 'Jugar':
		play()
window.Close()

w = Wiktionary(language='es')
palabra='gato'
