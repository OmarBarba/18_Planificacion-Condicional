from pyswip import Prolog

prolog = Prolog()

# Definir reglas de planificación
prolog.assertz("accion(ir_a, A, B) :- puede_ir(A, B), no_bloqueado(A), no_bloqueado(B)")
prolog.assertz("puede_ir(A, B) :- conexion(A, B)")
prolog.assertz("no_bloqueado(A) :- no_obstaculo(A)")

# Consultar plan
for solucion in prolog.query("accion(ir_a, inicio, destino)"):
    print(f"Plan: {solucion['inicio']} -> {solucion['destino']}")
