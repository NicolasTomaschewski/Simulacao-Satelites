import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox
import math

# Função para solicitar os valores iniciais
def solicitar_valores_iniciais():
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal
    num_manobras = simpledialog.askinteger("Número de Manobras", "Insira o número de manobras que deseja calcular:")
    a_inicial = simpledialog.askfloat("Posição Inicial", "Insira a posição inicial do veículo em km:")
    a_final = simpledialog.askfloat("Posição Final", "Insira a posição final do veículo em km:")
    velocidade_inicial = simpledialog.askfloat("Velocidade Inicial", "Insira a velocidade inicial do veículo:")
    tempo_inicial = simpledialog.askfloat("Tempo Inicial", "Insira o tempo necessário para o satélite completar uma volta completa ao redor da terra:")
    root.destroy()  # Fechar a janela
    return num_manobras, a_inicial, a_final, velocidade_inicial, tempo_inicial

# Função para calcular os parâmetros de cada manobra
def calcular_manobras(num_manobras, a_inicial, a_final, velocidade_inicial, tempo_inicial):
    a_list = np.linspace(a_inicial, a_final, num_manobras + 1)
    orbitas = []
    for i in range(num_manobras):
        a1 = a_list[i]
        a2 = a_list[i + 1]
        
        modulo1 = math.sqrt((2 * (a2 / a1))/((a2 / a1) + 1)) - 1
        if modulo1 <= 0:
            modulo1 = modulo1 * (-1)
        deltav1 = velocidade_inicial * modulo1

        modulo2 = (1 - math.sqrt((2 / ((a2 / a1) + 1))))
        if modulo2 <= 0:
            modulo2 = modulo2 * (-1)
        deltav2 = velocidade_inicial * modulo2 * (math.sqrt(a1 / a2))

        tempo_total = 0.5 * ((1 + (a2 / a1)) / 2) ** (3 / 2) * tempo_inicial
        
        orbitas.append((a1, a2, deltav1, deltav2, tempo_total))
    return orbitas

# Criação da janela para solicitar os valores das órbitas
def criar_janela():
    # Função para gerar a figura quando o botão for clicado
    def gerar_figura():
        num_manobras, a_inicial, a_final, velocidade_inicial, tempo_inicial = solicitar_valores_iniciais()
        orbitas = calcular_manobras(num_manobras, a_inicial, a_final, velocidade_inicial, tempo_inicial)
        desenhar_figura(orbitas)

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
def desenhar_figura(orbitas):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    fig.patch.set_facecolor('black')  # Define a cor de fundo da figura
    ax.set_facecolor('black')  # Define a cor de fundo dos eixos
    ax.set_ylim(0, max([a2 for a1, a2, deltav1, deltav2, tempo_total in orbitas]))

    # Define a cor dos rótulos e dos ticks
    ax.tick_params(colors='white')  # Define a cor dos ticks
    ax.yaxis.label.set_color('white')  # Define a cor do rótulo do eixo y
    ax.xaxis.label.set_color('white')  # Define a cor do rótulo do eixo x
    ax.title.set_color('white')  # Define a cor do título

    # Adiciona o título com tamanho maior
    ax.set_title("Manobras de Hohmann em 2-D", fontsize=20)

    for i, (a1, a2, deltav1, deltav2, tempo_total) in enumerate(orbitas):
        r1 = a1
        r2 = a2
        aTransfer = (r1 + r2) / 2

        # Função de posição radial em coordenadas polares
        def r(t, a, e):
            return a * (1 - e**2) / (1 + e * np.cos(t))

        e1 = 0  # Órbita inicial circular
        eTransfer = (r2 - r1) / (r2 + r1)  # Órbita de transferência elíptica
        e2 = 0  # Órbita final circular

        theta_transfer = np.linspace(0, np.pi, 100)
        r_transfer = r(theta_transfer, aTransfer, eTransfer)

        theta_final = np.linspace(0, 2 * np.pi, 200)
        r_final = r(theta_final, r2, e2)

        # Trajetórias
        if i == 0:
            ax.plot(np.linspace(0, 2 * np.pi, 100), [r1] * 100, color='blue', linestyle='--', label='Órbita inicial')  # Órbita inicial circular
        else:
            ax.plot(np.linspace(0, 2 * np.pi, 100), [r1] * 100, color='white', linestyle='--')  # Outras órbitas iniciais

        ax.plot(theta_transfer, r_transfer, color='orange', label='Órbita intermediária' if i == 0 else "")  # Trajetória de transferência
        ax.plot(np.linspace(0, 2 * np.pi, 100), [r2] * 100, color='red', linestyle='--', label='Órbita final' if i == 0 else "")  # Órbita final circular

    # Adiciona um ponto azul no centro para representar o planeta
    ax.plot(0, 0, 'bo', label='Planeta (Terra)')
    ax.legend(loc='lower left')  # Define a posição da legenda
    plt.show()

# Chamada para solicitar os valores das órbitas
criar_janela()
