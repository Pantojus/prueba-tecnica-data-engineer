class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = int(edad)

# Punto 4: 
#
#'self.nombre' es un ATRIBUTO de la instancia (estado propio del objeto).
#'nombre' es una VARIABLE local en el ámbito actual (no necesariamente ligada al objeto).
#En métodos de instancia, 'self' referencia al objeto y 'self.nombre' accede a su estado.

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")


# ------------Instancias------------

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()