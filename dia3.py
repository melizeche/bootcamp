############### CONDICIONALES #############
# == igual
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que
# != distinto o no igual
a = 3
#pregunta 1
if a > 3:
    print("Si, a es mayor a 3")
    print("Chau!")
else:
    print("No, a no es mayor a 3")
#pregunta 2
if a == 3:
    print("a es igual a 3")

nota = 60
#pregunta 3
if nota >= 60:
    print("Pasasteeeee!!!!")
else:
    print("Hule ya ")

# Ej. Crear una funcion que reciba como parametro una 
# nota del 1 al 100 e imprima si pasaste o te aplazaste (se aprueba con 61)

def puntaje(nota, nombre):
    if nota>=61:
        print("Pasaste!", nombre)
    else:
        print("No pasaste", nombre)

puntaje(60, "Pepito")

a = 6
if a > 5 and a < 10 :
    print("a es mayor a 5 y menor que 10")
else:
    print("a no esta en el rango, alguna de las 2 condiciones no se cumplieron")

if a > 5 or a < 10:
    print("a es mayor que 5 o menor que 10")
else:
    print("a no es mayor que 5 ni menor que 10")

edad = 7
if edad > 18:
    print("Deberia estar en la universidad")
elif edad > 13:
    print("Deberia estar en secundaria")
elif edad > 6:
    print("Deberia estar en primaria")
else:
    print("Deberia estar en su casa bbdlc")

#Anidado
if edad > 18:
    print("Universidad")
else:
    if edad>13:
        print("Secundaria")
    else:
        if edad > 6:
            print("Primaria")
        else:
            print("bbdlc")

#Ej. Crear una funcion puntaje que reciba como parametro una nota
# del 1 al 100 e imprima que nota sacaste
# nota < 60 ---->1 # nota entre 60 y 70 --->2
# nota entre 71 y 75 ---> 3# nota entr 76 y 85 ---> 4
# nota mayor que 85  --- > 5

def nivel(puntaje):
    if puntaje < 60 and puntaje> 1:
        print("Sacaste 1")
    elif puntaje >= 60 and puntaje < 70:
        print("Sacaste 2")
    elif puntaje >71 and puntaje < 75:
        print("Sacaste 3")
    elif puntaje <76 and puntaje >85:
        print("Sacaste 4")
    elif puntaje > 85:
        print("Sacaste 5")
    else:
        print("Ausente")

nivel(0)
nivel(70)

def cal_final(nota):
        if nota < 60:
            return 1
        elif nota <70:
            return 2
        elif nota<75:
            return 3
        elif nota < 85:
            return 4
        elif nota>=85:
            return 5

print(cal_final(66))

def paso_examen(calificacion):
    if calificacion >= 2:
        return True
    else:
        return False

print(paso_examen(3))

nota = cal_final(78)

if paso_examen(nota) == True:
    print("Felicidades pasaste!!!")
else:
    print("Te aplazaste :( ")


# nombre = input("Ingresa tu nombre: ")
# print("Hola", nombre)

edad = 33
saludo = "Tenes " + str(edad)
print(saludo)

num1 = int(input("Ingresa el primer numero a sumar: "))
num2 = int(input("Ingresa el segundo numero a sumar: "))
print("El resultado es: ", num1 + num2)

nombre = input("Ingresa tu nombre: ")
# Ej. Pedir al usuario  que ingrese tres numeros y multiplicarlos
# entre si, imprimir el resultado
# Pista
num1 = input("Ingresa el primer numero: ")

# Ej2. Pedir al usuario un numero del 1 al 100 y llamar a la 
# funcion que retornaba la nota que creamos hace un rato
# utilizando el valor ingresado por el usuario


###### Bucle while == Mientras  #####

x=0
while x != 5:
    print("Hola esto es un bucle while")
    x = int(input("Ingresa un numero: "))