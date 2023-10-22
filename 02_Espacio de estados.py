# Definición de estados y operadores
estados = ["A", "B", "C"]
operadores = [
    ("Operador1", "A", "B"),  # Desde A a B
    ("Operador2", "A", "C"),  # Desde A a C
]

# Función para aplicar un operador a un estado
def aplicar_operador(estado, operador):
    if operador[1] == estado:
        return operador[2]
    return estado

# Generar el espacio de estados
espacio_de_estados = []
for estado_inicial in estados:
    estado_actual = estado_inicial
    plan = [estado_actual]
    for _ in range(3):  # Realizar 3 pasos en el espacio de estados
        operador_elegido = operadores[0]  # Usar el primer operador (puedes cambiarlo)
        estado_actual = aplicar_operador(estado_actual, operador_elegido)
        plan.append(estado_actual)
    espacio_de_estados.append(plan)

# Imprimir el espacio de estados
for i, plan in enumerate(espacio_de_estados):
    print(f"Plan {i + 1}: {' -> '.join(plan)}")
