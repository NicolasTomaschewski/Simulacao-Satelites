import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import simpledialog, messagebox
import math

# Função para solicitar os valores das órbitas
def solicitar_valores_orbitas():
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal
    a1 = simpledialog.askfloat("Valor da órbita inicial", "Insira o raio da órbita inicial em km:")
    a2 = simpledialog.askfloat("Valor da órbita final", "Insira o raio da órbita final em km:")
    velocidade_inicial = simpledialog.askfloat("Velocidade inicial", "Insira a velocidade inicial do veículo (em m/s):")
    tempo_inicial = simpledialog.askfloat("Tempo necessário", "Insira o tempo necessário para o satélite completar uma volta completa ao redor da Terra (em segundos):")
    
    modulo1 = math.sqrt((2 * (a2 / a1)) / ((a2 / a1) + 1)) - 1
    deltav1 = velocidade_inicial * modulo1

    modulo2 = 1 - math.sqrt(2 / ((a2 / a1) + 1))
    deltav2 = velocidade_inicial * modulo2 * math.sqrt(a1 / a2)

    tempo_total = 0.5 * ((1 + (a2 / a1)) / 2) ** (3 / 2) * tempo_inicial

    root.destroy()  # Fechar a janela
    
    messagebox.showinfo("Resultados", "Delta V1 = {:.2f}\nDelta V2 = {:.2f}\nTempo Total = {:.2f} segundos".format(deltav1, deltav2, tempo_total))
    
    return a1, a2

# Criação da janela para solicitar os valores das órbitas
def criar_janela():
    # Função para gerar a figura quando o botão for clicado
    def gerar_figura():
        a1, a2 = solicitar_valores_orbitas()
        if a1 is not None and a2 is not None:
            desenhar_figura(a1, a2)

    # Função para fechar a janela
    def sair():
        janela.destroy()

    # Criação da janela
    janela = tk.Tk()
    janela.title("Solicitar Valores de Órbitas")
    
    # Label e botão
    label = tk.Label(janela, text="Clique no botão para inserir os valores das órbitas.")
    label.pack(padx=10, pady=10)

    botao_inserir = tk.Button(janela, text="Inserir Dados", command=gerar_figura)
    botao_inserir.pack(padx=10, pady=5)

    botao_sair = tk.Button(janela, text="Sair", command=sair)
    botao_sair.pack(padx=10, pady=5)

    janela.mainloop()

# Desenhar a figura com os valores das órbitas inseridos
def desenhar_figura(a1, a2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Função de posição radial em coordenadas polares
    def r(t, a, e):
        return a * (1 - e**2) / (1 + e * np.cos(t))

    # Raio da órbita inicial e final
    r1 = a1
    r2 = a2

    # Órbita de transferência
    aTransfer = (r1 + r2) / 2

    # Excentricidades
    e1 = 0  # Órbita inicial circular
    eTransfer = (r2 - r1) / (r2 + r1)  # Órbita de transferência elíptica
    e2 = 0  # Órbita final circular

    # Trajetórias
    theta_transfer = np.linspace(0, np.pi, 100)
    r_transfer = r(theta_transfer, aTransfer, eTransfer)

    theta_final = np.linspace(0, 2 * np.pi, 200)
    r_final = r(theta_final, r2, e2)

    # Plot das órbitas
    ax.plot(r1 * np.cos(theta_final), r1 * np.sin(theta_final), 0, color='blue', label='Órbita Inicial')
    ax.plot(r_transfer * np.cos(theta_transfer), r_transfer * np.sin(theta_transfer), 0, color='orange', label='Órbita de Transferência')
    ax.plot(r2 * np.cos(theta_final), r2 * np.sin(theta_final), 0, color='red', label='Órbita Final')

    # Adiciona um ponto azul no centro para representar o planeta
    ax.scatter(0, 0, 0, color='blue', label='Planeta (Terra)')

    # Configurações adicionais
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Manobra de Hohmann em 3D')
    ax.legend()

    plt.show()

# Chamada para solicitar os valores das órbitas
criar_janela()
