import matplotlib.pyplot as plt

# Definir dos agentes con posiciones iniciales y objetivos
agente1 = {"posicion": (1, 1), "objetivo": (4, 4)}
agente2 = {"posicion": (2, 2), "objetivo": (4, 1)}

# Función para mover un agente hacia su objetivo
def mover_agente(agente):
    x, y = agente["posicion"]
    objetivo_x, objetivo_y = agente["objetivo"]
    
    if x < objetivo_x:
        x += 0.5
    elif x > objetivo_x:
        x -= 0.5
    
    if y < objetivo_y:
        y += 0.5
    elif y > objetivo_y:
        y -= 0.5
    
    agente["posicion"] = (x, y)

# Simular la planificación continua y multiagente
num_pasos = 20
posiciones_agente1 = []
posiciones_agente2 = []

for _ in range(num_pasos):
    posiciones_agente1.append(agente1["posicion"])
    posiciones_agente2.append(agente2["posicion"])
    mover_agente(agente1)
    mover_agente(agente2)

# Visualizar el movimiento de los agentes
x_agente1, y_agente1 = zip(*posiciones_agente1)
x_agente2, y_agente2 = zip(*posiciones_agente2)

plt.plot(x_agente1, y_agente1, label="Agente 1")
plt.plot(x_agente2, y_agente2, label="Agente 2")
plt.scatter([agente1["objetivo"][0], agente2["objetivo"][0]], [agente1["objetivo"][1], agente2["objetivo"][1]], color='red', marker='x', label="Objetivos")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Movimiento de Agentes')
plt.legend()
plt.grid(True)
plt.show()
