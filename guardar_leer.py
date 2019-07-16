import os
import json
import time
from matriz import Matriz
from sonido import Sonido
from temperatura import Temperatura

matriz = Matriz()
sonido = Sonido()
temperatura = Temperatura()

def acciones():
    print ("Sonido Detectado!")
    temp_data = temperatura.datos_sensor()
    temp_formateada = 'Temperatura = {0:0.1f}°C  Humedad = {1:0.1f}%'.format(temp_data['temperatura'], temp_data['humedad'])
    matriz.mostrar_mensaje(temp_formateada, delay=0.08, font=2)
    
def leer_temp():
    info_temperatura = temperatura.datos_sensor()
    info_temperatura.update({"fecha": str(time.asctime(time.localtime(time.time())))})
    return info_temperatura
 
def guardar_temp(info):
    with open(os.path.join("archivos_texto", "ultimo_log_temperatura.json"), "r") as log_file:
        try:
            lista_de_temperaturas = json.load(log_file)
        except Exception:
            # En caso de que el json no sea una lista
            lista_de_temperaturas = []
    lista_de_temperaturas.append(info)
    with open(os.path.join("archivos_texto", "ultimo_log_temperatura.json"), "w") as log_file:
        json.dump(lista_de_temperaturas, log_file, indent=4)

ahora=time.time()
while True:
	if time.time()-ahora<10:
		time.sleep(0.1)
		sonido.evento_detectado(acciones)
	else:
		temp = leer_temp()
        guardar_temp(temp)
		ahora=time.time()
	
