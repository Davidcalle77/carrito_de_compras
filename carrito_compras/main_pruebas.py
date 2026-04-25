# Solo el script CSV
import csv
from carrito import CarritoCompras  # Importa la clase

# Escritura CSV
frutas = [
    ["Manzana", "Roja", "Dulce"],
    ["Platano", "Amarillo", "Dulce"],
    ["Lima", "Verde", "Acida"],
]
with open("frutas.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(frutas)
print(" Archivo frutas.csv creado exitosamente.")

# Lectura CSV
datos_frutas = []
# open(..., "r")Abre el archivo en modo lectura
# csv.reader(archivo)Lee el CSV fila por fila
# datos_frutas.append(fila)Guarda cada fila como una lista
# print(datos_frutas)Imprime la lista de listas completa
with open("frutas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        datos_frutas.append(fila)
print(datos_frutas)


# Ejecutar pruebas
# python main_pruebas.py
# frutas.csv se genera al ejecutar python main_pruebas.py
