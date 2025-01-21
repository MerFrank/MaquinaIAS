# Parte de Owen. 
#El acumulador y la memoria(es un diccionario para simular los espacios) deben ser globales
acumulador = -10
memoria = {}

# LOAD Absoluto
def load_abs(adress):
    global acumulador
    if adress in memoria:
        valor = memoria[adress]
        acumulador = abs(valor)
        print(f"LOAD ha sido ejecutado. Dirección: {hex(adress)}, valor {valor}, acumulador {acumulador}")
    else:
        print(f"ERROR. LOAD no ha sido ejecutado. La dirección: {hex(adress)} no existe en la memoria")

def load_abs_neg(adress):
    global acumulador
    if adress in memoria:
        valor = memoria[adress]
        acumulador = -abs(valor)
        print(f"LOAD -ABS ha sido ejecutado. Dirección: {hex(adress)}, valor {valor}, acumulador {acumulador}")
    else:
        print(f"ERROR. LOAD -ABS no ha sido ejecutado. La dirección: {hex(adress)} no existe en la memoria")

def ext_left(word):
    mitad_left = word >> 20
    return mitad_left

def ext_right(word):
    mask = 0xFFFFF
    mitad_right = word & mask
    return mitad_right

def jump_left(adress):
    global acumulador
    if adress in memoria:
        palabra = memoria[adress]
        siguiente = ext_left(palabra)
        acumulador = siguiente
        print(f"JUMP ha sido ejecutado. Palabra completa {bin(palabra)}")
        print(f"Mitad izquierda extraída {bin(siguiente)}")
        print(f"Nueva dirección del acumulador {hex(acumulador)}")
    else:
        print(f"ERROR. JUMP no ha sido ejecutado. No se pudo leer la dirección {hex(adress)}")
        
def jump_right(adress):
    global acumulador
    if adress in memoria:
        palabra = memoria[adress]
        siguiente = ext_right(palabra)
        acumulador = siguiente
        print(f"JUMP ha sido ejecutado. Palabra completa {bin(palabra)}")
        print(f"Mitad derecha extraída {bin(siguiente)}")
        print(f"Nueva dirección del acumulador {hex(acumulador)}")
    else:
        print(f"ERROR. JUMP no ha sido ejecutado. No se pudo leer la dirección {hex(adress)}")
        
def jump_left_con(adress):
    global acumulador
    if acumulador >= 0:
        if adress in memoria:
            palabra = memoria[adress]
            siguiente = ext_left(palabra)
            acumulador = siguiente
            print(f"JUMP ha sido ejecutado. Palabra completa {bin(palabra)}")
            print(f"Mitad izquierda extraída {bin(siguiente)}")
            print(f"Nueva dirección del acumulador {hex(acumulador)}")
        else:
            print(f"ERROR. JUMP no ha sido ejecutado. No se pudo leer la dirección {hex(adress)}")
    else:
        print(f"El acumulador es negativo")



#Funcion DIV_M(X) (Estefani)
#nombre de la funcion 
def DIV_M (AC, X):
    MQ = AC / X   #se hace la division
    AC = AC % X # se calcula el resto de la division
    return MQ, AC 

def STOR (D) :
    global AC
    if D in memoria:
        AC=memoria[D]
        print(f"Nuevo valor del acomulador:",AC)
    else:
        print("Error, la direccion no existe en la memoria ")
    #REVISAR FUNCIONES, PUEDEN ESTAR INCOMPLETAS
def LSH (AC):
    
    res = AC *2# se multiplica el acomulador por 2
    return res

def RSH (AC):
    
    res = AC / 2# se divide el acomulador por 2
    return res

#Codigos de yes
# Instrucción 1: LOAD MQ
def load_mq():
    """
    Transfiere el contenido del registro MQ al acumulador.
    """
    global acumulador, MQ
    acumulador = MQ
    print(f"LOAD MQ ejecutado. MQ: {MQ}, acumulador: {acumulador}")

# Instrucción 2: LOAD MQ, M(X)
def load_mq_mem(address):
    """
    Transfiere el contenido de la posición de memoria X a MQ.
    """
    global MQ
    if address in memoria:
        MQ = memoria[address]
        print(f"LOAD MQ, M({hex(address)}) ejecutado. MQ: {MQ}")
    else:
        print(f"ERROR: Dirección {hex(address)} no encontrada en memoria.")

# Instrucción 3: STOR M(X)
def stor_mem(address):
    """
    Transfiere el contenido del acumulador a la posición de memoria X.
    """
    global acumulador, memoria
    memoria[address] = acumulador
    print(f"STOR M({hex(address)}) ejecutado. Memoria[{hex(address)}]: {memoria[address]}")

# Instrucción 4: LOAD M(X)
def load_mem(address):
    """
    Transfiere el contenido de M(X) al acumulador.
    """
    global acumulador, memoria
    if address in memoria:
        acumulador = memoria[address]
        print(f"LOAD M({hex(address)}) ejecutado. Acumulador: {acumulador}")
    else:
        print(f"ERROR: Dirección {hex(address)} no encontrada en memoria.")

# Instrucción 5: LOAD -M(X)
def load_neg_mem(address):
    """
    Transfiere el valor negativo de M(X) al acumulador.
    """
    global acumulador, memoria
    if address in memoria:
        acumulador = -memoria[address]
        print(f"LOAD -M({hex(address)}) ejecutado. Acumulador: {acumulador}")
    else:
        print(f"ERROR: Dirección {hex(address)} no encontrada en memoria.")



#Codigos de prueba
if __name__ == "__main__":
    # Ejemplo: creamos una palabra de 40 bits
    # Usando números binarios para mejor visualización
    # Por ejemplo: 40 bits divididos en:
    # - 20 bits izquierda: 10101 (instrucción 1)
    # - 20 bits derecha:   00110 (instrucción 2)
    memoria[0x01] = 0b10101000000000000000000110000000000000000

    print(f"acumulador antes del salto: {hex(acumulador)}")
    jump_left_con(0x01)
    print(f"acumulador después del salto: {hex(acumulador)}")



    #CODIGO PARA PROBAR INSTRUCCIONES ARITMETICAS   
if __name__ == "__main__":
    # Configuramos algunos valores en la memoria
    memoria[0x01] = -15
    memoria[0x02] = 20
    memoria[0x03] = 0

    # Ejecutamos la instrucción LOAD o la que se decida (Debe modificarse el codigo)
    print("Antes de ejecutar LOAD:")
    print(f"Acumulador: {acumulador}")
    load_abs_neg(0x01)  # Cargar desde dirección 0x01
    print("Después de ejecutar LOAD:")
    print(f"Acumulador: {acumulador}")