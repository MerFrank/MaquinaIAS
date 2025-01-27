from instrucciones import *

address = ""
x = 0
instrucciones = {
    "LOAD MQ": load_mq,
    "LOAD MQ M": lambda: load_mq_mem(address),
    "STOR M": lambda: stor_mem(address),
    "LOAD M": lambda: load_mq_mem(address),  
    "LOAD -M": lambda: load_neg_mem(address),
    "LOAD |M|": lambda: load_abs(address),
    "LOAD -|M|": lambda: load_abs_neg(address),
    f"JUMP M({x},0:19)": lambda x=x: jump_left(address),
    f"JUMP M({x},20:39)": lambda: jump_left(address),
    f"JUMP + M({x},0:19)": lambda: jump_left(address),
    f"JUMP + M({x},20:39)": lambda: jump_left(address),
}