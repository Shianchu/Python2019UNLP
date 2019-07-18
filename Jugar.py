import PySimpleGUI as sg
import random as ran
import string
import time

def play(listita,cant,vert,caps,ayuda,color):

	lista=[]
	defi=[]
	tipo=[]
	while not cant==[0,0,0]:
		i=ran.randrange(1,len(listita))
		palabra=listita[i]
		if caps:
			palabra[0]=palabra[0].upper()
		else:
			palabra[0]=palabra[0].lower()
		if not (palabra[0] in lista):
			if palabra[1]=='sustantivo':
				if cant[0]>0:
					cant[0]=cant[0]-1
					lista.append(palabra[0])
					tipo.append(palabra[1])
					defi.append(palabra[2])
			else:
				if palabra[1]=='adjetivo':
					if cant[1]>0:
						cant[1]=cant[1]-1
						lista.append(palabra[0])
						tipo.append(palabra[1])
						defi.append(palabra[2])
				else:
					if palabra[1]=='verbo':
						if cant[2]>0:
							cant[2]=cant[2]-1
							lista.append(palabra[0])
							tipo.append(palabra[1])
							defi.append(palabra[2])
			
	
	if(caps):
		for i in lista:
			i=i.upper()
	else:
		for i in lista:
			i=i.lower()

	def dimensiones(listaPal):
	    max=0
	    for i in listaPal:
	        if len(i) >= max:
	            max= len(i)
	    cantPalabras= len(listaPal)
	    return (max,cantPalabras)



	tupla = dimensiones(lista)
	if vert:
		x,y= tupla[0],tupla[1]
	else:
		y,x= tupla[0],tupla[1]

	def haceMatriz(posUno, posDos, pruebita,tipo,listaMatrices,maxY):#Mete a la matriz la palabra enviada
		if(len(pruebita)==len(listaMatrices[0][posUno])):
			for i in range(len(pruebita)):
				if vert:
					listaMatrices[0][posUno][posDos-i]=pruebita[i]
					listaMatrices[1][posUno][posDos-i]=tipo
				else:
					listaMatrices[0][posUno][i]=str(pruebita[i])
					listaMatrices[1][posUno][i]=tipo
		else:
			if caps:
				if vert:
					for i in range(int(posDos+0.5),maxY):
						char= ran.choice(string.ascii_uppercase)
						listaMatrices[0][posUno][posDos-i-1]=char
				else:
					for i in range(0,int(posDos+0.5)):
						char= ran.choice(string.ascii_uppercase)
						listaMatrices[0][posUno][i]=char
			else:
				if vert:
					for i in range(int(posDos+0.5),maxY):
						char= ran.choice(string.ascii_lowercase)
						listaMatrices[0][posUno][posDos-i-1]=char
				else:
					for i in range(0,int(posDos+0.5)):
						char= ran.choice(string.ascii_lowercase)
						listaMatrices[0][posUno][i]=char
			if caps:
				if vert:
					for i in range(0,int(posDos+0.5-len(pruebita))+1):
						char= ran.choice(string.ascii_uppercase)
						listaMatrices[0][posUno][i]=char
				else:
					for i in range(int(posDos+0.5+len(pruebita)),maxY):
						char= ran.choice(string.ascii_uppercase)
						listaMatrices[0][posUno][i]=char
			else:
				if vert:
					for i in range(0,int(posDos+0.5-len(pruebita))+1):
						char= ran.choice(string.ascii_lowercase)
						listaMatrices[0][posUno][i]=char
				else:
					for i in range(int(posDos+0.5+len(pruebita)),maxY):
						char= ran.choice(string.ascii_lowercase)
						listaMatrices[0][posUno][i]=char
			for i in range(len(pruebita)):
				if vert:
					listaMatrices[0][posUno][posDos-i]=pruebita[i]
					listaMatrices[1][posUno][posDos-i]=str(tipo)
				else:
					listaMatrices[0][posUno][posDos+i]=pruebita[i]
					listaMatrices[1][posUno][posDos+i]=tipo

		return listaMatrices

	listaMatrices= [[],[],[]]

	layout=[[sg.Graph(canvas_size=(30*y,30*x), graph_bottom_left=(-0.1,-0.1), graph_top_right=(y+0.1,x+0.1), background_color='White', enable_events= True, key= 'graph', visible= True)],
			[sg.Button('Ayuda',disabled=True,key='Ayuda')],
			[sg.Button('Sustantivo',button_color=('White',color['sustantivo'])),sg.Button('Adjetivo',button_color=('White',color['adjetivo'])),sg.Button('Verbo',button_color=('White',color['verbo']))],
			[sg.Cancel('Salir'),sg.Button('Verificar')]]

	win=sg.Window('Grafiquito',layout).Finalize()
	grafo=win.Element('graph')
	if ayuda:
		win.FindElement('Ayuda').Update(disabled=False)

	for j in range(y+1):
		grafo.DrawLine((j,0),(j,x),color='Black', width= 1)
	for j in range(x+1):
		grafo.DrawLine((0,j),(y,j),color= 'Black', width = 1)

	if vert:
		listaMatrices[0]= [[':c' for uno in range(x)] for dos in range(y)]#la matriz de las palabras
		listaMatrices[1]= [[':c' for uno in range(x)] for dos in range(y)]#la matriz con los tipos de palabra
		listaMatrices[2]= [[':c' for uno in range(x)] for dos in range(y)]#la matriz con los estados actuales de la grilla
	else:
		listaMatrices[0]= [[':c' for uno in range(y)] for dos in range(x)]#la matriz de las palabras
		listaMatrices[1]= [[':c' for uno in range(y)] for dos in range(x)]#la matriz con los tipos de palabra
		listaMatrices[2]= [[':c' for uno in range(y)] for dos in range(x)]#la matriz con los estados actuales de la grilla
	for i in range(0,len(lista)):
		if vert:
			inicioY= (ran.randrange((len(lista[i]))-1,x))+0.5
			listaMatrices=haceMatriz(int(i+0.5),int(inicioY-0.5),lista[i],tipo[i],listaMatrices,x)
		else:
			inicioY= (ran.randrange(0,y-(len(lista[i])-1)))+0.5
			listaMatrices=haceMatriz(int(i+0.5),int(inicioY-0.5),lista[i],tipo[i],listaMatrices,y)
	go=False
	actual='sustantivo'
	for i in range(0,y):
		for j in range(0,x):
			if vert:
				grafo.DrawText(listaMatrices[0][i][j],(i+0.5,j+0.5))
			else:
				grafo.DrawText(listaMatrices[0][j][i],(i+0.5,j+0.5))
	while True:
		event,values = win.Read()
		if event == 'Verificar':
			if listaMatrices[1]==listaMatrices[2]:
				sg.Popup('Felicidades, completaste el juego!')
				break
			else:
				errores={'sustantivo':0,'adjetivo':0,'verbo':0,':c':0}
				for i in range(len(listaMatrices[1])):
					for j in range(len(listaMatrices[1][i])):
						if  not (listaMatrices[1][i][j]==listaMatrices[2][i][j]):
							print(listaMatrices[2][i][j])
							print(listaMatrices[1][i][j])
							errores[listaMatrices[1][i][j]]=errores[listaMatrices[1][i][j]]+1
				sg.Popup('No es la solucion correcta, hay ' + str(errores['sustantivo']) + ' letras de sustantivo sin marcar correctamente, ' + str(errores['adjetivo']) + ' de adjetivos y ' + str(errores['verbo']) + ' de verbos, hay ' + str(errores[':c']) + ' letras marcadas que no forman parte de una palabra')
		if event == 'Ayuda':
			defino=''
			for i in defi:
				defino=defino+i+'\n'
			sg.Popup(defino)
		if event == 'Sustantivo':
			actual='sustantivo'
		if event == 'Adjetivo':
			actual='adjetivo'
		if event == 'Verbo':
			actual='verbo'
		if event == 'graph':
			if(not values['graph'][0]==None):
				posx=int(values['graph'][0])
				posy=int(values['graph'][1])
			if posx in range(y) and posy in range(x):
				if go:	
					if vert:
						if listaMatrices[2][posx][posy]==actual:
							grafo.DrawRectangle(top_left=(posx,posy+1),bottom_right=(posx+1,posy),fill_color='White',line_color=None)
							listaMatrices[2][posx][posy]=':c'
						else:
							grafo.DrawRectangle(top_left=(posx,posy+1),bottom_right=(posx+1,posy),fill_color=color[actual],line_color=None)
							listaMatrices[2][posx][posy]=actual
						go=False
					else:
						if listaMatrices[2][posy][posx]==actual:
							grafo.DrawRectangle(top_left=(posx,posy+1),bottom_right=(posx+1,posy),fill_color='White',line_color=None)
							listaMatrices[2][posy][posx]=':c'
						else:
							grafo.DrawRectangle(top_left=(posx,posy+1),bottom_right=(posx+1,posy),fill_color=color[actual],line_color=None)
							listaMatrices[2][posy][posx]=actual
					go=False
				else:
					go=True
				if vert:
					grafo.DrawText(listaMatrices[0][posx][posy],(posx+0.5,posy+0.5))
				else:
					grafo.DrawText(listaMatrices[0][posy][posx],(posx+0.5,posy+0.5))

		if event == None or event=='Salir':
			break

	win.Close()
