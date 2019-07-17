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