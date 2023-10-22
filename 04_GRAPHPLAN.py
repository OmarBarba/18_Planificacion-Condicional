estados = ["A", "B", "C", "D"]
acciones = ["A->B", "B->C", "A->D"]

grafo_planificacion = {
    "estados": estados,
    "acciones": acciones
}

def generar_plan(grafo):
    plan = []
    for accion in grafo["acciones"]:
        plan.append(accion)
    return plan

plan = generar_plan(grafo_planificacion)

print("Plan de acción:")
for accion in plan:
    print(accion)
