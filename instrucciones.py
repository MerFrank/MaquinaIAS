from instrucciones import *
#El acumulador y la memoria(es un diccionario para simular los espacios) deben ser globales
acumulador = -10
memoria = {}

# LOAD Absoluto
def load_abs(address):
    global acumulador
    if address in memoria:
        valor = memoria[address]
        acumulador = abs(valor)
        print(f"LOAD ha sido ejecutado. Dirección: {hex(address)}, valor {valor}, acumulador {acumulador}")
    else:
        print(f"ERROR. LOAD no ha sido ejecutado. La dirección: {hex(address)} no existe en la memoria")

def load_abs_neg(address):
    global acumulador
    if address in memoria:
        valor = memoria[address]
        acumulador = -abs(valor)
        print(f"LOAD -ABS ha sido ejecutado. Dirección: {hex(address)}, valor {valor}, acumulador {acumulador}")
    else:
        print(f"ERROR. LOAD -ABS no ha sido ejecutado. La dirección: {hex(address)} no existe en la memoria")

def ext_left(word):
    mitad_left = word >> 20
    return mitad_left

def ext_right(word):
    mask = 0xFFFFF
    mitad_right = word & mask
    return mitad_right

def jump_left(address):
    global acumulador
    if address in memoria:
        palabra = memoria[address]
        siguiente = ext_left(palabra)
        acumulador = siguiente
        print(f"JUMP ha sido ejecutado. Palabra completa {bin(palabra)}")
        print(f"Mitad izquierda extraída {bin(siguiente)}")
        print(f"Nueva dirección del acumulador {hex(acumulador)}")
    else:
        print(f"ERROR. JUMP no ha sido ejecutado. No se pudo leer la dirección {hex(address)}")
        
def jump_right(address):
    global acumulador
    if address in memoria:
        palabra = memoria[address]
        siguiente = ext_right(palabra)
        acumulador = siguiente
        print(f"JUMP ha sido ejecutado. Palabra completa {bin(palabra)}")
        print(f"Mitad derecha extraída {bin(siguiente)}")
        print(f"Nueva dirección del acumulador {hex(acumulador)}")
    else:
        print(f"ERROR. JUMP no ha sido ejecutado. No se pudo leer la dirección {hex(address)}")
        
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

#JUMP + M(X,20:39)

def jump_right_con(adress):
    global acumulador
    if acumulador >= 0:
        if adress in memoria:
            palabra = memoria[adress]
            siguiente = ext_right(palabra)
            acumulador = siguiente
            print(f"JUMP  + M(X,20:39) ha sido ejecutado. Palabra completa {bin(palabra)}")
            print(f"Mitad derecha extraída {bin(siguiente)}")
            print(f"Nueva dirección del acumulador {hex(acumulador)}")
        else:
            print(f"ERROR. JUMP  + M(X,20:39) no ha sido ejecutado. No se pudo leer la dirección {hex(adress)}")
    else:
        print(f"El acumulador es negativo")


#ADD M(X)

def add_m(adress):
    global acumulador
    if adress in memoria:
        valor = memoria[adress]
        acumulador += valor
        print(f"ADD M(X) ha sido ejecutado. Dirección: {hex(adress)}, valor {valor}")
        print(f"Acumulador después de la suma: {acumulador}")
    else:
        print(f"ERROR. ADD M(X) no ha sido ejecutado. La dirección: {hex(adress)} no existe en la memoria")

#ADD |M(X)|

def add_abs_m(adress):
    global acumulador
    if adress in memoria:
        valor = abs(memoria[adress])  # Valor absoluto de M(X)
        acumulador += valor
        print(f"ADD |M(X)| ha sido ejecutado. Dirección: {hex(adress)}, valor absoluto {valor}")
        print(f"Acumulador después de la suma: {acumulador}")
    else:
        print(f"ERROR. ADD |M(X)| no ha sido ejecutado. La dirección: {hex(adress)} no existe en la memoria")

#SUB M(X)

def sub_m(adress):
    global acumulador
    if adress in memoria:
        valor = memoria[adress]
        acumulador -= valor
        print(f"SUB M(X) ha sido ejecutado. Dirección: {hex(adress)}, valor {valor}")
        print(f"Acumulador después de la resta: {acumulador}")
    else:
        print(f"ERROR. SUB M(X) no ha sido ejecutado. La dirección: {hex(adress)} no existe en la memoria")

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
def STOR (I) :
    global AC
    if I in memoria:
        AC=memoria[I]
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



