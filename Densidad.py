import matplotlib.pyplot as plt
import math
import statistics
import numpy as np

def casas_cuartos():
    # lista con los 90 valores
    precios = [270, 250, 550, 500, 450, 600, 300, 450, 600, 300, 500, 450, 150, 350, 250, 350, 700, 400, 500, 350, 280, 500, 550, 600, 200, 400, 400, 200, 200, 250, 300, 300, 250, 250, 150, 300, 350, 230, 300, 300, 250, 300, 400, 350, 250, 100, 150, 450, 450, 300, 250, 250, 350, 250, 200, 300, 400, 250, 200, 150, 350, 200, 230, 200, 400, 150, 500, 250, 350, 200, 300, 750, 250, 230, 300, 650, 300, 350, 250, 200, 350, 100, 200, 300, 250, 200, 300, 350, 200, 200]  

    zona_a = precios[0:30]
    zona_b = precios[30:60]
    zona_c = precios[60:90]

    datos = [zona_a, zona_b, zona_c]
    etiquetas = ["Plaza de la Revolución", "Centro Habana", "Playa"]
    colores = ["#66c2a5", "#fc8d62", "#8da0cb"]

    # ---- KDE gaussiano en Python puro ----
    def kde(valores, x, h):
        """Densidad de kernel gaussiano en el punto x con ancho de banda h."""
        n = len(valores)
        s = 0.0
        for xi in valores:
            u = (x - xi) / h
            s += math.exp(-0.5 * u * u) / math.sqrt(2 * math.pi)
        return s / (n * h)

    def silverman_h(valores):
        """Ancho de banda óptimo según la regla de Silverman."""
        n = len(valores)
        sigma = statistics.stdev(valores)
        return 1.06 * sigma * n ** (-1 / 5)

    # ---- Rango común del eje X para las tres zonas ----
    todos = zona_a + zona_b + zona_c
    x_min = 0
    x_max = 800
    pasos = 300
    xs = [x_min + i * (x_max - x_min) / (pasos - 1) for i in range(pasos)]

    fig, ax = plt.subplots(figsize=(9, 6))

    # ---- Dibujar una curva de densidad por zona ----
    for grupo, etiqueta, color in zip(datos, etiquetas, colores):
        h = silverman_h(grupo)
        ys = [kde(grupo, x, h) for x in xs]
        xs_array=np.array(xs)
        ys_array=np.array(ys)
        precio_min=min(precios)
        ys_array[xs_array < precio_min]=0
        ax.plot(xs_array, ys_array, color=color, linewidth=2, label=etiqueta)
        ax.fill_between(xs, ys, color=color, alpha=0.25)

    # ---- Ejes y estilo ----
    ax.set_xlabel("Precio de alquiler")
    ax.set_ylabel("Densidad")
    ax.set_title("Densidad de precios de alquiler por zona (n = 30 por zona)")
    ax.grid(linestyle="--", alpha=0.4)
    ax.legend(loc="best")

    plt.xlim(100,x_max)
    plt.ylim(bottom=0)

    plt.tight_layout()
    return plt.show()
casas_cuartos()