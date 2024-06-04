import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros
a1 = 7000  # Semi-eixo maior da órbita inicial em km
a2 = 42164  # Semi-eixo maior da órbita geostacionária em km
mu = 3.986 * 10**5  # Constante gravitacional da Terra em km^3/s^2

# Raio da órbita inicial e final
r1 = a1
r2 = a2

# Órbita de transferência
aTransfer = (r1 + r2) / 2

# Funções de posição
def r(t, a, e):
    return a * (1 - e**2) / (1 + e * np.cos(t))

def x(t, a, e):
    return r(t, a, e) * np.cos(t)

def y(t, a, e):
    return r(t, a, e) * np.sin(t)

# Excentricidades
e1 = 0  # Órbita inicial circular
eTransfer = (r2 - r1) / (r2 + r1)  # Órbita de transferência elíptica
e2 = 0  # Órbita final circular

# Trajetórias
trajectoryTransfer = np.array([[x(t, aTransfer, eTransfer), y(t, aTransfer, eTransfer)] for t in np.linspace(0, np.pi, 100)])
trajectoryFinal = np.array([[x(t, r2, e2), y(t, r2, e2)] for t in np.linspace(0, 2*np.pi, 200)])

# Criação da figura e eixos
fig, ax = plt.subplots()
ax.set_xlim(-a2, a2)
ax.set_ylim(-a2, a2)
ax.set_aspect('equal')
ax.plot(*zip(*trajectoryTransfer), color='blue')  # Trajetória de transferência (não precisa ser animada)
orbit_initial, = ax.plot([], [], 'o', color='red')
orbit_final, = ax.plot([], [], 'o', color='red')

# Desenhar órbitas
circle1 = plt.Circle((0, 0), r1, color='gray', fill=False)
circle2 = plt.Circle((0, 0), r2, color='gray', fill=False)
ax.add_patch(circle1)
ax.add_patch(circle2)

def init():
    orbit_initial.set_data([], [])
    orbit_final.set_data([], [])
    return orbit_initial, orbit_final

def update(frame):
    if frame < 200:
        t = 2 * np.pi * frame / 200
        orbit_initial.set_data(x(t, r1, e1), y(t, r1, e1))
        orbit_final.set_data([], [])
    elif frame < 300:
        t = np.pi * (frame - 200) / 100
        orbit_initial.set_data([], [])
        orbit_final.set_data(x(t, aTransfer, eTransfer), y(t, aTransfer, eTransfer))
    else:
        t = 2 * np.pi * (frame - 300) / 200
        orbit_initial.set_data([], [])
        orbit_final.set_data(x(t, r2, e2), y(t, r2, e2))
    return orbit_initial, orbit_final

# Criação da animação
ani = FuncAnimation(fig, update, frames=np.arange(0, 500), init_func=init, blit=True)

# Exibir a animação
plt.show()
