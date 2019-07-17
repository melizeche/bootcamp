class Persona:  # Definimos la clase, una receta para crear un objeto
                # o tambien  la clase es la "plantilla"
    edad = 0    # Atributo de clase o propiedad del objeto que vamos a crear

    def __init__(self, un_nombre):  # __init__ es el metodo constructor
                                    # metodos --> funciones dentro de una clase
        self.mi_nombre = un_nombre  # usamos self para referirnos al objeto mismo
        print("Hola naci, me llamo", self.mi_nombre) 
    
    def cumple(self):             # cumple es metodo de la clase Persona
        self.edad = self.edad + 1 # que aumenta la propiedad edad en 1
    
    def asignar_edad(self, una_edad): #asignar_edad es un metodo que recibe un
                                    # argumento numero y asigna a la propiedad
        self.edad = una_edad        # edad del objeto

# Ej. Agregar un metodo a la clase Persona que asigne una nacionalidad y otro
# metodo saludar que imprima "Hola soy ___ y mi nacionalidad es ____"      
# Crear un objeto persona, asignarle una nacionalidad y hacerle saludar 
# 

nombre = Persona("Mauro") 

pepe = Persona("Pepito") # pepe es un objeto de la clase persona o tipo persona
pepa = Persona("Pepita")
print(pepe.edad)
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)

print(pepa.mi_nombre)

#hacer una clase que se llame vehiculo y que tenga tres atributos y uno de 
#sea cantidad_ruedas; y un metodo que sea definir_tipo_vehiculo que me 
#diga si es "bicicleta, triciclo, auto" de acuerdo a la cantidad de ruedas.
#pista:
# movil = Vehiculo("rojo",3)
# movil.definir_tipo_vehiculo()
# "movil tiene 3 ruedas y es un triciclo"

# class Movil:
#     ruedas = 0

#     def __init__(self,cantidad_ruedas):
#         self.mi_vehiculo = cantidad_ruedas
#         print("vehiculo es", self.mi_vehiculo)

# ruedas = Movil(7)

class Vehiculo:
    cantidad_ruedas = 0
    color = ""
    marca = ""

    def __init__(self,ruedas,un_color,una_marca):
        self.cantidad_ruedas = ruedas
        self.color=un_color
        self.marca=una_marca

    def definir_tipo_vehiculo(self):
        if self.cantidad_ruedas == 2:
            print("es una bici de color", self.color)
        elif self.cantidad_ruedas == 3:
            print("es un triciclo")
        elif self.cantidad_ruedas == 4:
            print("es un auto")

autito = Vehiculo(2,"rojo","toyota")
autito.definir_tipo_vehiculo()

    




