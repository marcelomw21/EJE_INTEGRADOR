#Escribir una función que calcule el máximo común divisor entre dos números.
def MCD(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

numero1 = int(input("Ingrese el primer Nro: "))
numero2 = int(input("Ingrese el segundo Nro: "))

resultado = MCD(numero1, numero2)
print("El Máximo Común Divisor de", numero1, "y", numero2, "es:", resultado)
