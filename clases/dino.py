class Animal:
    vivo = True

    def __init__(self):
        self.vivo = True
    
    def esta_vivo(self):
        if self.vivo==True:
            print("Estoy vivo")
        else:
            print("estoy morido")
    
    def morir(self):
        self.vivo = False
        print("Me murí")

class Dino(Animal):
    ojos = 2
    genero = None 

    def __init__(self, un_nombre, un_color, canti_patas=4, un_genero=None):
        self.nombre = un_nombre
        self.color = un_color
        self.patas = canti_patas
        self.genero = un_genero
        print("Naci")
    
    def saludar(self):
        print("Hola me llamo", self.nombre, "tengo", self.patas, "patas y soy", 
        self.color )
    
    def cortar_pata(self, cantidad_de_patas_a_cortar=1):
        if self.patas >0:
            self.patas = self.patas - cantidad_de_patas_a_cortar
        else:
            print("No tengo mas patas para cortar, chau :(")
        if self.patas <=0:
            self.morir()
    
    def decir_genero(self):
        print("Hola soy", self.nombre, "y me identifico como", self.genero)


pepe = Dino("Pepito", "Verde", 4, "Macho alfa pecho peludo")
print(pepe.nombre)
pepe.saludar()
pepa = Dino("Pepita", "Lila", 13, "Hembra")
pepa.saludar()

pepa.cortar_pata()
pepa.saludar()
pepa.cortar_pata(10)
pepa.saludar()

pepa.decir_genero()
pepe.decir_genero()

class TRex(Dino): # La clase TRex hereda los metodos y atributos definidos
                  # en la clase Dino
    def __init__(self, nombre, patas=4, color=None):
        self.nombre = nombre
        self.patas = patas
        self.color = color
        print("Hola soy un TRex y me llamo", self.nombre)

robert = TRex("Roberto el TREX")
print(robert.ojos)

robert.saludar()
robert.decir_genero()

robert.esta_vivo()

robert.saludar()
robert.cortar_pata()
robert.saludar()
robert.cortar_pata()
robert.cortar_pata()
robert.cortar_pata()
robert.cortar_pata()

robert.saludar()

robert.esta_vivo()

