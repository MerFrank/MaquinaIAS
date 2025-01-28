
from traductor import lista_instrucciones, lista_memoria
import re
lista_modificada = []


def instrucciones_valor(lista_modificada, lista_instrucciones):
    for linea in lista_instrucciones:
        #linea : LOAD M(103)
        match_simple = re.match(r"([A-Z\s]+)\(([^)]+)\)", linea)
        if match_simple:  # Si coincide con el formato simple
                valor_dinamico = match_simple.group(2)      # Extraemos el valor dinámico (ej: 5 o 'x') 
                direccion = int(valor_dinamico)
                direccion = direccion - 100
                valor_texto = lista_memoria[direccion]
                valor_numero = int(''.join(filter(str.isdigit, valor_texto)))
                instruccion_modificada = re.sub(r'\(.*?\)',f'({valor_numero})', linea)
                lista_modificada.append(instruccion_modificada)
                