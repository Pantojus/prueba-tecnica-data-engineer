from persona import Persona

class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento="Data", puesto="Analyst"): 
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.puesto = puesto

# Punto 3: añadimos los valores por defecto a las departamento='Data' y puesto=A'nalyst'

# Punto 2: Cambiar el método presentation
    def presentation(self):
        super().presentation()  # Llamamos a la presentación original
        print(f"Trabajo en {self.departamento} como {self.puesto}")


# ------------Ejemplo------------

trabajador_1 = Trabajador("Lucía", 28, "Producto", "PM")
trabajador_1.presentation()

# Punto 5: Construir usando una lista:
my_var_list = ['Andrea', '42', 'Ventas', 'Manager']
trabajador_2 = Trabajador(*my_var_list)
trabajador_2.presentation()

# Punto 6: Construir usando un diccionario:
my_var_dict = {'nombre': 'Andrea', 'edad': '42', 'departamento': 'Ventas', 'puesto': 'Manager'}
trabajador_3 = Trabajador(**my_var_dict)
trabajador_3.presentation()