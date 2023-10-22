def planificar_tarea(estado_inicial, condicion):
    if condicion == "buena":
        plan = ["Realizar tarea A", "Realizar tarea B", "Realizar tarea C"]
    elif condicion == "regular":
        plan = ["Realizar tarea A", "Realizar tarea C"]
    else:
        plan = ["Realizar tarea B", "Realizar tarea C"]
    return plan

# Definir el estado inicial y la condición
estado_inicial = "Estado inicial"
condicion_actual = "buena"

# Generar un plan condicional
plan_condicional = planificar_tarea(estado_inicial, condicion_actual)

# Imprimir el plan generado
print("Plan condicional:")
for paso, accion in enumerate(plan_condicional, 1):
    print(f"Paso {paso}: {accion}")
