from instrucciones import *

# Diccionario de instrucciones (clave: parte fija, valor: función)
dic_intrucciones = {
    # Instrucciones de LOAD
    "LOAD MQ": load_mq,
    "LOAD MQ, M": load_mq_mem,
    "LOAD M": load_mem,
    "LOAD - M": load_neg_mem,
    "LOAD |M|": lambda x: load_abs(x),
    "LOAD - |M|": lambda x: load_abs_neg(x),

    # Instrucciones de JUMP
    "JUMP M": jump_left,
    "JUMP + M": jump_right_con,

    # Instrucciones de ADD
    "ADD M": add_m,
    "ADD IM": lambda x: add_m(x, inmediato=True),

    # Instrucciones de SUB
    "SUB M": sub_m,
    "SUB IM": lambda x: sub_m(x, inmediato=True),

    # Instrucciones de MUL y DIV
    "MUL M": mul_m,  # Ahora usando la función mul_m
    "DIV M": lambda x: DIV_M(acumulador, lista_memoria[x]),

    # Instrucciones de desplazamiento
    "LSH": LSH,
    "RSH": RSH,

    # Instrucciones de STOR
    "STOR M": STOR,
}