print(2+4+4+6)
print(3*4)
print(12-4)
print(12/4)
print("Hola Mundo!")
print(2)
print("2")
print(2+2) #hola Suma de enteros 
print("Hola Mundo" + "2")
#Lo siguiente es una suma/concatenacion de strings
print("2+2")
print("Hola " * 10) #Imprimir un texto 10 veces
#########################
a = 2 # Asignamos el valor 2 a la variable a
b = 10 #Asignamos 10 a la variable b
print(a+b)#imprimimos la suma de los valores de a y b
print("Hola el valor de las variables a y b es",a, b)
# Para imprimir distintos valores separamos 
# los valores con coma
print("Hola", 2, "Chau", 10)

# Ej1. Crear una variable nombre y una variable edad
# con sus nombres y edades y despues imprimir:
# Hola, me llamo ____  y tengo ___ años
nombre = "Marce"
edad = 33
print("Hola, me llamo", nombre, "y tengo", edad, "años")

# Ej1.1 Crear una variable hobby con tu pasatiempo 
# e imprimir
#Hola, me llamo __  y tengo __ años y mi hobby es___
hobby = "jugar rugby"
print("Hola, me llamo", nombre, "y tengo", edad, "años y mi hobby es", hobby)
edad = "33 años"
print("Hola, me llamo", nombre, "y tengo", edad, "y mi hobby es", hobby)

lista_vacia = []   # con los corchetes se crea una lista vacia
listax = [1,2,6,8] # lista con 4 elementos de tipo integer
print(lista_vacia) # se imprime la lista vacia
print(listax)      # Se imprime la lista listax
datos = ["Marce"]  # Se crea una lista datos con un elemento string
print(datos)    # Imprimos la lista anterior
alumnos = ["Jose", "Ramoncito", nombre, "Maria"] #Lista de 
print(alumnos)
#nro_alumno = 3
print(alumnos[2], alumnos[0])

#Ej. Crear una lista datos que en el primer lugar esté tu nombre
# y en la segunda posicion esté tu edad.
# Imprimir  "Hola me llamo ___, y tengo ___ años"
datos = ["Marce", 33]
print("Hola me llamo", datos[0], "y tengo", datos[1], "años")
datos[1] = 99
print("Hola me llamo", datos[0], "y tengo", datos[1], "años")
print(datos)    # Imprimimos la lista datos q tiene 2 elementos
#Agregamos con .append() el string "programador" a la lista
datos.append("Programador")
print(datos)
print(datos[2])

# Ej. Agregar una profesion y un hobby a la lista datos 
# previamente creada (usar append())
# imprimir la lista

datos.append("Contadora")
datos.append("Viajar")
print(datos)


# funcion len() => lenght => dimension/longitud en ingles
print(datos)
#guardamos la dimension de datos en la variable dimension_de_datos
dimension_de_datos = len(datos) 
#Imprimimos dimension_de_datos
print(dimension_de_datos)
datos.pop() # Eliminamos el ultimo elemento de la lista datos
print(datos)
print(len(datos)) #Imprimimos la dimension de la lista datos
saludo = "Hola, que tal" #creamos una variable de tipo string
print(saludo) # imprimimos
print(len(saludo)) # imprimimos la dimension de la variable saludo

#ej. obtener la dimension de la lista datos e imprimir:
# "La lista datos tiene ___ elementos"

print("La lista datos tiene", len(datos), "elementos")

dimension_de_datos = len(datos)
print("La lista de datos tiene", dimension_de_datos, "elementos")

lista_larga = [3,4,5,6,7,8,3,2,4,6,4,4,7,8,8,6,55]
# ej. Imprimir el ultimo elemento de una lista sin saber
# cuantos elementos tiene, pista usar len()
# NO hacer lista_larga[27]

print(lista_larga[len(lista_larga)-1])

ultimo = len(lista_larga)-1
print("el ultimo elemento es", lista_larga[ultimo])


datos = ["Marce", 33, "Programador"]
datos.append("rugby")
print(datos[2])
print(len(datos))
indice_ultimo = len(datos) - 1
print(indice_ultimo)
print(datos[indice_ultimo])


######### Bucles/Loops/Ciclos/Iteraciones  #######

lista_temas = ["variables", "listas", "tipos de datos"]

for concepto in lista_temas:
    print("Hoy aprendí", concepto)
    print("Que gusto!")
print("Esto es lo que aprendí hoy")

for variable_for in lista_temas:
    #bloque de codigo
    print("esto se repite")
print("esto no se repite")
# recorrer una lista con for e imprimir en cada ciclo
# el valor del elemento con 3 signos de admiracion y al final
# fuera del bucle "FIN!!!"
# ej: variables !!! 

for concepto in lista_larga:
    print("compañeros!", concepto)
    print("buena onda")
print("FIN")

lista_corta = ["linda", "fea", "buena"]

for significa in lista_corta:
    print(significa, "!!")
print("FIN")
# range(1,11) #del 1 al 10
for elegi_nomas in range(10): # del 0 al 9
    print("HOLA", elegi_nomas)

# Ej1 Imprimir los numeros del 1 al 100 usando for 
# y range

#DESAFIO
# Imprimir el resultado de la suma de los numeros
# del 1 al 10 usando range -> 1+2+3+4+5+6+7+8+9+10=55