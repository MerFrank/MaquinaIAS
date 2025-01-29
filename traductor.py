import os
import re
# Nombre del archivo
archivo = "ejemplo_instrucciones.txt"
lista_instrucciones = []
lista_memoria =[]
lista_modificada = []

def dividir_instrucciones_memoria(archivo):    
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
    return lista_instrucciones, lista_memoria

dividir_instrucciones_memoria(archivo)


# def instrucciones_valor(lista_modificada, lista_instrucciones):
#     for linea in lista_instrucciones:
#         #linea : LOAD M(103)
#         match_simple = re.match(r"([A-Z\s]+)\(([^)]+)\)", linea)
#         if match_simple:  # Si coincide con el formato simple
#             valor_dinamico = match_simple.group(2)      # Extraemos el valor dinámico (ej: 5 o 'x') 
#             direccion = int(valor_dinamico)
#             direccion = direccion - 100
#             valor_texto = lista_memoria[direccion]
#             valor_numero = int(''.join(filter(str.isdigit, valor_texto)))
#             instruccion_modificada = re.sub(r'\(.*?\)',f'({valor_numero})', linea)
#             lista_modificada.append(instruccion_modificada)
        
#     return lista_modificada

# dividir_instrucciones_memoria(archivo)

print(lista_instrucciones)
# print("/n")
# print(lista_memoria)

