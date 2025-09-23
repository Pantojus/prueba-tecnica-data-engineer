class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = int(edad)

# self.nombre es un atributo del objeto (cada instancia tiene su propio valor)
# nombre es solo la variable local, que en este caso se pasa al constructor

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")


# ------------Instancias------------

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()