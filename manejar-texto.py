import os
# Nombre del archivo
archivo = "ejemplo_instrucciones.txt"
lista_instrucciones = []
lista_memoria =[]

def dividir_instrcciones_memoria(archivo):    
    guardar_en_lista_instrucciones = True
    with open(archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "HALT":
                guardar_en_lista_instrucciones = False
                continue
            if guardar_en_lista_instrucciones:
                lista_instrucciones.append(linea)
            else:
                lista_memoria.append(linea)