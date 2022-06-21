#=============
# Clase curva
#=============

class Curva
""" Curva construye la curva que pasa por los puntos x
        parametros 
            x coordenadas ordenadas [(x1, x2, x3, ...)]
            y propiedades [f1(x),f2(x),...]
            dim dimenciones
            """
#======================
# Atrivutos de clase
#====================
x: float =[]
dim: int = 3

#==================
# Construcotr
#==================
def __init__(s,x:float=[],dim:int=3):
    s.x = X
    s.dim = dim
    s.n:int =int(len(s.x)/s.dim) #numero de puntos
    s.l = []                    #longitud sobre la curva
    s.lista_de_puntos()
    s.longitud()
#===========================
# lista de puntos
#==================
def lista_de_puntos(s) -> str:
    print(f"numerode puntos= {str(s.n)Ç")
    # Formato de datos
    s.formato = ""
    for j in range (s.dim):
        s.formato += "%15.8e"
    s.formato +="\n" # vuelta de carro:

