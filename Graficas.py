import matplotlib
from  matplotlib import pyplot as plt
import Funciones
from Funciones import alq

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
                figsize=(14,7),
                facecolor="#d4d4d4")    
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
        plt.title('Servicios Básicos de Casas en Venta',
        fontname="Bell MT",
        fontsize=30,
        pad=10
        )
        plt.grid(True,
                color="#1757C6",
                )
        return plt.show()

def barras(x,y):
        plt.figure(
        figsize=(14,6.2),
        facecolor="#d4d4d4")

        plt.bar(x,y,
                width=0.5,
                align="center",
                bottom=0,
                color="#2531D8",
                edgecolor="#9E0303",
                )
        plt.xticks(
                fontname="Algerian",
                fontsize=20,
                color="black",
                fontweight="bold")
        plt.yticks([0,5,10,15,20],
                fontname="Algerian",
                fontsize=15)
        plt.xlim(-0.5,1.5)
        plt.ylim(0,20)
        plt.title("Cantidad de varones y hembras en el curso",
                fontsize=20,
                fontname="Algerian",
                loc="center",
                pad=10,
                color="#000000")
        plt.text(0,18,"18", ha="center", va="bottom",
                fontname="Calibri",
                fontsize=13,
                fontweight="bold")
        plt.text(1,10,"10", ha="center", va="bottom",
                fontname="Calibri",
                fontsize=13,
                fontweight="bold")
        plt.hlines(18,-0.5,-0.25,
                linestyles="--",
                colors="#2531D8",
                linewidth=1)

        plt.hlines(10,-0.5,1.25,
                linestyles="--",
                colors="#2531D8",
                linewidth=1)
        plt.xlabel("Genero",
                fontname="Algerian",
                fontsize=25)
        plt.ylabel("Cantidad",
                fontname="Algerian",
                fontsize=25,
                labelpad=20)
        plt.grid(False)
        return plt.show()
barras(["Hembras","Varones"],[18,10])