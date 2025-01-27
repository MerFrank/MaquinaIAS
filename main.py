from diccionario import *

import re  # Importamos el módulo de expresiones regulares

# Diccionario de funciones (simuladas)
def load_mq_m(x):
    print(f"Ejecutando LOAD MQ M con el valor: {x}")

def add_m(x):
    print(f"Ejecutando ADD M con el valor: {x}")

# Diccionario de instrucciones (clave: parte fija, valor: función)
dic_intrucciones = {
    "LOAD MQ M": load_mq_m,
    "ADD M": add_m,
}

# Lista de instrucciones (simulada)
lista_instrucciones = [
    "LOAD MQ M(5)",
    "ADD M(10)",
    "LOAD MQ M(20)",
    "SUB M(15)",  # Esta instrucción no está en el diccionario
]

# Función para procesar las instrucciones
def procesar_instrucciones(lista_instrucciones, dic_intrucciones):
    for linea in lista_instrucciones:
        # Usamos una expresión regular para extraer la parte fija y el valor dinámico
        match = re.match(r"([A-Z\s]+)\((\d+)\)", linea)
        if match:
            parte_fija = match.group(1).strip()  # Extraemos la parte fija (ej: "LOAD MQ M")
            valor = int(match.group(2))         # Extraemos el valor dinámico (ej: 5)

            # Verificamos si la parte fija está en el diccionario
            if parte_fija in dic_intrucciones:
                # Ejecutamos la función asociada y pasamos el valor dinámico
                dic_intrucciones[parte_fija](valor)
            else:
                print(f"Instrucción no encontrada: {linea}")
        else:
            print(f"Formato de instrucción no válido: {linea}")

# Procesamos las instrucciones
procesar_instrucciones(lista_instrucciones, dic_intrucciones)