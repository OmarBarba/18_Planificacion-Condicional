from collections import defaultdict

# Definir las tareas y sus dependencias
tasks = {
    "A": [],
    "B": ["A"],
    "C": ["A"],
    "D": ["B", "C"],
    "E": ["D"],
    "F": [],
}

# Crear un diccionario para almacenar el estado de las tareas
task_state = defaultdict(lambda: "no_realizada")

# Función para ejecutar una tarea y cambiar su estado
def realizar_tarea(task):
    task_state[task] = "realizada"
    print(f"Tarea {task} realizada.")

# Función para verificar si todas las dependencias de una tarea están completas
def dependencias_completas(task):
    return all(task_state[dep] == "realizada" for dep in tasks[task])

# Planificación de orden parcial
while any(state == "no_realizada" for state in task_state.values()):
    for task, state in task_state.items():
        if state == "no_realizada" and dependencias_completas(task):
            realizar_tarea(task)

# Imprimir el estado final de las tareas
for task, state in task_state.items():
    print(f"Tarea {task} está {state}.")
