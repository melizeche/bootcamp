# Tipo de dato String/cadena/str de texto
"Esto es un string" 
#Tipo de dato Integer/Entero/int
105
#Listas
[] #Lista Vacia
["Marce", 33, "Programador"] #Lista de 3 elementos
# Variables
nombre = "Marce"
edad = 30+3
edad_mal = "30+3"
variable_lista = ["Hola", nombre, 99]
# Acceder a un elemento de la lista
print(variable_lista[0], edad, variable_lista[2])
#Acciones/operaciones sobre listas
variable_lista.append("rugby") #agregar elemento a lista
variable_lista.pop() #eliminar ultimo elemento
variable_lista[2] = 50
print(variable_lista)
variable_lista[2] = "Chau"
print("variable_lista es",variable_lista)

# Bucles / Loop / Ciclos
print(len(variable_lista))
#Imprimir cada elemento de una lista
for loquesea in variable_lista:
    print(loquesea)

# Imprimir los numeros del 1 al 10 usando for y range
for cualquiercosa in range(1,11):
    print(cualquiercosa)
print("-----------------------")
otra_lista = [5 , "Hola que tal", "Chau", 4]

print(otra_lista)
print(otra_lista[len(otra_lista)-1])

dimension_de_lista = len(otra_lista) - 1
print(otra_lista[dimension_de_lista])

print("-------------------------------")
# Imprimir el ultimo elemento de una lista sin saber cuantos
# Elementos tiene, solucion general
otra_lista = [5 , "Hola que tal", "Chau", 4]
otra_lista.append("AAAA")

# Solucion paso por paso
dim_lista = len(otra_lista)
print("La dimension de otra_lista es", dim_lista)
indice_del_ultimo = dim_lista - 1
print("El indice del ultimo elemento es", indice_del_ultimo)
print(otra_lista[indice_del_ultimo])

# Solucion de una linea
print(otra_lista[len(otra_lista)-1])

#esto es equivalente
for numero in range(1,11):
    print(numero)
# a esto
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print(numero)
# imprimir hola 10 veces
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("hola", numero) #imprimir numero es opcional

#imprimir el numero de resultado de la sma de los numeros 
#del 1 al 10   -> 55
#acumuladores 
challenge=[1,2,3,4,5,6,7,8,9,10]  #se crea una lista
a=0                         #se crea una variable de base 
for x in challenge:        #se crea un ciclo que va a correr la cantidad de elementos que tiene la lista challenge
    a=a+x                  #se va acumulando las sumas parciales  
print(a)

sumatoria=0         #variable inicializada en cero 
for valor in range(1,11):  
    sumatoria= sumatoria + valor   
print(sumatoria)


    
 








