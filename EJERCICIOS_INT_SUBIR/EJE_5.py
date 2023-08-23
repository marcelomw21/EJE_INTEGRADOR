
# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

#De forma iterativa:
def get_int():
    while True:
        try: # bloque generará una excepción, no está definido:
            valor = int(input("Ingrese un valor entero: "))
            return valor    # si es de ipo INT fializa el bucle while de lo contrario
        except ValueError:  # se eecuta except solicitando reingreso del valor
            print("Error: Ingrese un valor válido.")

# main prog.
entero = get_int()
print("Valor entero ingresado:", entero)


# De forma Recursiva:
def get_int():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor # si es de tipo int no hay error 
    except ValueError:
        print("Error: Ingrese un valor válido.")
        return get_int() # A difencia del iterativo al haber un error 
                         # con el tipo de dato se hace 
                         # una llamada recursiva a la fucion get_int()
# main prog.
entero = get_int()
print("Valor entero ingresado:", entero)
