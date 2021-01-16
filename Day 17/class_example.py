class Persona:

    def __init__(self, nombre, nacionalidad):
        self.nombre = input('Nombre: ')
        self.nacionalidad = nacionalidad

persona1 = Persona("",'chileno')

print(persona1.nombre)

