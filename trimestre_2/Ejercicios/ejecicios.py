
class coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_info(self):
        print(f"coche: {self.marca} {self.modelo} ({self.color})")

coche1=coche("toyota", "Corolla" , "Rojo" )
coche1.mostrar_info()


"""class persona:
    def __init__(self, nombre, edad):
     self.nombre = nombre
     self.edad = edad
    def cumplir_años(self):
       self.edad +=1
    def mostrar_info(self):
       print(f"{self.nombre} tiene {self.edad} años")

persona1 = persona("juan", 20)
persona1.mostrar_info()
persona1.cumplir_años()
persona1.mostrar_info()"""


"""class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def mostrar_info (self):
        return f"{self.nombre} tiene {self.edad} años"
class Empleado(persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto=puesto
    def mostrar_info(self):
        return f"{self.nombre} tiene {self.edad} años y trabaja como {self.puesto}"
    
empleado1=Empleado ("ana", 30, "Desarrolladora")
print(empleado1.mostrar_info())
persona1 = persona("cristian",26)
print(persona1.mostrar_info())"""


"""class animal:
    def hablar(self):
        raise NotImplementedError("El metodo hablar debe ser implementado por subclases")

class perro:
    def hablar(self):
        print("guau")

class gato:
    def hablar(self):
        print("miau")

perro ="""""