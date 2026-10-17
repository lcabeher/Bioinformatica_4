pi = 3.1416

def saludar(nombre):
    return f"¡Hola, {nombre}!"

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentar(self):
        return f"Hola, me llamo {self.nombre}"
