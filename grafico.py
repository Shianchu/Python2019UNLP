import PySimpleGUI as sg
import random as ran
import string

def columnas(pal,aux,tup):
	inicioX= (ran.randrange(tup[1]))
	while(inicioX in aux):
		inicioX=(ran.randrange(tup[1]))
	print(inicioX)
	if (len(pal) == tup[1]):
		for i in range(tup[1]):
			grafo.DrawText(pal[i],(inicioX+0.5,tup[1]-0.5-i))
	else:
		print('tup:',tup[1])
		print('len:',len(pal))
		print(tup[1]-len(pal))
		inicioY= (ran.randrange(0,(tup[1]-len(pal))+1))
		print('inicioy')
		print(inicioY)
		for i in range(inicioY):
			char= ran.choice(string.ascii_lowercase)
			grafo.DrawText(char, (inicioX+0.5,tup[1]-i-0.5))
		for i in range(len(pal)):
			grafo.DrawText(pal[i],(inicioX+0.5,tup[1]-inicioY-i-0.5))
			aux.append(inicioX)
		for i in range(inicioY+len(pal),tup[1]):
		 	char= ran.choice(string.ascii_lowercase)
		 	grafo.DrawText(char, (inicioX+0.5,tup[1]-i-0.5))

def filas(pal,aux,tup):
	print('tupla 1',tup[1])
	inicioY= (ran.randrange(tup[1]))
	print('inicioY',inicioY)
	while(inicioY in aux):
		print('ya dibuje algo en la coordenada Y')
		inicioY=(ran.randrange(tup[1]))
	print('tupla 0',tup[0])
	if (len(pal) == tup[0]):
		print('tamanio de palabra igual a longitud')
		for i in range(tup[0]):
			grafo.DrawText(pal[i],(0+i+0.5,inicioY+0.5))
	else:
		inicioX= (ran.randrange(0,(tup[0]-len(pal)-1)))
		print('inicioX',inicioX)
		print(len(pal))
		for i in range(inicioX):
			print('range pal alazar antes de palabra ingresada ',i)
			char= ran.choice(string.ascii_lowercase)
			grafo.DrawText(char, (i+0.5,inicioY+0.5))
		for i in range(len(pal)):
			print('range de len pal: ',i)
			grafo.DrawText(pal[i],(inicioX+i+0.5,inicioY+0.5))
			aux.append(inicioY)
		for i in range(inicioX+len(pal),tup[0]):
			print('i',i)
			char= ran.choice(string.ascii_lowercase)
			grafo.DrawText(char, (i+0.5,inicioY+0.5))


def dimensiones(listaPal):
    max=0
    for i in listaPal:
        if len(i) >= max:
            max= len(i)
    cantPalabras= len(listaPal)
    return (max,cantPalabras)

lista=['gato','perro','elefante','cocodrilo','lobo','abeja','preoperatorio']

tupla = dimensiones(lista)

layout=[[sg.Graph(canvas_size=(40*tupla[0],40*tupla[1]), graph_bottom_left=(-0.1,-0,1), graph_top_right=(tupla[0],tupla[1]+0.1), enable_events= True, key= 'graph', visible= True)],
		[sg.Text('New Palabra-->'),sg.Input(key= 'Input'),sg.Button('Aceptar')],
		[sg.Text('(Maximo de 15 palabras)')],
		[sg.Cancel('Cancelar')]]

win=sg.Window('Grafiquito',layout).Finalize()
grafo=win.Element('graph')

pos=True
BOX_SIZE = 25

def dibujar(x):
	print(x)
	for j in range(x+1):
		grafo.DrawLine((j,0),(j,x),color='Black', width= 1)
		grafo.DrawLine((0,j),(x,j),color= 'Red', width = 1)

def dibujarA(x,y):
	for row in range(y):
		for col in range(x):
			grafo.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
			#grafo.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black', fill_color='black')
if pos:
	dibujar(tupla[0])
else:
	print('entre aca')
	dibujarA(tupla[0],tupla[1])





auxX= []
auxY= []


while True:
	event,values = win.Read()
	if event == 'graph':
		#grafo.Update((values['graph'],'Black'))
		if(not values['graph'][0]==None):
			posx=int(values['graph'][0])
			posy=int(values['graph'][1])
		grafo.DrawRectangle(top_left=(posx,posy+1),bottom_right=(posx+1,posy),fill_color='white',line_color=None)
		print(posx,posy)
	if event == None or event=='Cancelar':
		break
	if event == 'Aceptar':#lo modifique, no toma la palabra que le pongas pero escribe la lista de todas las palabras
		for i in lista:
			filas(i,auxY,tupla)
		#pal= values['Input']
		#columnas(pal,auxY,tupla)
		#filas(pal,auxY,tupla)
