'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
- Un constructor.
- Los setters y getters para el nuevo atributo.
- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
  tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
  mayor de edad pero menor de 25 años y falso en caso contrario.
- Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
'''
# Herencia multiple
# Class persona 
class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    def es_mayor_de_edad(self):
        return self.__edad >= 18
    
    def nombre_completo(self):
        return f"\nNombre:{self.__nombre} Edad:{self.__edad}  DNI:{self.__dni}"
    
# Class cuenta
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
            
    
    def mostrar(self):
        print("Titular:", self.__titular.nombre_completo())
        print("Cantidad:", self.__cantidad)

class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion, cantidad=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        if bonificacion >= 0:
            self.__bonificacion = bonificacion
    
    def es_titular_valido(self):
        return self._Cuenta__titular.es_mayor_de_edad() and self._Cuenta__titular.es_mayor_de_edad() < 25
            
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
            print("Puede retirar dinero. Titular valido.")
        else:
            print("No se puede retirar dinero. Titular no valido.")
    
    def mostrar(self):
        return f"Cuenta Joven - Bonificacion: {self.__bonificacion}%"

# Instancia de Persona 
persona1 = Persona("Ana", 20, 87654321)

# Instancia de Cuenta
cuenta1 = Cuenta(persona1, 1000.0)
cuenta1.mostrar()

# Instancia de CuentaJoven
cuenta_joven = CuentaJoven(persona1, 50, 500.0)

# Mostrar información de la cuenta joven
print(cuenta_joven.mostrar())

# Retirar dinero
cuenta_joven.retirar(500.0)


