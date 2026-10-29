import matplotlib
from  matplotlib import pyplot as plt
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

def barras():
        y=Funciones.precios_casas()
        x=["1 cuarto", "2 cuartos", "3 cuartos"]

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
                fontsize=15,
                color="black",
                fontweight="bold")
        plt.yticks(
                fontname="Algerian",
                fontsize=15)
        plt.xlim(-0.5,2.5)
        #plt.ylim()
        plt.title("Precio Promedio de Casas en Venta \nen dependencia de la cantidad de cuartos",
                fontsize=20,
                fontname="Algerian",
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
                fontname="Algerian",
                fontsize=16,
                labelpad=10)
        plt.ylabel("Precio Promedio en USD",
                fontname="Algerian",
                fontsize=16,
                labelpad=10)
        plt.grid(False)
        return plt.show()
barras()