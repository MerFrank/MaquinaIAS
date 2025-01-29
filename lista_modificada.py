
from traductor import *
import re

def instrucciones_valor(lista_modificada, lista_instrucciones):
    for linea in lista_instrucciones:
        # Patrón para instrucciones simples como LOAD M(103)
        match_simple = re.match(r"([A-Z\s]+)\(([^)]+)\)", linea)
        if match_simple:  # Si coincide con el formato simple
            valor_dinamico = match_simple.group(2)      # Extraemos el valor dinámico (ej: 5 o 'x') 
            direccion = int(valor_dinamico) - 100
            valor_texto = lista_memoria[direccion]
            valor_numero = int(''.join(filter(str.isdigit, valor_texto)))
            instruccion_modificada = re.sub(r'\(.*?\)', f'({valor_numero})', linea)
            lista_modificada.append(instruccion_modificada)
        
        # Patrón para instrucciones complejas como JUMP M(10, 20:39)
        match_complejo = re.match(r"([A-Z]+)\s*\+\s*M\s*\(([^,]+),\s*(\d+:\d+)\)", linea)
        if match_complejo: 
            parte_fija = match_complejo.group(1).strip()  # Extraemos la parte fija (ej: "JUMP M")
            valor_dinamico = match_complejo.group(2)      # Extraemos el valor dinámico (ej: 10 o 'x')
            parte_fija_parentesis = match_complejo.group(3)  # Extraemos la parte fija dentro del paréntesis (ej: 20:39)
            if parte_fija in ["JUMP M", "JUMP + M", "STOR M"]:
                lista_modificada.append(linea)
        

    return lista_modificada

instrucciones_valor(lista_modificada, lista_instrucciones)
print("/n")
print(lista_modificada)