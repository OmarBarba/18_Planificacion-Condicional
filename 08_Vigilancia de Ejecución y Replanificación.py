class Planificador:
    def __init__(self, plan_inicial, objetivo):
        self.plan_actual = plan_inicial
        self.objetivo = objetivo

    def ejecutar_plan(self):
        print("Ejecutando plan:")
        for accion in self.plan_actual:
            print(accion)
        print("Plan ejecutado.")

    def replanificar(self, nuevo_objetivo):
        print(f"Replanificando para alcanzar el objetivo: {nuevo_objetivo}")
        # En una aplicación real, aquí se generaría un nuevo plan en función del nuevo objetivo.
        self.plan_actual = ["Paso 1", "Paso 2", "Paso 3"]

    def vigilar_ejecucion(self):
        print(f"Vigilando la ejecución hacia el objetivo: {self.objetivo}")
        ejecucion_exitosa = True  # En una aplicación real, esto se basaría en la monitorización del entorno.
        
        if not ejecucion_exitosa:
            print("Se detectó una desviación en la ejecución.")
            nuevo_objetivo = "Nuevo objetivo"  # En una aplicación real, esto se determinaría en función de la desviación.
            self.replanificar(nuevo_objetivo)
            self.ejecutar_plan()

# Crear un planificador con un plan inicial y objetivo
plan_inicial = ["Paso 1", "Paso 2", "Paso 3"]
objetivo = "Objetivo final"
planificador = Planificador(plan_inicial, objetivo)

# Ejecutar el plan inicial
planificador.ejecutar_plan()

# Simular una desviación en la ejecución (puedes ajustar este escenario)
ejecucion_exitosa = False

# Vigilar la ejecución y replanificar en caso de problemas
planificador.vigilar_ejecucion()
