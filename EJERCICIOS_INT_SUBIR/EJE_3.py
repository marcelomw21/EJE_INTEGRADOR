# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece

def contar_palabras(texto):
    palabras = texto.split()  # Dividir el texto en palabras
    contador = {}  # Diccionario para almacenar las palabras y su frecuencia

    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para hacer coincidencias
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador

cadena = input("Ingrese una cadena de texto: ")
resultado = contar_palabras(cadena)

print("Palabras y sus frecuencias:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")
