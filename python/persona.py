class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = int(edad)

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")


# ------------Instancias------------

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()