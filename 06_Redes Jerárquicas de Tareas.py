class Tarea:
    def __init__(self, nombre, subordtareas=None):
        self.nombre = nombre
        self.subordtareas = subordtareas or []

    def ejecutar(self):
        print(f"Ejecutando tarea: {self.nombre}")
        for subordtarea in self.subordtareas:
            subordtarea.ejecutar()


# Crear tareas
tarea_principal = Tarea("Tarea Principal", [
    Tarea("Subtarea 1"),
    Tarea("Subtarea 2", [
        Tarea("Subsubtarea 1"),
        Tarea("Subsubtarea 2")
    ]),
    Tarea("Subtarea 3")
])

# Ejecutar la tarea principal (y sus sub-tareas)
tarea_principal.ejecutar()
