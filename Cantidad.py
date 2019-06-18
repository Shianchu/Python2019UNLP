lista=['gato','perro','elefante','cocodrilo','lobo']

def dimensiones(listaPal):
    max=0
    for i in listaPal:
        if len(i) >= max:
            max= len(i)
    cantPalabras= len(listaPal)
    return (max,cantPalabras)

tupla = dimensiones(lista)
print(tupla)
print(tupla[0])
print(tupla[1])
