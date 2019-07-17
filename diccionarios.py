#Diccionario de datos

# Un diccionario es una estructura de datos y un tipo de dato en Python
# que nos permite almacenar pares de clave:valor
# Los diccionarios nos permiten identicar los elementos por una 
# clave(key)

nombre_del_diccionario = { "nombre_de_la_clave":"valor de cualquier tipo"}
diccionario_vacio = {}

dic_persona = {"nombre":"Marce", "edad":33 }

#Para acceder a un valor ponemos el nombre del diccionario y entre[]
#la clave
print(dic_persona["nombre"])
# Para cambiar el valor ponemos el nombre del dic, entre[] la clave 
# y asignamos con =
dic_persona["edad"] = 99

nombre = "Steven"
lista_hobbies = ["rugby","comer mbeju","cortar patas de dinos"]
idiomas = {
    "espanhol":"bueno", 
    "ingles":"bueno", 
    "guarani":"jopara", 
    "portugues":"kaure"
    }
persona = {
    "nombre": nombre, 
    "edad":33, 
    "profesion":"programador",
    "nacionalidad":"paraguaya",
    "hobbies": lista_hobbies,
    "idiomas": idiomas
    }

lista_persona= ["Marce", 33, "programador", "rugby", "paraguaya"]

diccionario_vacio = {}
print("diccionario persona: ",persona)
print("lista persona:", lista_persona)
print(persona["nombre"])
print(persona["edad"])
print(persona["profesion"])
print("------------------")
print(persona["hobbies"][2])
print(persona["idiomas"])
print(persona["idiomas"]["portugues"])

lista_persona[2] = "Panadero"
print(lista_persona)

persona["profesion"] = "Panadero"
print(persona)