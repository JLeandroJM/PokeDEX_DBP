import pymongo
import requests

def obtener_datos(nombre):

# Establecer la conexión a MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")  # Reemplaza con tu conexión MongoDB

# Seleccionar la base de datos
    db = client["pokemon"]  # Reemplaza con el nombre de tu base de datos
    data = db.pokemon.find_one({"name":nombre})
    # Cerrar la conexión a MongoDB
    client.close()
    return data
# Obtener datos de la API de Pokémon (reemplaza la URL con la URL de tu API)
def obtener_nombres():
    import os

    # Ruta de la carpeta que contiene las imágenes
    ruta_carpeta = "../PokemonDataset"

    # Lista para almacenar los nombres de los archivos
    nombres_imagenes = []

    # Obtener los nombres de los archivos en la carpeta
    for nombre_archivo in os.listdir(ruta_carpeta):
        # Verificar si el archivo es una imagen (puedes agregar más extensiones si es necesario)
        if nombre_archivo.endswith((".jpg", ".jpeg", ".png", ".gif")):
            nombres_imagenes.append(os.path.splitext(nombre_archivo)[0].lower())

    return nombres_imagenes

# for i in obtener_nombres():
#     nombre = i
#     url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Error al obtener los datos de {nombre}")
#         continue
#     poke = response.json()
#     del poke["game_indices"]
#     del poke["sprites"]
#     del poke["past_types"]
#     del poke["forms"]
#     del poke["past_abilities"]
#     del poke["species"]
#     del poke["held_items"]

#     # Insertar los datos en la colección de MongoDB
#     coleccion = db["pokemon"]  # Nombre de la colección

#     coleccion.insert_one(poke)  # Insertar los datos en MongoDB


