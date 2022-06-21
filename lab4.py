#==================================
# PROGRAMACION ORIENTADA A OBJETOS
#==================================

#================================
# Una clase para un objeto vacio
# no esta tan vacio, necesita
# la palabra pass = pasar
#============================

class ObjetoVacio:
    pass

#nada tambien es un Objeto Vacio
nada= ObjetoVacio()
print(type(nada))

#================
# La clase llanta
#================

class llanta:

#=====================================
# Varialble cuenta es de toda la clase
#=====================================

    cuenta = 0
    #===================================   
    # Funcion constructora de identidad
    # __int__ es una funcion reservada 
    #comienza con uno mismo: self
    #pero puede ser otro nombre (mi)
    # parametros de entrada = default
    #===================================

    def __init__(mi,radio=50,ancho=30,presion=1.5):     #la funciono __init__ lleva doble guion bajo, de no ser asi no es reconocido como constructor del objeto, si no como otra funcion, el "mi" que esta al inicio del prentesis no es nnecesariamente mi, puede ser self o algo mas x.

        #variable de la estructura completa llanta
        llanta.cuenta += 1
        #variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion
#=======================     
# objetos (instanciados)
#======================
llanta1 = llanta(50,30,1.5)
llanta2 = llanta(presion=1.2)
llanta3 = llanta() 
llanta4 = llanta(40,30,1.6)

#===================================
# O bjeto que ocntiene otros objetos
#===================================


class coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = coche(llanta1, llanta2, llanta3, llanta4)
print("total de llantas: ", llanta.cuenta) #variable global de la clase
print("presion de la llanta 4 = ",llanta4.presion) #presion de la llanta 4
print("radio de la llanta 4 = ", llanta4.radio)
print("radio de la llanta 3 = ", llanta3.radio)
print("presion de la llanta 1 de mi coche = ", micoche.llanta1.presion)

#===============================
# E N C A P S U L A M I E N T O 
#===============================

#====================================================================
# Uso de la funcion de python property para poner y obtener atributos
#====================================================================
class estudiante:
    def __init__(self):
        self.__nombre = ''
    def ponerme_nombre(self, nombre):
        print('se llamo a ponerme_nombre')
        self.__nombre = nombre
    def obtener_nombre (self):
        print('se llamo a obtener_nombre')
        return self.__nombre
    nombre= property(obtener_nombre,ponerme_nombre)
#===================================
# Crear objeto estudiante sin nombre
#===================================
estudiante = estudiante()
#======================================================================
# Ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre
# (sin tener que llamar explicitamente la funcion)
#======================================================================
estudiante.nombre = "Diego"

# obtener el nombre con el metodo obtener_nombre__nombre__nombre
# es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explicitamente a la funcion obtener_nombre)

print(estudiante.nombre)

#esto no funciona realmente
#print(estudiante.__nombre)

#=====================
#  Herencia de clases
#=====================
class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1 = a
        mi.lado2 = b
        mi.lado3 = c
        mi.lado4 = d

    def perimetro (mi):
        p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4 
        print("perimetro=",p)
        return p
#========================================
# Su hijo rectangulo
# rectangulo es hijo de  cuadrilatero
# rectangulo (cuasrilatero)
#=======================================

class rectangulo(Cuadrilatero):
     def __init__(mi, a, b):
        #======================================         
        # constructor de su madre
        #======================================
        super().__init__(a, b, a, b)
#====================
# El nieto Cuadrado
# Hijo del rectangulo
#=====================

class cuadrado(rectangulo):
    def __init__(mi, a):
        super().__init__(a, a)

    def area(mi):
        area= mi.lado1**2
        return area

#  def perimetro(self):
   #     p = 4*self.lado1
    #    print("perimetro =",p)
     #   return p

#===================
# Crear un cuadrado
#===================

cuadrado1 = cuadrado(5)

#=====================================================
# LLamar al metodo perimetro de su abuelo cuadrilatero
#=====================================================

perimetro1 = cuadrado1.perimetro()

#===============================
# Llamar a su propio metodo area
#================================

area1 = cuadrado1.area()

print("perimetro =", perimetro1)
print("area =", area1)

#================================================================
# Sobre-escribir un metodo de su madre o abuela o tatarabuela...
# es volver a definir una funcion ya existente
#================================================================

