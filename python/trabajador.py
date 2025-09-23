from persona import Persona

class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento="Data", puesto="Analyst"): e
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.puesto = puesto

    # Punto 2: Cambiar el método presentation
    def presentation(self):
        super().presentation()  # Llamamos a la presentación original
        print(f"Trabajo en {self.departamento} como {self.puesto}")


# ------------Ejemplo------------

trabajador_1 = Trabajador("Lucía", 28, "Producto", "PM")
trabajador_1.presentation()