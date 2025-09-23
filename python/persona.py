class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = int(edad)

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")