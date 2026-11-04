import matplotlib
from  matplotlib import pyplot as plt
import statistics
import numpy as np
import math
import Funciones
from Funciones import alq
from Funciones import cxc

def scatter_serv():
        x_ll=Funciones.servicios_alquileres("servicios")    
        pr=Funciones.precios_alquileres()
        for i in range(len(pr)):
                for j in range(len(pr)-1):
                        if pr[j]>pr[j+1]:
                                pr[j], pr[j+1]=pr[j+1],pr[j]
                                x_ll[j], x_ll[j+1]=x_ll[j+1],x_ll[j]    
        for i in range(len(pr)):
                pr[i]=f"$ {pr[i]}"    
        y_l=[]
        for i in range(len(x_ll)):
                for j in range(len(x_ll[i])):
                        y_l.append(i)    
        x_l=[]
        for i in range(len(x_ll)):
                for j in range(len(x_ll[i])):
                        x_l.append(x_ll[i][j])    
        plt.figure(
                figsize=(12,6),
                facecolor="#d4d4d4",
                dpi=1080)    
        plt.scatter(x_l,y_l,
                s=50,
                facecolor="#1757C6",
                #color="#130303"
                )
        plt.xticks(
        ticks=range(8),
        fontsize=16,
        fontname="Bell MT",
        labels=["Respaldo\n Energético","Tanque de\n Agua","Teléfono Fijo","Wifi","Climatización","Gas de la\n Calle","Calentador","Lavadora"]
        )
        plt.yticks(
        ticks=range(30),
        labels=pr,
        fontname="Bell MT",
        fontsize=15
        )
        plt.xlabel("Servicios Básicos",
        fontname="Bell MT",
        fontsize=20,
        labelpad=1
        )
        plt.ylabel("Precio por casa en USD",
        fontname="Bell MT",
        fontsize=25,
        labelpad=10
        )
        plt.title('Servicios Básicos de Casas en Alquileres',
        fontname="Bell MT",
        fontsize=30,
        pad=10
        )
        plt.grid(True,
                color="#1757C6",
                )
        return plt.show()

def barras():
        y=Funciones.precios_casas()
        x=["1 cuarto", "2 cuartos", "3 cuartos"]
        plt.figure(
                figsize=(14,6.2),
                facecolor="#d4d4d4",
                dpi=1080
                )
        plt.bar(x,y,
                width=0.5,
                align="center",
                bottom=0,
                color="#2531D8",
                #edgecolor="#D00909"
                )
        plt.xticks(
                fontname="Bell MT",
                fontsize=15,
                color="black",
                fontweight="bold")
        plt.yticks(
                fontname="Bell MT",
                fontsize=15)
        plt.xlim(-0.5,2.5)
        #plt.ylim()
        plt.title("Precio Promedio de Casas en Venta \nen dependencia de la cantidad de cuartos",
                fontsize=20,
                fontname="Bell MT",
                loc="center",
                pad=10,
                color="#000000")
        plt.text(0,9523,"$ 9523", ha="center", va="bottom",
                fontname="Bell MT",
                fontsize=13,
                fontweight="bold")
        plt.text(1,26066,"$ 26066", ha="center", va="bottom",
                fontname="Bell MT",
                fontsize=13,
                fontweight="bold")
        plt.text(2,45733,"$ 45733", ha="center", va="bottom",
                fontname="Bell MT",
                fontsize=13,
                fontweight="bold")
        plt.hlines(9523,-0.5,0,
                linestyles="--",
                colors="#2531D8",
                linewidth=1)
        plt.hlines(26066,-0.5,1,
                linestyles="--",
                colors="#2531D8",
                linewidth=1)
        plt.hlines(45733,-0.5,2,
                linestyles="--",
                colors="#2531D8",
                linewidth=1)
        plt.xlabel("Cantidad de Cuartos",
                fontname="Bell MT",
                fontsize=16,
                labelpad=10)
        plt.ylabel("Precio Promedio en USD",
                fontname="Bell MT",
                fontsize=16,
                labelpad=10)
        plt.grid(False)
        return plt.show()

def comp_países():
        data=[
                ("Brasil", 7710, 91698),
                ("El Salvador", 5249, 90000),
                ("México", 4792, 96982),
                ("Cuba", 204, 16500)]
        labels=['0']
        years=[0]
        for país, salario, vivienda in data:
                labels.append(f"{país}\nSalario: \\${salario}/año|Casa: \\${vivienda}")
                years.append(vivienda/salario)
        plt.figure(figsize=(14,6),
                facecolor="#eadddd",
                edgecolor="#d45050")
        plt.plot(labels,years,
                marker=".",
                color="blue"
                )
        plt.xticks(fontname="Bell MT",
                fontsize=12
                )
        plt.yticks(fontname="Bell MT",
                fontsize=15
                )
        plt.xlim(0,4.5)
        plt.ylim(0,90)
        plt.xlabel("Países con sus Salarios Promedios y Precio Promedio de Casas en Venta",
                fontname="Bell MT",
                fontsize=18,
                labelpad=8)
        plt.ylabel("Años de salario íntegro necesarios\n para comprar la vivienda",
                fontname="Bell MT",
                fontsize=18,
                labelpad=10)
        plt.grid(linestyle="--", alpha=0.4)
        plt.title("Años para comprar una vivienda destinando el 100% del salario anual (2025)",
                fontname="Bell MT",
                fontsize=20,
                color="black")
        plt.vlines(x=labels, ymin=-10, ymax=years, linestyles="--", linewidth=1, colors="blue")
        return plt.show()

def type_casa():
        y=[15000,23000,30000,36000,38500,60000]
        x=["Apartamento","Casas","Colonial","Biplanta","Casa de campo","Casas \nIndependientes"]
        plt.figure(figsize=(12,6),
                facecolor="#dccfcf"
                )
        plt.barh(x,y,
                height=0.7,
                color="#1D6ACE",
                edgecolor="black")
        #plt.subplots_adjust(left=0.15, right=0.9, top=0.95, bottom=0.03)
        plt.yticks(ticks=range(6),
                fontsize=14,
                fontname="Bell MT"
                )
        plt.xticks(fontsize=14,
                fontname="Bell MT")
        plt.ylabel("Tipos de vivienda",
                fontname="Bell MT",
                fontsize=20,
                loc="center",
                labelpad=1)
        plt.xlabel("Mediana del Precio",
                fontname="Bell MT",
                fontsize=20,
                loc="center",
                labelpad=10)
        for i in range(len(y)):
                plt.text((y[i]//2.25),i-0.1, f"${y[i]}",
                        color="#ffffff",
                        fontname="Bell MT",
                        fontsize=20)
        #plt.grid(linestyle="--", alpha=0.4)
        plt.ylim(-1,6)
        plt.vlines(y, ymin=-1, ymax=range(len(y)), linestyles="--", linewidth=1, colors="blue" )
        plt.title("Precio Mediano por Tipo de Vivienda",
                fontname="Bell MT",
                fontsize=24)
        return plt.show()

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
        plt.xticks(fontname="Bell MT",
                fontsize=16)
        plt.yticks(fontname="Bell MT",
                fontsize=16)
        ax.set_xlabel("Precio de alquiler",
                fontname="Bell MT",
                fontsize=18)
        ax.set_ylabel("Densidad",
                fontname="Bell MT",
                fontsize=18)
        ax.set_title("Densidad de precios de alquiler por zona (n = 30 por zona)",
                fontname="Bell MT",
                fontsize=20)
        ax.grid(linestyle="--", alpha=0.4)
        ax.legend(loc="best")

        plt.xlim(100,x_max)
        plt.ylim(bottom=0)

        plt.tight_layout()
        return plt.show()