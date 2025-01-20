 # Variables globales
memoria = {}
acumulador = 0
MQ = 0  # Registro MQ

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

# Código de prueba
if __name__ == "__main__":
    # Inicializamos memoria con algunos valores
    memoria[0x01] = 42
    memoria[0x02] = -15
    memoria[0x03] = 100

    # Asignamos un valor inicial a MQ
    MQ = 123

    # Probamos las instrucciones
    print("\nPrueba de LOAD MQ:")
    load_mq()

    print("\nPrueba de LOAD MQ, M(X):")
    load_mq_mem(0x01)

    print("\nPrueba de STOR M(X):")
    stor_mem(0x04)  # Guardar el acumulador en una nueva posición de memoria

    print("\nPrueba de LOAD M(X):")
    load_mem(0x01)

    print("\nPrueba de LOAD -M(X):")
    load_neg_mem(0x02)

    print("\nEstado final:")
    print(f"Acumulador: {acumulador}")
    print(f"MQ: {MQ}")
    print(f"Memoria: {memoria}")
