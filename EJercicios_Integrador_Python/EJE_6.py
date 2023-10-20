'''Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
   siguientes métodos para la clase:
   -Un constructor, donde los datos pueden estar vacíos.
   -Los setters y getters para cada uno de los atributos.Hay que validar las entradas dedatos.
   -mostrar(): Muestra los datos de la persona.
   -Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. 
'''

class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property # Getter
    def nombre(self):
        return f'{self.__nombre}'
    
    @property # Getter
    def edad(self):
        return f'{self.__edad}'
    
    @property # Getter
    def dni(self):
        return f'{self.__dni}'
    
    @nombre.setter # Setter
    def nombre(self, nuevo_nombre):
        while nuevo_nombre=="":  # Verificar si el nombre no eta vacio
            print("El nombre no puede estar vacio") 
            nuevo_nombre=(input("Ingrese un Nombre: "))  
        self.__nombre = nuevo_nombre
        

    @edad.setter # Setter
    def edad(self, nueva_edad):         
        while True: # agregar try para validar
            try: # bloque generará una excepción, no está definido:           
               while nueva_edad <=0:
                   nueva_edad= int(input("Ingrese la Edad: "))                      
               self.__edad = nueva_edad
               break     
            except ValueError:  # se eecuta except solicitando reingreso del valor
              print("Error: Ingrese un entero para la Edad.") 

    @dni.setter # Setter
    def dni(self, nuevo_dni):
        while len(nuevo_dni)!=8:  # Verificar si el DNI tiene 8 dígitos 
            print("Error: El DNI debe tener 8 dígitos.") 
            nuevo_dni=(input("Ingrese un DNI: "))   
        self.__dni = nuevo_dni
                   
    @property # Getter
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")

    @property # Getter
    def mayor_de_edad(self):
        if self.__edad >= 18:
            print("Es mayor de edad.")
        else:
            print("No es mayor de edad.")

# Crear una instancia de Persona
persona1 = Persona(None,None,None)

# Establecer atributos usando setters
persona1.nombre=(input("Ingrese un Nombre: "))
persona1.edad=int(input("Ingrese la Edad: ")) 
persona1.dni=str(input("Ingrese un DNI: "))

# Mostrar los datos de la persona
persona1.mostrar

# Verificar si es mayor de edad
persona1.mayor_de_edad
# Su edad
print(f'Su Edad: {persona1.edad} Años')
