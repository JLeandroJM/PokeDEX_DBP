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

print(nombres_imagenes)