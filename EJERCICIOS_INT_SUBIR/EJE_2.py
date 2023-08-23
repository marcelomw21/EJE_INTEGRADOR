
# Escribir una función que calcule el mínimo común múltiplo entre dos números

def CalcularMCD(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

def CalcularMCM(a, b):
    return (a * b // CalcularMCD(a, b))


numero1 = int(input("Ingrese el primer  Nro: "))
numero2 = int(input("Ingrese el segundo Nro: "))

resultado = CalcularMCM(numero1, numero2)
print("El Mínimo Común Múltiplo entre", numero1, "y", numero2, "es:", resultado)