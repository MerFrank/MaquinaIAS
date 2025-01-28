from traductor import *
#El acumulador y la memoria(es un diccionario para simular los espacios) deben ser globales
acumulador = 0
mq = 0



#Yes aquí pone tuy0 

def vd_convertir_a_hexadecimal(variable):
    try:
        # Intentar convertir a entero para verificar si es decimal
        numero_decimal = int(variable)
        # Si se puede convertir, convertir a hexadecimal
        return hex(numero_decimal)
    except ValueError:
        # Si no es decimal, devolver None
        print(f"'{variable}' no es un número decimal válido.")
        return None



def vh_convertir_a_decimal(num):
    try:
# Intentamos convertir el número a decimal usando base 16, int(num, 16) toma el valor num y lo interpreta como un número hexadecimal el 16 es de la base que es hexadecimal, si la conversión esta bien se almacena el resultado en la variable decimal y la función devuelve ese valor.
        decimal = int(num, 16)
        return decimal
    except ValueError:
        # Si ocurre un error, es porque no es hexadecimal
        return "Error: El número no es hexadecimal válido."
        
numero = input("Introduce un número hexadecimal: ")
resultado = vh_convertir_a_decimal(numero)
print(resultado)

###
#:) voy gracias 


# LOAD Absoluto
def load_abs(address):
    global acumulador
    if address in lista_memoria:
        valor = lista_memoria[address]
        acumulador = abs(valor)
        print(f"LOAD ha sido ejecutado. Dirección: {hex(address)}, valor {valor}, acumulador {acumulador}")
    else:
        print(f"ERROR. LOAD no ha sido ejecutado. La dirección: {hex(address)} no existe en la memoria")

def load_abs_neg(address):
    global acumulador
    if address in lista_memoria:
        valor = lista_memoria[address]
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
    if address in lista_memoria:
        palabra = lista_memoria[address]
        siguiente = ext_left(palabra)
        acumulador = siguiente
        print(f"JUMP ha sido ejecutado. Palabra completa {bin(palabra)}")
        print(f"Mitad izquierda extraída {bin(siguiente)}")
        print(f"Nueva dirección del acumulador {hex(acumulador)}")
    else:
        print(f"ERROR. JUMP no ha sido ejecutado. No se pudo leer la dirección {hex(address)}")
        
def jump_right(address):
    global acumulador
    if address in lista_memoria:
        palabra = lista_memoria[address]
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
        if adress in lista_memoria:
            palabra = lista_memoria[adress]
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
        if adress in lista_memoria:
            palabra = lista_memoria[adress]
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
    if adress in lista_memoria:
        valor = lista_memoria[adress]
        acumulador += valor
        print(f"ADD M(X) ha sido ejecutado. Dirección: {hex(adress)}, valor {valor}")
        print(f"Acumulador después de la suma: {acumulador}")
    else:
        print(f"ERROR. ADD M(X) no ha sido ejecutado. La dirección: {hex(adress)} no existe en la memoria")

#ADD |M(X)|

def add_abs_m(adress):
    global acumulador
    if adress in lista_memoria:
        valor = abs(lista_memoria[adress])  # Valor absoluto de M(X)
        acumulador += valor
        print(f"ADD |M(X)| ha sido ejecutado. Dirección: {hex(adress)}, valor absoluto {valor}")
        print(f"Acumulador después de la suma: {acumulador}")
    else:
        print(f"ERROR. ADD |M(X)| no ha sido ejecutado. La dirección: {hex(adress)} no existe en la memoria")

#SUB M(X)

def sub_m(adress):
    global acumulador
    if adress in lista_memoria:
        valor = lista_memoria[adress]
        acumulador -= valor
        print(f"SUB M(X) ha sido ejecutado. Dirección: {hex(adress)}, valor {valor}")
        print(f"Acumulador después de la resta: {acumulador}")
    else:
        print(f"ERROR. SUB M(X) no ha sido ejecutado. La dirección: {hex(adress)} no existe en la memoria")

#Funcion DIV_M(X) (Estefani)
#nombre de la funcion 
def DIV_M (acumulador, X):
    mq = acumulador / X   #se hace la division
    acumulador = acumulador % X # se calcula el resto de la division
    return mq, acumulador 

def STOR (D) :
    global acumulador
    if D in lista_memoria:
        acumulador=lista_memoria[D]
        print(f"Nuevo valor del acomulador:",acumulador)
    else:
        print("Error, la direccion no existe en la memoria ")
def STOR (I) :
    global acumulador
    if I in lista_memoria:
        acumulador=lista_memoria[I]
        print(f"Nuevo valor del acomulador:",acumulador)
    else:
        print("Error, la direccion no existe en la memoria ")

    #REVISAR FUNCIONES, PUEDEN ESTAR INCOMPLETAS
def LSH (acumulador):
    
    res = acumulador *2# se multiplica el acomulador por 2
    return res

def RSH (acumulador):
    
    res = acumulador / 2# se divide el acomulador por 2
    return res



#Codigos de yes
# Instrucción 1: LOAD MQ
def load_mq():
    """
    Transfiere el contenido del registro MQ al acumulador.
    """
    global acumulador, mq
    acumulador = mq
    print(f"LOAD MQ ejecutado. MQ: {mq}, acumulador: {acumulador}")

# Instrucción 2: LOAD MQ, M(X)
def load_mq_mem(address):
    """
    Transfiere el contenido de la posición de memoria X a MQ.
    """
    global mq
    if address in lista_memoria:
        mq = lista_memoria[address]
        print(f"LOAD MQ, M({hex(address)}) ejecutado. MQ: {mq}")
    else:
        print(f"ERROR: Dirección {hex(address)} no encontrada en memoria.")

# Instrucción 3: STOR M(X)
def stor_mem(address):
    """
    Transfiere el contenido del acumulador a la posición de memoria X.
    """
    global acumulador, lista_memoria
    lista_memoria[address] = acumulador
    print(f"STOR M({hex(address)}) ejecutado. Memoria[{hex(address)}]: {lista_memoria[address]}")

# Instrucción 4: LOAD M(X)
def load_mem(address):
    """
    Transfiere el contenido de M(X) al acumulador.
    """
    global acumulador, lista_memoria
    if address in lista_memoria:
        acumulador = lista_memoria[address]
        print(f"LOAD M({hex(address)}) ejecutado. Acumulador: {acumulador}")
    else:
        print(f"ERROR: Dirección {hex(address)} no encontrada en memoria.")

# Instrucción 5: LOAD -M(X)
def load_neg_mem(address):
    """
    Transfiere el valor negativo de M(X) al acumulador.
    """
    global acumulador, lista_memoria
    if address in lista_memoria:
        acumulador = -lista_memoria[address]
        print(f"LOAD -M({hex(address)}) ejecutado. Acumulador: {acumulador}")
    else:
        print(f"ERROR: Dirección {hex(address)} no encontrada en memoria.")



def mul_m(address):
    global acumulador
    if address in lista_memoria:
        valor = lista_memoria[address]
        acumulador *= valor
        print(f"MUL M({hex(address)}) ha sido ejecutado. Valor: {valor}, Acumulador: {acumulador}")
    else:
        print(f"ERROR: Dirección {hex(address)} no encontrada en memoria.")
        
