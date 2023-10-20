#Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.

def contar_palabras(texto):
    palabras = texto.split()  # Divide el texto en palabras
    contador = {} # diccioario para las palabras y frecuecias
    
    for palabra in palabras:
        palabra = palabra.lower()  # Covertir a mayuscula o minuscula
        if palabra in contador:    # x = ["apple", "banana"] 
                                   # print("banana" in x)
            contador[palabra] += 1 # si existe inc cont.
        else:
            contador[palabra] = 1  
    
    return contador

def palabra_mas_repetida(diccionario):
    palabra_mas_repetida = max(diccionario, key=diccionario.get) # maxima clave metodo get
    frecuencia = diccionario[palabra_mas_repetida]  # usamos la clave 
    return (palabra_mas_repetida, frecuencia) #retornamos la palabra y su clave

texto = input("Ingrese una cadena de texto: ")
resultado = contar_palabras(texto)
print("Diccionario de palabras y frecuencias:", resultado)

palabra_mas_repetida_tupla = palabra_mas_repetida(resultado)
print("Palabra más repetida y su frecuencia:", palabra_mas_repetida_tupla)

