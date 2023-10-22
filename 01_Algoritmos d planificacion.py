estado_inicial = {"luz_encendida": True}
objetivo = {"luz_encendida": False}

def apagar_luz(estado):
    if estado["luz_encendida"]:
        nuevo_estado = estado.copy()
        nuevo_estado["luz_encendida"] = False
        return nuevo_estado
    return estado

plan = []

while estado_inicial != objetivo:
    estado_inicial = apagar_luz(estado_inicial)
    plan.append("Apagar la luz")

print("Plan:")
for accion in plan:
    print(accion)
