'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional.
Crear los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. 
  El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
- mostrar(): Muestra los datos de la cuenta.
- ingresar(cantidad): se ingresa una cantidad a la cuenta, 
  si la cantidad introducida es negativa, no se hará nada.
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos
'''

class Cuenta:

    def __init__(self, titular="", cantidad=0.0):
        self.__titular  = titular
        self.__cantidad = cantidad

# Metodos getter: leer valores de u atribiuto  
    @property # getter
    def titular(self):
        return self.__titular
    
    @property # getter
    def cantidad(self):
        return self.__cantidad
       
# Metodos setter: modificar valores de los atribiutos 
    @titular.setter # setter   
    def titular(self, titular):
        self.__titular = titular   

    @cantidad.setter # setter    
    def cantidad(self, cantidad):
        if cantidad >= 0:
           self.__cantidad = cantidad

    @property # Getter
    def mostrar(self):
        print(f"Titular:  {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")

    @cantidad.setter # Setter
    def ingresar(self, nuevo__ingreso):
        if nuevo__ingreso > 0:
            self.__cantidad += nuevo__ingreso
        else:
            print("ERROR: El ingreso debe ser un valor positivo!")

    @cantidad.setter # Setter
    def retirar(self, nuevo__retiro):
        if nuevo__retiro > 0:
            self.__cantidad -= nuevo__retiro


# Instancia 
mi_cuenta=Cuenta("JUAN",1000.0)

# Mostrar los datos de la cuenta
mi_cuenta.mostrar

# Ingresar dinero en la cuenta
mi_cuenta.ingresar=float(input("Cantidad a Ingresar: "))
mi_cuenta.mostrar

# Retirar dinero de la cuenta
mi_cuenta.retirar=float(input("Cantidad a Retirar: "))
mi_cuenta.mostrar

