"""ESTE ES UN SUPER COMENTARIO DEL INSTRUCTIVO"""
 #===============
 #OPERACIONES BASICAS
 #===============
print(2+3)
print(2-3)
print(2/3)
print(2**10) #doble asteriscoes para elevar o potencia
print(2**.5) #tambien se puede hacer raices u potencias fraccionadas
print(10%2) 
print(10%.1) #solo en python se puede hacer modulares fraccionarios

#===========
#PARA SABER EL TIPO DE OBJETO SE USA T Y P E
#==========

r=0
print (type(r)) #debe salir entero
a=3.5
print (type(a)) #real, flotante
t='true'
print (type(t)) #booleano

#==========
#MENSAJES A PANTALLA
#==========
print("este es un comando de python. ", "Este es otro neunciado.", t)
print('id: ',1)
print('First name;', 'steve')
print('second name;', 'de minecraft')
print("vamos a sumar esto" + " con esto")
#======================
#CONTINUAR UNA INSTRUCCION EN VARIOS RENGLONES
#=====================
if 100>99 and\
    200<=300 and\
    True != False:
        print('hello world')
#====================
#COMANDOS DIFERENTES EN LA MISMA LINEA
#===================
print("hola "); print("tu!!") #se considera esto mala practica

#==================
#USANDO PARÉNTESIS REDONDOS, CUADRADOS O LLAVES
#SE PUEDE ESCRIBIR EN VARIOS RENGLONES
#==================
list=[1, 2, 3 ,4,
      5, 6, 7, 8,
      9, 10, 11, 12]
matriz= [ [1,2,3,4,5,6,7,8,9,10,11,12] ]
print(list)
print(matriz)

#======================
# INDENTACIÓN ESTRICTA PARA PROCESOS EPENDIENTES DE : (DOS PUNTOS)
#=====================
if 10>5:
    print ("diez es mayor que cinco")
    print("otra indentacion")
    for i in list:
        print(i)
        print("ok")
if 10>5:
    print("verdadero")
    if 10<20:
        print("verdadero")
elif 5>3: #comienza segundo condicional
    print ("esto no se imprimira")
else:
    print ("aqui nunca llega")

#===================
#FUNCIONES
#================
def say_hello(name):
    print("hello ", name)
    print("welcome to python tutorials")
    say_hello("julian")

#==============
#inpud permite obtener datos del usuario en promter
#===============
nombre= input ("dame tu nombre")
print("hola como estas", nombre)

#===============
#los enteros son de presicion ilimitada
#==============
y= 20000000000000000000000000
print(y)

#================
#se pueden delimitar numeros con guion bajo pero no con coma
#================
y=5_000_000
print(y)

#===============
# La notacion cientifica de flotantes utiliza e o E
#==============
#1.2 x 10^{-9}
#=============
y = 1.2E-9
print(y)

#==================
#La funcion float() convierte strings y enteros a floats
#===================
y= float("34.3")
print (y)

#================
# Los complejos se escriben con la raz de menos uno
# j siempre como un numero como prefijo 
# no acepta la j suelta 
#=================
z= 1+1j
#suma +
#resta -
#multiplicacion *
#division /
#modulo %
#exponente **
# // cuncion piso (redondeo hacia abajo)
#Funciones para transformar números int() float() complex()
# Operaciones 
 	#abs() devuelve el valor absoluto de la entrada pasada
	#round() el redondeo mas proximo 
	#pow() diseñada para exponenciar valores dados a la base y el exponente
print(round(3.1459, 4))
#=====================
#String de varias lineas
#=====================
parrafo =""" En el bosque de la bebecita bebe lean
            el lean se perdio"""
            #despues de declarar algo hay que darle siempre un espacio
print(parrafo)

#=================000
#La funcion len() obtiene el tamaño del string
#=====================
n= len(parrafo)
print (n)

#============================
#las letras en un string ocupan lugares como en un arreglo
#(tambien de atras para delante comenzando en -1 el ultimo)
#===========================
palabra = "hola"
print (palabra [0])
print(palabra[-4])




        
