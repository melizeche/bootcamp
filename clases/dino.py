class Dino:
    ojos = 2

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
        self.patas = self.patas - cantidad_de_patas_a_cortar
    
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
