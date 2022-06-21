#==========================================================
# C O N D I C I O N A L E S     Y      F U N C I O N E S
#==========================================================
precio = 30 
#················
# si esto...
#················
if precio < 50:
    print("El precio es menor que 50")
#··························
# si no... si esto otro...
#·······················
elif precio > 50:
    print("El precio es mayor que 50")
#···························
# Si nada de lo anterior...
#·························
else:
    print("El precio es 50")

precio = 50 
cantidad = 5
total = precio*cantidad
print(total)
#========================
# Condicionales aninados
#=======================
if total>100:
    if total>500:
        print("total es mayor que 500")
    else:
        if total <500 and total > 400:
            print("total es menor que 500 pero mayor que 400")
        elif total < 500 and total > 300:
            print("total entre 300 y 500")
        else:
           print("total entre 100 y 300")
#··································
# La condicional de igualdad es ==
#··································
elif total==100:
    print("total es 100")
else: 
    print("total menor que 100")

#==============================================
# Contador mientras la condicion sea verdadera
#==============================================

#num = 0 
#while num < 5:
#   num = num + 1
#   print('num=', num)

#   num = 0
#   while num < 5:
#       num += 1                #num += 1 es lo mismo que num = num + 1
#       print('num =', num)
#       if num == 3:            # condicion antes de salir del bucle
#           break

#num = 0 
#while num < 5:
 #   num += 1
  #  if num >3:
   #     continue        #evitar lo que siguem continuar con las iteraciones
   # print('num=', num)

#==================
# Bucle sobre lista
#==================

nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)

#=======================
# Bucle sobre un string
#=======================

for char in 'Hello':
    print (char)

#===========================
# Bucle sobre un diccionario
#   items = elementos
#============================
numNames = {1:'One', 2:'Two', 3:'Three'}
for pair in numNames.items():
    print(pair)

#============================
# Bucle sobre diccionario 
# key= llave
# value = valor
#===========================
for k,v in numNames.items():
    print("key=", k, ", value=", v)


#==========================
#    F U N C I O N E S
#       primera funcion 
#==========================

def saludo():
    # Documentacion de la funcion
  """Esata funcion saluda"""
  print("que pedo rey ¿que haciendas?")
#=======================
# Llamado de la funcion
#=======================
saludo()

salida = saludo()
#con esa sentencia se ejecuta pero no se asigna

print(salida) #hacer eso no sirve xd

#help(saludo)  --> hacer eso muestra la documentacion 

#========================
# Funcion con argumento 
#========================

def salu2(nombre):
    """Esta funcion te saluda de nombre"""
    print("buenas, buenas", nombre,"!")
salu2("Judith")
salu2("Batman")
#==========================================
# Ahorrar trabajo del interprete
# nombre: str la variable nombre es un str
#==========================================
def saludos(nombre:str):
    """esta funcion te llama de nobre, de forma estricta"""
    print( "buens, buenas", nombre)
saludos("Judy")
a=123
print(type(a))
saludos(a)

#==============================               
# Funcion con muchos argumentos              
#==============================                
def saludos_multiples(nombre1,nombre2,nombre3):
    """esta funcion saluda a 3 personas al mismo tiempo"""
    print("Hola", nombre1, "," ,nombre2, "y", nombre3)
saludos_multiples("axel","dana","abi")

#====================================================
# Funcion que saluda a cualquier numero de argumentos
#=====================================================

def muchos_saludos(*nombres):
    """Esata funcion permite cualquier cantidad de argumentos"""
    i=0
    #end= es para poner de corrido todo
    print("hola", end="")
    while len(nombres)>i:
    #Ultimo nombre
    if (i==len(nombres) - 1):
    print(nombres[i])
    else:
    #cualquier otro nombre
    print(nombres[i], end=", ")
    i+=1
    muchos_saludos("Judy", "Angel", "David", "mili", "Edwin", "Levi", "Luis", "abdiel", "Zabdiel", "Esau")
    def greet(firstname, lastname):
        print ('Hello', firstname, lastname)

#=============================================
# Llamar la funcion con argumentos en desorden
#==============================================
greet(lasname = 'jobs', firstname='steve') #se pueden especifiar las varariables en desorden

#==================================      
# Funcion con argumentos escondidos
#===================================
def greet (**person):
    #==================================================
    # Persona tiene caracteristicas firstame y lastname
    #===================================================
    print('hello', person['fistname'], person['lastanme'])

greet(firstname= 'steve', lastname= 'jobs')
greet(lastname= 'jobs', firstname= 'steve')
greet(firstname='bill', lastname='gates')

#===================================
# Funcion con variables por defecto
#===================================
def greet(name= 'guest'):
    print('hello', name)
greet() #Utiliza el valor dado de antemano
greet('steve')

#=======================
# Funcion con resultado
#========================
def suma(a,b):
    return a + b

#==================================
# Programacion funcional
# Se pueden funciones en funciones
#==================================
total=suma(5, suma(10, 20))
print(total)

#=================================================
# Calculo lambda
# nombre de la funcion = lambda variable : Funcion
#==================================================
x_al_cuadrado = lambda x : x*x
al = x_al_cuadrado(5)
print(al)

#===========================
# lambda de varias variables
#============================
suma = lambda x1,x2,x3: x1+x2+x3
print(suma(99,98,97))

sumas= lambda *x: x[0]+x[1]+x[2]+x[3]

print(sumas(100,200,300,400))

#========================================
# Uso de funcion anonima
# el argumento va afuera entre parentesis
#=========================================
print((lambda x: x*x)(6)) # Funcion anonima

#====================================
# Funcion con variable global
# EVITE EL EXESO !!!!
#====================================

name= 'steve'
def greet():
    global name #parra utilizar una variable global (que viene de fuera del bloque)
    name= 'bill'
    print('Hello', name)
greet()
