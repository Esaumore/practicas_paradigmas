#==========================================
#   C O N J U N T O S    Y    L I S T A S 
#==========================================
even_nums = {2,4,6,8,10} #conjunto de numeros pares
print(even_nums)
emp = {1, 'seven', 10.3, True} #es un conjunto con diferentes objetos, el booleano no entra dentro de los conjuntos.
print(emp)
nums ={1,2,3,4,5,5,6,6,2,3,4,9,9}
print(nums)
#================================
# Convertir secuencia a conjunto
#================================
s= set('hello') #la setencia set en python se usa para declarar conjuntos
print(s) # el conjunto no se genera en orden
s= set((1,2,3,4,5,6,7))
print (s)
#==============================================
# de diccionario a conjunto:conjunto de llaves
#==============================================
d= {1: 'one', 2: 'two'}
s= set(d)
print (s)

s.add(100) #el .add sirve para añadir onjetos a tu conjunto
print(s)
s.update(nums) #el .update genera una suma de conjuntos, no los ordena
print(s) 
s.remove (100) #.remove sirve para remover objetos de un conjunto
print(s) 
s1={1,2,3,4,5,5}
s2={4,5,7,6,9,10}

su= s1|s2 #UNION
print(su)

si= s1&s2 #INTERSECCIÒN
print(si)
ss= s1^s2 #DIFERENCIA SIMETRICA, es el conjunto de elementos que solo pertenecen a uno u otro de los conjuntos pero no a ambos.
print(ss)

#====================
# Uso de diccionarios
#====================

capitals= {"USA": "Washington D.C.", "France": "Paris", "India": "New Delhi"}
print(capitals)

#=================
# llave:valor
#=================
# diccionario vacio
d={}
#ññave entera, valor string
numNames= {1: "One", 2: "Two", 3: "Three"}
#llave real,valor string
deciNames= {1.5:"One and Half", 2.5: "Two and half", 3.5:"Three and half"}
# llave tupla, valor string
items= {("parker", "Reynolds", "Richards"): "pen", ("LG","Wirlpool", "Samsung"): "Refrigerator"}
# llave string, valor int
romanNums= {'I': 1, 'II':2, 'III':3, 'VI':4, 'V':5}

print(romanNums)
print(romanNums["I"]) #se puede especificar un elemento del conjunto en particular para imprimir.

print(capitals.get("India"))
print(capitals.get("india")) #La forma de escritura si importa 

# Reportal llave y valor
for k in capitals:
     print("key =" + k + ",Value=" + capitals[k])
# Nuevo dato del diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["USA"]
print(capitals)
#borrar todo el diccionario
del capitals

#Reportar llaves
print(romanNums.keys())
# Reportar valores 
print(romanNums.values())

# Juicio de llave (esta o n oesta la llave en el diccionario)
print("I" in romanNums)
print("XX" in romanNums)
print("X" in romanNums)


#=======================================    
#               Listas
# estas pueden ser de objetos diferentes
#=======================================
primeralista = [] # Lista Vacia
print(primeralista)
#=================         
# llenar la lista
#=================
primeralista = [1,"javi",1.34, "bosco", "sirham","2", True]
print(primeralista)
#====================================
# List: hacer una lista
#range(i.j): secuencia de i hasta j-1
#=====================================

nums= list(range(1,61))
for i in nums:
    print(i)

#=======================================
#   incluir nuevos elementos en la lista
#=======================================

nums.append(61)
nums.append(62)
nums.append(61)
print(nums)
#=============================
# Borrar elementos de la lista
#==============================
nums.remove(61)
print(nums)

#=============================
# Quitar elemento con indice i 
#=============================
i=61
del nums [i]
print (nums)

#===============
#Borrar la lista
#===============
del nums

#==============
# Sumar listas
#==============

L1= [1,2,3]
L2= [4,5,6]
print (L1+L2)


#================
# Llenado a mano
#================
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
    print(potencial[100])

#================================
# Generaar una tupla con la lista
#================================
potencial= tuple(potencial)
print(potencial[100])

