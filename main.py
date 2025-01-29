from diccionario import *
from lista_modificada import *
import re  # Importamos el módulo de expresiones regulares


def procesar_instrucciones(lista_instrucciones, dic_intrucciones):
    for linea in lista_instrucciones:
        # Caso 1: Instrucciones con formato JUMP M(x,20:39)
        match_complejo = re.match(r"([A-Z\s]+)\(([^,]+),(\d+:\d+)\)", linea)
        # Caso 2: Instrucciones con formato LOAD MQ(x)
        match_simple = re.match(r"([A-Z\s]+)\(([^)]+)\)", linea)

        if match_complejo:  # Si coincide con el formato complejo
            parte_fija = match_complejo.group(1).strip()  # Extraemos la parte fija (ej: "JUMP M")
            valor_dinamico = match_complejo.group(2)      # Extraemos el valor dinámico (ej: 10 o 'x')
            parte_fija_parentesis = match_complejo.group(3)  # Extraemos la parte fija dentro del paréntesis (ej: 20:39)

            if parte_fija in dic_intrucciones:
                # Ejecutamos la función asociada y pasamos ambos valores
                dic_intrucciones[parte_fija](f"{valor_dinamico},{parte_fija_parentesis}")
            else:
                print(f"Instrucción no encontrada: {linea}")

        elif match_simple:  # Si coincide con el formato simple
            parte_fija = match_simple.group(1).strip()  # Extraemos la parte fija (ej: "LOAD MQ")
            valor_dinamico = match_simple.group(2)      # Extraemos el valor dinámico (ej: 5 o 'x')

            if parte_fija in dic_intrucciones:
                # Ejecutamos la función asociada y pasamos el valor dinámico
                dic_intrucciones[parte_fija](valor_dinamico)
            else:
                print(f"Instrucción no encontrada: {linea}")

        else:
            print(f"Formato de instrucción no válido: {linea}")

# Procesamos las instrucciones
procesar_instrucciones(lista_instrucciones, dic_intrucciones)